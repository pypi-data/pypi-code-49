#!/usr/bin/python3
"""
The driving module for the command line version of Family Ledger.

Copyright (C) 2020, fondlez "Anuber"-Kronos, fondlez at protonmail.com
"""
import csv
from datetime import datetime
import gettext
import locale
import logging
import os
import sys
from collections import namedtuple
from functools import partial
from itertools import chain

import xlsxwriter

from familyledger import account
from familyledger.config import Config
from familyledger import commandline
from familyledger import dataview
from familyledger import possessions
from familyledger import version
from familyledger.utils import _console
from familyledger.utils._exception import set_exception_handler
from familyledger.utils import _file
from familyledger.utils._i18n import n_
from familyledger.utils import _iterable
from familyledger.utils import _path
from familyledger.utils import _logging
from familyledger.utils._logging import get_log
from familyledger.utils import _warcraft


FORMAT_TO_DIALECT = {
    'csv': 'excel',
    'tsv': 'excel-tab',
    'unix': 'unix',
}
"""Mapping from output file format to ``csv.writer`` dialect."""

EXCEL_TABS = (
    'factiongold', 'gold', 'item', 'character', 'location', 'mail', 'worn', 
    'raw')
"""List of Excel sheet names corresponding to a dataview."""

ExcelSheet = namedtuple('ExcelSheet', ['title', 'title_cols'])
"""Data type for Excel sheet settings."""

EXCEL_SHEETS = {
    'factiongold': ExcelSheet('Gold Per Faction', 3), 
    'gold': ExcelSheet('Gold Per Character', 3), 
    'item': ExcelSheet('Items Per Server', 2), 
    'character': ExcelSheet('Items Per Character', 3), 
    'location': ExcelSheet('Items Per Character - Location', 4), 
    'mail': ExcelSheet('Items Per Character - Mail', 4), 
    'worn': ExcelSheet('Items Per Character - Worn', 4), 
    'raw': ExcelSheet('Original Item Data', 3), 
    'about': ExcelSheet('About This Data', 2), 
}
"""Mapping from Excel sheet names to Excel sheet settings."""


def setup():
    """Sets up the debugging context for the main application.
    
    Args:
        args (:obj:`argparse.Namespace`): program arguments.
    """
    # Disables traceback output by default to be end user friendly
    sys.excepthook = partial(set_exception_handler, debug_flag=False)
    args = commandline.options().parse_args()
    # - unless the user states they want to see it
    sys.excepthook = partial(set_exception_handler, debug_flag=args.debug)
    internationalize(args)
    try:
        log_level = None
        if args.debug:
            print(args)
            log_level = logging.DEBUG
        log_level = log_level or getattr(logging, args.log_level.upper(), None)
        if not args.log_disable:
            _logging.configure_root_logger(
                log_file='{}.log'.format(_path.extless(__file__)),
                log_level=log_level)
        main(args)
    except Exception as e:
        if args.debug:
            import pdb
            import traceback
            traceback.print_exc()
            pdb.post_mortem()
        else:
            log = get_log('ledger')
            log.exception('Uncaught exception %s' % e)
            raise


def internationalize(args):
    # Internationalizes this module via the gettext standard library module.
    # Unconventional global variable placement is to enable a non-fallback
    # default language supplied from the system locale or the user.
    # PYINSTALLER: data files must be bundle-aware
    mo_path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
    mo_path = os.path.join(mo_path, 'share/locale')
    translate = gettext.translation(
        'ledger', localedir=mo_path, languages=user_lang(args.lang), 
        fallback=True)
    global _
    _ = translate.gettext

            
def main(args):
    """Starts the main application.
    
    Args:
        args (:obj:`argparse.Namespace`): program arguments.
    """
    checked_args = validate_inputs(args)
    if args.search:
        report_query(checked_args, args)
        return
    export_possessions_to_file(checked_args, args)


