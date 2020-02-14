"""
A module for parsing command line application arguments.

Copyright (C) 2020, fondlez "Anuber"-Kronos, fondlez at protonmail.com
"""
import argparse
import os
from collections import namedtuple
from tkinter import filedialog
from tkinter import Tk

from . import dataview
from . utils._i18n import n_
from . import version


FORMAT_EXTENSION = {
    'csv': '.csv',
    'excel': '.xlsx',
    'tsv': '.tsv',
    'unix': '.csv',
}
"""Mapping from output format type to filename extension."""

EXPORT_FORMATS = ('csv', 'excel', 'tsv', 'unix')
"""Available formats for export to file."""

CONSOLE_FORMATS = ('csv', 'tsv', 'unix')
"""Available formats for display on console."""


CheckedArgs = namedtuple('CheckedArgs', ['wowpath', 'format', 'output'])
"""Critical application arguments."""


def options(gui=None):
    """Defines arguments for a command line parser.
    
    Args:
        gui (bool): flag indicating re-use of command line arguments in 
            graphical user interface programs.
    
    Returns:
        :obj:`argparse.ArgumentParser`: commandline argument parser.
    """
    parser = argparse.ArgumentParser(
        description='List possessions stored on accounts in '
        'a World of Warcaft vanilla 1.12 folder. '
        'This program currently requires the Possessions addon '
        'to be installed in World of Warcraft.',
        epilog='')
    parser.add_argument(
        '-V', '--version', action='version',
        version='%(prog)s {}'.format(version.__version__))
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('-q', '--quiet', action='store_true')
    parser.add_argument(
        '--log-level', 
        choices=['debug', 'info', 'warning', 'error', 'critical'], 
        default='warning',
        help='level of logging (default: warning)')
    parser.add_argument(
        '--log-disable', action='store_true',
        help='disable logging to file')
    parser.add_argument(
        '--lang', help='language (default: en)')
    parser.add_argument(
        '--db', choices=['twinhead', 'wowhead', 'classicdb', 'id'],
        default='twinhead',
        help='item link database (default: twinhead)')
    parser.add_argument(
        '--include-mail', type=check_bool, default='false',
        help='include items in mail for views with location ambiguity')
    parser.add_argument(
        '--gold-format', help='output format for gold '
        '(default:"{gold}g {silver:02d}s {copper:02d}c")')
    parser.add_argument(
        '--view', choices=dataview.DATAVIEWS, type=check_view, 
        help='view of the data (default: "character" for non-excel)')
    if not gui:
        parser.add_argument(
            '-f', '--format', choices=EXPORT_FORMATS,
            help='output file format (default: excel)')
        parser.add_argument(
            '-o', '--output', 
            help='output file (default: output.tsv, "-" is console)')
        parser.add_argument(
            '-s', '--search', 
            help='search for string, results always in console')
    parser.add_argument(
        'wowpath', metavar='folder', nargs='?',
        help='World of Warcraft folder path')
    return parser


def check_bool(bool_str):
    """Checks for the presence of a valid boolean from a string.
    
    Note:
        Utility intended for use in type validation within arguments of
        :obj:`argparse.ArgumentParser`.
    
    Args:
        bool_str (str): string representing a boolean (case-insensitive).

    Returns:
        bool: boolean value.
        
    Raises:
        :obj:`argparse.ArgumentTypeError`: if input does not represent boolean.
    """
    boolean = {'true': True, 'false': False}
    value = boolean.get(bool_str.lower(), None)
    if value is None:
        msg = '%r is not boolean' % bool_str
        raise argparse.ArgumentTypeError(msg)
    return value


def check_view(choice):
    """Checks for a valid dataview selection that begins with a substring.
    
    This function will return the input unchanged for an invalid choice to 
    allow further validation.
    
    Note:
        Utility intended for use in type validation of string choices within 
        arguments of :obj:`argparse.ArgumentParser`.
    
    Args:
        choice (str): input text.
        
    Returns:
        str: dataview name or input text.
    """
    selection = [name for name in dataview.DATAVIEWS if name.startswith(choice)]
    if len(selection) == 1:
        return selection[0]
    return choice


def check_args(args, config, **kwargs):
    """Checks command line arguments and returns a tuple of validated arguments.
    
    Args:
        args (:obj:`argparse.Namespace`): program arguments.

    Returns:
        :obj:`CheckedArgs`: namedtuple of validated program arguments.
    """
    gui = kwargs.pop('gui', None)
    output = None
    output_format = None
    saved_wowpath = config.data.get('wowpath', None)
    if not gui:
        output_format = check_output_format(
            args.output, args.format, args.search)
        output = check_output(args.output, output_format)
    checked_args = CheckedArgs(
        check_wowpath(args.wowpath, saved_wowpath), output_format, output)
    return checked_args


def check_output_format(output_file, requested_format, search_mode):
    """Checks and returns the output format selected by the user.
    
    If the output is to the console, either due to the output file being '-'
    or search mode is selected, then only a subset of formats are available
    (text only).
    
    Args:
        output_file (str): output filename.
        requested_format (str): user format selection.
        search_mode (bool): flag for whether in search mode.
        
    Returns:
        str: output format.
    """
    default_format = 'tsv'
    # Check not in console mode => export mode
    if output_file != '-' and not search_mode:
        default_format = 'excel'
        if requested_format in EXPORT_FORMATS:
            return requested_format
    # Check for valid console format
    elif requested_format in CONSOLE_FORMATS:
        return requested_format
    return default_format


def check_output(output_file, output_format):
    """Checks and returns the output filename.
    
    If no output filename is selected, a default is provided with a file
    extension corresponding to the selected format.
    
    Args:
        output_file (str): output filename.
        output_format (str): output format.
        
    Returns:
        str: output filename.
    """
    if output_file is None:
        output_file = 'output' + FORMAT_EXTENSION[output_format]
    return output_file


def check_wowpath(wowpath, saved_wowpath=None):
    """Checks and returns the path to the World of Warcraft directory.
    
    If no path is provided or the path does not exist, a graphical request
    is made with the initial directory defaulting to any previously saved
    path.
    """
    if wowpath is None or not os.path.exists(wowpath):
        # Graphical request for correct folder
        Tk().withdraw()
        wowpath = filedialog.askdirectory(
            title=n_('World of Warcraft folder'), initialdir=saved_wowpath)
        if not wowpath:
            raise SystemExit(n_('Error: no World of Warcraft folder given'))
    return wowpath