def validate_inputs(args, **kwargs):
    """Validates the (critical) application arguments.
    
    WoW path information is obtained from and saved to configuration file.
    The presence of correctly named addon data files at the WoW path is checked.
    
    Args:
        args (:obj:`argparse.Namespace`): program arguments.

    Returns:
        :obj:`commandline.CheckedArgs`: namedtuple of validated program 
            arguments.
    """
    config = Config()
    checked_args = commandline.check_args(args, config, **kwargs)
    if not possessions.check_possessions(checked_args.wowpath):
        print(_(
            "Check you have given the correct WoW folder "
            "path and it contains 'Possessions.lua' files under the 'WTF' "
            "tree. If you already have the Possessions addon installed, you "
            "may need to log into WoW and open your mail and bank to get all "
            "data for each character."))
        raise SystemExit(_('Error: no data found.'))
    config.data['wowpath'] = checked_args.wowpath
    try:
        config.save()
    except OSError as e:
        log = get_log('ledger')
        log.warning('Unable to save configuration: %s' % e)
    return checked_args


def report_query(checked_args, args):
    """Reports the results from search mode to console.
    
    Args:
        checked_args (:obj:`commandline.CheckedArgs`): namedtuple of validated 
            program arguments.
        args (:obj:`argparse.Namespace`): program arguments.
    """
    with sys.stdout as output_file:
        data = gen_possessions_data(checked_args, args)
        view = dataview.create_view(data, args)
        results = dataview.search(view, args.search)
        csv_output(output_file, view.header, results, checked_args, args)


def export_possessions_to_file(checked_args, args):
    """Exports item data to an output file.
    
    Note:
        Any existing output file with the same name is overwritten in effect.
    
    Args:
        checked_args (:obj:`commandline.CheckedArgs`): namedtuple of validated 
            program arguments.
        args (:obj:`argparse.Namespace`): program arguments.
    """
    output = checked_args.output
    if output != '-':
        _file.remove_file_silent(output)
    if checked_args.format == 'excel':
        excel_output(output, checked_args, args)
    else:
        with _file.unixoutput(
                output, mode='at', encoding='utf_8', newline='') as output_file:
            data = gen_possessions_data(checked_args, args)
            view = dataview.create_view(data, args)
            csv_output(output_file, view.header, view, checked_args, args)


def gen_possessions_data(checked_args, args):
    """Yields item data from specific addon data files in a WoW path.
    
    For the Possessions addon data, the account name is obtained from the 
    path itself of the data file, then added back into the item data structure.
    
    Args:
        checked_args (:obj:`commandline.CheckedArgs`): namedtuple of validated 
            program arguments.
        args (:obj:`argparse.Namespace`): program arguments.
        
    Yields:
        :obj:`account.AccountItemRecord`: raw item data plus account name as 
            namedtuple.
    """
    log = get_log('ledger')
    log.info('Reading data files:')
    for filepath in possessions.find_possessions(checked_args.wowpath):
        account_name = _path.splitall(filepath)[-3]
        data = possessions.read(filepath)
        vprint(args, filepath)
        log.info('* %s' % filepath)
        for row in data:
            yield account.AccountItemRecord(*chain([account_name], row))


def excel_output(output, checked_args, args):
    """Outputs item data to Excel.
    
    Since the Excel output format supports multiple data sheets, the output
    contains all the supported data views for convenient access to all data.
    
    In addition, basic attempts have been made to format the data for end-user 
    friendly access while not inconveniencing further data processing within
    Excel.
    
    Args:
        output (str): output file name.
        checked_args (:obj:`commandline.CheckedArgs`): namedtuple of validated 
            program arguments.
        args (:obj:`argparse.Namespace`): program arguments.
    """
    # Cache data to create multiple views
    data = list(gen_possessions_data(checked_args, args))
    workbook = xlsxwriter.Workbook(output)
    # Formats used throughout Excel workbook need to be pre-created
    # - attempts to replicate the built-in 'Heading 1' style as a format object
    title_format = workbook.add_format(
        {
            'bold': True, 'font_name': 'Calibri', 'font_color': '#003366',
            'font_size': 15, 'bottom': 5, 'bottom_color': '333399',
        })
    header_format_left = workbook.add_format(
        {
            'bold': True, 'font_name': 'Calibri', 'font_color': '#FFFFFF',
            'bg_color': '#0066CC', 'left': 4, 'align': 'left',
        })
    header_format_right = workbook.add_format(
        {
            'bold': True, 'font_name': 'Calibri', 'font_color': '#FFFFFF',
            'bg_color': '#0066CC', 'left': 4, 'align': 'right',
        })
    body_format = workbook.add_format({'font_name': 'Calibri', 'left': 4})
    body_format_gold = workbook.add_format(
        {'font_name': 'Calibri', 'left': 4, 'num_format': '#,##0.0000'})
    # Worksheet tab colors
    tab_colors = {
        'factiongold': '#FF0000',
        'gold': '#FFCC00', 
        'item': '#00FF00', 
        'character': '#99CCFF', 
        'location': '#3366FF', 
        'mail': '#C0C0C0',
        'worn': '#800080', 
        'raw': '#000000',
    }
    # Create a sheet per dataview
    for view_name in _console.progress_bar(EXCEL_TABS, disable=args.quiet):
        view = dataview.create_view(data, args, view_name)
        worksheet = workbook.add_worksheet(_(view_name))  # Translate sheet name
        worksheet.set_tab_color(tab_colors[view_name])
        worksheet.hide_gridlines(2)
        # Create a title with formatting based on sheet settings
        sheet_settings = EXCEL_SHEETS[view_name]
        title = sheet_settings.title
        worksheet.write(0, 0, title, title_format)
        # - formatting blank cells requires writing blank cells with a format
        for title_col_index in range(1, sheet_settings.title_cols):
            worksheet.write_blank(0, title_col_index, None, title_format)
        # Position around row and column offsets to give flexibility of 
        # placement of the content
        row_offset = 2
        col_offset = 0
        # "Freeze panes" enables scrolling while headers remain visible
        # Positioned on first item of leftmost data
        worksheet.freeze_panes(row_offset + 1, col_offset)
        # Track headers in format sets to align headers and format appropriately
        numerical_indices = set()
        gold_indices = set()
        # Track the maximum width of data in a column to resize the column width
        max_column_widths = []
        for header_index, header_name in enumerate(view.header):
            header_col_index = header_index + col_offset
            header_format = header_format_left
            if header_name in dataview.PRESENTATION_FORMATS['numerical']:
                numerical_indices.add(header_index)
                header_format = header_format_right
            if header_name in dataview.PRESENTATION_FORMATS['gold']:
                gold_indices.add(header_index)
                header_format = header_format_right
            worksheet.write(
                row_offset, header_col_index, _(header_name), header_format)
            max_column_widths.append(len(header_name))
        # Headers complete, now output body of data on following rows
        row_offset += 1
        for row_index, row_data in enumerate(view.data):
            body_row_index = row_index + row_offset
            for col_index, item in enumerate(row_data):
                body_col_index = col_index + col_offset
                value = item
                # Non-gold data
                if col_index not in gold_indices:
                    if col_index not in numerical_indices:
                        worksheet.write(
                            body_row_index, body_col_index, value, body_format)
                    else:
                        value = int(value)
                        worksheet.write_number(
                            body_row_index, body_col_index, value, body_format)                    
                # Gold data
                else:
                    if not args.gold_format:
                        # Default gold format is as a decimal
                        value = _warcraft.decimal_gold(value)
                        worksheet.write_number(
                            body_row_index, body_col_index, value, 
                            body_format_gold)
                    else:
                        # ... unless a user requests a specific gold format
                        value = _warcraft.format_gold(
                            value, format=args.gold_format)
                        worksheet.write(
                            body_row_index, body_col_index, value, body_format)
                # Track maximum content length within columns
                max_column_widths[col_index] = max(
                    max_column_widths[col_index], len(str(value)))
        # Adjust column widths based on maximum content length.
        # The adjustment is an estimate due to Microsoft Excel rendering.
        # Source: https://xlsxwriter.readthedocs.io/worksheet.html
        for col_index, width in enumerate(max_column_widths):
            body_col_index = col_index + col_offset
            new_width = max(8.43, width) * 1.1  # Magic numbers for Calibri font
            worksheet.set_column(body_col_index, body_col_index, new_width)
    # 'About' sheet
    worksheet = workbook.add_worksheet(_('about'))
    worksheet.hide_gridlines(2)
    #   0. Don’t hide gridlines.
    #   1. Hide printed gridlines only.
    #   2. Hide screen and printed gridlines.
    # Date-time in ISO8601 format excluding microsecond component
    current_datetime = datetime.now().replace(microsecond=0).isoformat()
    about_data = [
        (_('Application'), 'Family Ledger'),
        (_('Version'), version.__version__),
        (_('Author'), 'fondlez "Anuber"-Kronos, fondlez at protonmail.com'),
        (_('Source'), 'http://github.com/anuber-Kronos/familyledger'),
        (_('Credits'), 
            'Possessions addon (https://github.com/Road-block/Possessions)'),
        ('', 'slpp module (https://github.com/SirAnthony/slpp)'),
        ('', 'remi (https://github.com/dddomodossola/remi)'),
        ('', 'xlsxwriter (https://github.com/jmcnamara/XlsxWriter)'),
        ('', 'Kronos Private Vanilla World of Warcraft Project '
            '(https://www.kronos-wow.com/)'),
        (_('Generated'), current_datetime),
    ]
    # Adds a title to this sheet
    sheet_settings = EXCEL_SHEETS['about']
    title = sheet_settings.title
    worksheet.write(0, 0, title, title_format)
    # - formatting blank cells requires writing blank cells with a format
    for title_col_index in range(1, sheet_settings.title_cols):
        worksheet.write_blank(0, title_col_index, None, title_format)
    # Offsets for content placement flexibility
    row_offset = 2
    col_offset = 0
    # Only two columns as key-value pairs required here
    label_col_index = col_offset
    value_col_index = label_col_index + 1
    for row_index, row_data in enumerate(about_data):
        body_row_index = row_index + row_offset
        label = row_data[label_col_index]
        value = row_data[value_col_index]
        worksheet.write(
            body_row_index, label_col_index, label, header_format_left)
        worksheet.write(
            body_row_index, value_col_index, value, body_format)
    # Adjust column widths to maximum length of content in columns.  
    # Since the data is static, the values are pulled manually from Excel.
    worksheet.set_column(label_col_index, label_col_index, 10.43)
    worksheet.set_column(value_col_index, value_col_index, 25.14)
    workbook.close()


def csv_output(output_file, header, row_data, checked_args, args):
    """Outputs item data in a CSV format to file or console.
    
    Reformatting is carried out for columns containing gold values before 
    output, if the data is not from a 'raw' view.
    
    Args:
        output_file (io.IOBase): output file.
        header (tuple): header fields.
        row_data: iterable containing tuples.
        checked_args (:obj:`commandline.CheckedArgs`): namedtuple of validated 
            program arguments.
        args (:obj:`argparse.Namespace`): program arguments.
    """
    csv_dialect = FORMAT_TO_DIALECT[checked_args.format]
    f_csv = csv.writer(output_file, dialect=csv_dialect)
    f_csv.writerow(list(map(_, header)))  # Translate header through gettext
    gold_indices = [
        index for index, name in enumerate(header) 
        if name in dataview.PRESENTATION_FORMATS['gold']
    ]
    if not gold_indices or args.view == 'raw':
        f_csv.writerows(row_data)
    else:
        for row in row_data:
            format_row = list(row)
            for gold_index in gold_indices:
                gold_value = format_row[gold_index]
                console_mode = args.output == '-' or args.search
                if not args.gold_format and not console_mode:
                    # Structured output like data files by default prefers
                    # data like gold as a number/decimal to further process.
                    format_row[gold_index] = _warcraft.decimal_gold(
                        gold_value)
                else:
                    # Unstructured output, like the console by default prefers
                    # user-friendly final output like gold as shown in-game.
                    format_row[gold_index] = _warcraft.format_gold(
                        gold_value, format=args.gold_format)
            f_csv.writerow(format_row)


def user_lang(lang=None):
    """Sets and returns a language code. Default: 'en'."""
    return _iterable.first_true((lang, locale.getdefaultlocale()), 'en')


def vprint(args, text):
    """Helper function for verbose printing to console."""
    if args.verbose:
        print(text)


if __name__ == '__main__':
    setup()
