#!/usr/bin/python3
"""
The driving module for the web version of Family Ledger.

Copyright (C) 2020, fondlez "Anuber"-Kronos, fondlez at protonmail.com
"""
import gettext
import html
import logging
import operator
import os
import re
import sys
from functools import partial

import remi.gui as gui
from remi import App
from remi import start

from familyledger import commandline
from familyledger import dataview
from familyledger import ledger
from familyledger.utils import _console
from familyledger.utils._exception import set_exception_handler
from familyledger.utils import _path
from familyledger.utils import _logging
from familyledger.utils._logging import get_log
from familyledger.utils import _timer
from familyledger.utils import _warcraft


class LedgerWeb(App):
    """Main appplication class."""
    def __init__(self, *pargs, **kwargs):
        """Initializes GUI server parent class."""
        self._log = get_log('ledger.web')
        super().__init__(*pargs, **kwargs)

    def main(self, *pargs, **kwargs):
        # Re-enables logging and names a new log.
        """Sets up the core widgets of the graphical user interface."""
        # Check input arguments supplied
        if (pargs and len(pargs) > 1):
            self._args, self._checked_args, *__ = pargs
        else:
            self._log.error('No input arguments found')
            return

        # Create "master" container which will hold top container and bottom 
        # container. Add widgets to it vertically
        self.main_container = gui.Container(margin='10px')
        self.main_container.set_style({'border': '1px solid white'})
        self.main_container.set_layout_orientation(
            gui.Container.LAYOUT_VERTICAL)

        # Create top container then add widgets to it horizontally
        self.top_container = gui.Container(margin='0px auto', height=50)
        self.top_container.set_style({'border': '1px solid white'})
        self.top_container.set_layout_orientation(
            gui.Container.LAYOUT_HORIZONTAL)
            
        # Create middle container then add widgets to it horizontally
        self.middle_container = gui.Container(margin='0px auto', height=50)
        self.middle_container.set_style({'border': '1px solid white'})
        self.middle_container.set_layout_orientation(
            gui.Container.LAYOUT_HORIZONTAL)

        # Create bottom container then add widgets to it horizontally
        self.bottom_container = gui.Container(margin='0px auto 0px auto')
        self.bottom_container.set_style({'border': '1px solid white'})
        self.bottom_container.set_layout_orientation(
            gui.Container.LAYOUT_HORIZONTAL)

        # Create widgets that will be placed in the top container
        # - label for view dropdown
        self.label_view = gui.Label(
            _('View:'), 
            width='10%', height=30, margin='10px',
            style={
                'text-align': 'right',
                'font-size': '16px',
                'font-weight': 'bold',
            })
        # - dropdown of views
        drop_view_list = list(dataview.DATAVIEWS)
        # -- the default view is assumed to be the first from the list if not  
        #    provided by the user
        drop_view_default = self._args.view or dataview.DATAVIEWS[0]
        self.drop_view = gui.DropDown.new_from_list(
            drop_view_list,
            width='16%', height=32, margin='10px 10px 10px 10px')
        self.drop_view.set_style({
            'text-align': 'center', 'font-weight': 'bold'})
        self.drop_view.select_by_value(drop_view_default)
        self.drop_view.onchange.do(self.on_view_changed)
        # - label for search box
        self.label_start = gui.Label(
            _('Start search:'), 
            width='16%', height=30, margin='10px',
            style={
                'text-align': 'right',
                'font-size': '16px',
                'font-weight': 'bold',
            })
        # - search box
        self.text_search = gui.TextInput(width='10%', height=30, margin='10px')
        self.text_search.set_style({'line-height': '30px'})
        # - search box 'Search' button
        self.button_search = gui.Button(
            _('Search'), width='10%', height=30, margin='10px')
        self.button_search.set_style({'background-color': '#0066CC'})
        self.button_search.onclick.do(self.on_search_pressed)
        # - 'Refresh' button
        self.button_refresh = gui.Button(
            _('Refresh'), width='10%', height=30, margin='10px')
        self.button_refresh.set_style({'background-color': '#0066CC'})
        self.button_refresh.onclick.do(self.on_refresh_pressed)
        # - 'Close' button
        self.button_close = gui.Button(
            _('Close'), width='10%', height=30, margin='10px')
        self.button_close.set_style({'background-color': '#0066CC'})
        self.button_close.onclick.do(self.on_close_pressed)

        # Add those widgets to the top container
        self.top_container.append((
            self.label_view, self.drop_view, self.label_start, self.text_search,
            self.button_search, self.button_refresh, self.button_close))
            
        # Create widgets that will be placed in the middle container
        # - label for results count
        self.label_results = gui.Label(
            '',
            width='100%', height=30, margin='10px',
            style={
                'text-align': 'left',
                'font-size': '16px',
            })
            
        # Add those widgets to the middle container
        self.middle_container.append((self.label_results))
            
        # Add the top and middle container to the master container
        self.main_container.append((self.top_container, self.middle_container))
        
        # At startup, set textinput widget as ready to accept input
        self.text_search.attributes['tabindex'] = '1'
        self.text_search.attributes['autofocus'] = 'autofocus'
        self.text_search.onkeydown.do(self.on_enter_key)

        return self.main_container

    def on_view_changed(self, widget, value):
        """Runs when a user changes the dropdown list value to select a View."""
        if not hasattr(self, 'view'):
            self.data_refresh()
        self.view_refresh(self.view_from_dropdown(value))
        self.display_data()

    def on_refresh_pressed(self, widget):
        """Runs when a user clicks on the 'Refresh' button."""
        # Reset the search textinput box
        self.text_search.set_value('')
        # Reset the sorted status
        self.already_sorted = None
        # (Re-)Fetch the data, create a view based on the GUI and display it
        self.data_refresh()
        view_name = self.view_from_dropdown(self.drop_view.get_value())
        self.view_refresh(view_name)
        self.display_data()

    def on_search_pressed(self, widget):
        """Runs when a user clicks on the 'Search' button."""
        # Fetches initial data only
        if not hasattr(self, 'view'):
            self.data_refresh()
            view_name = self.view_from_dropdown(self.drop_view.get_value())
            self.view_refresh(view_name)
        self.display_data()

    def data_refresh(self):
        """Helper function: (re-)fetches data."""
        # Fetch the raw data
        self.vprint(_('Fetching data ...'))
        data = ledger.gen_possessions_data(self._checked_args, self._args)
        if data is None:
            self._log.error('No data found.')
            return
        # Ensure the data is a not an iterator to enable multiple searches
        if not isinstance(data, list):
            self.data = list(data)
        self.vprint(_('* Found %d data items.') % len(self.data))

    def view_refresh(self, view_name):
        """Helper function: creates a view from the fetched data."""
        self.vprint(_('Creating view "%s" ...') % view_name)
        view = dataview.create_view(self.data, self._args, view_name)
        if view is None:
            self._log.error('No view found.')
            return
        self.header = view.header
        # Check that the user did not request the raw data which is already
        # cached
        if self.data is not view.data:
            # Ensure the view's data is a not an iterator to enable 
            # multiple searches
            if not isinstance(view.data, list):
                self.view = list(view.data)
            else:
                self.view = view.data
        else:
            # Requesting a 'raw' view is the same as the original data.
            self.view = self.data
        # Reset the sorted status
        self.already_sorted = None
        self.vprint(_('* Found %d view entries.') % len(self.view))

    def display_data(self):
        """Helper function: displays tabular data."""
        # Create the table widget if it does not exist, otherwise remove
        # all its children
        if hasattr(self, 'table') and self.table is not None:
            self.table.empty()
        else:
            self.table = gui.Table(margin='0px auto 0px auto')
            
        # Register interest for table row clicks (to sort by clicking on header)
        self.table.on_table_row_click.do(self.on_table_row_click)
        
        # Generate the table row containing the table header names
        row = gui.TableRow()
        row.attributes['id'] = 'data_header'
        numerical_indices = set()
        gold_indices = set()
        url_indices = set()
        for header_index, header_item in enumerate(self.header):
            # Track any numerical columns so they can be formatted
            if header_item in dataview.PRESENTATION_FORMATS['numerical']:
                numerical_indices.add(header_index)
            # Track any gold value columns so they can be formatted
            if header_item in dataview.PRESENTATION_FORMATS['gold']:
                gold_indices.add(header_index)
            if header_item in dataview.PRESENTATION_FORMATS['url']:
                url_indices.add(header_index)
            table_item = gui.TableItem(
                _(str(header_item)), 
                style={
                    'background-color': '#a4c2f5',
                    'font': 'Courier New',
                    'font-size': '20px',
                })
            table_item.set_identifier(header_item)
            row.append(table_item)

        # Add the header row to the table
        self.table.append(row)

        # Check if the user searched for something and search the data
        search_string = self.text_search.get_value()
        if search_string:
            # Escape potentially user interface breaking characters
            search_string = html.escape(search_string, quote=True)
            self.vprint(_('* searching "%s" ...') % search_string)
            search_data = self.search(search_string)
        else:
            search_data = self.view

        # Generate rows that will contain the table data
        results_count = 0
        timer = _timer.Timer()
        timer.start()
        for row_index, row_data in enumerate(
                _console.progress_bar(search_data, disable=self._args.quiet)):
            results_count += 1
            row = gui.TableRow()
            for col_index, row_item in enumerate(row_data):
                str_row_item = str(row_item)
                if col_index not in url_indices or not detect_url(str_row_item):
                    # Format gold values
                    if col_index in gold_indices:
                        str_row_item = _warcraft.format_gold(
                            row_item, format=self._args.gold_format)
                    table_item = gui.TableItem(str_row_item)
                    # Format numerical values
                    if col_index in numerical_indices:
                        table_item.set_style({'text-align': 'right'})
                else:
                    # Track any URLs so they can be formatted as Link objects
                    table_item = gui.TableItem()
                    table_item.append(gui.Link(str_row_item, str_row_item))
                # Alternate row background color to improve row identification
                if row_index % 2 == 0:
                    table_item.set_style({'background-color': '#ffd'})
                row.append(table_item)
            # Add the data row to the table
            self.table.append(row)

        self.vprint(_('** data table complete. Rendering ...'))
        if results_count > 0:
            # Add the table widget to the bottom container
            self.bottom_container.append(self.table)
            # Add the bottom container to the master container
            self.main_container.append(self.bottom_container)
        else:
            self.table.empty()
        self.vprint(_('** rendering complete.'))
        timer.stop()
        
        # Updating results count
        self.label_results.set_text(
            _('{} results ({:.0f} seconds)').format(
                results_count, timer.elapsed))

    def search(self, pattern):
        """Searches view data for a pattern, returning matched rows.
        
        The search for the pattern is case-insensitive.
        
        Args:
            pattern (str): string containing a regular expression.
        
        Yield:
            iterable: matching row from iterable view data.
        """
        for row in self.view:
            for item in row:
                if re.search(pattern, str(item), re.IGNORECASE):
                    yield row
                    break

    def on_table_row_click(self, table, row, item):
        """Runs when the user mouse clicks on a table row."""
        if (row.identifier == 'data_header'):
            # Prepares to sort based on the clicked header row and id (name).
            header_id = item.identifier
            self.vprint(
                _('Clicked on a header: %s. Sorting ...') % item.get_text())
            self.sort(header_id)
            self.already_sorted = header_id
            self.display_data()

    def sort(self, field):
        """Sorts nested attributed data by attribute name.
        
        Args:
            field (str): attribute name.
        """
        if not field:
            return
        if hasattr(self, 'already_sorted') and self.already_sorted == field:
            # Reverses the sort if the data is already sorted by this field.
            self.view.reverse()
        else:
            # Sorts by field in reverse order.
            self.view.sort(key=operator.attrgetter(field), reverse=True)

    def on_enter_key(self, new_value, old_value, keycode):
        """Runs when the user clicks Enter in the text input box.
        
        If an Enter keycode is detected, the search text box 'onchange' event 
        is activated and the search button pressed action is emulated.
        """
        if keycode in ('13', '10'):  # 13 == ord('\r'), 10 == ord('\n')
            self.text_search.onchange(old_value)
            self.on_search_pressed(self.button_search)

    def on_close_pressed(self, widget):
        """Runs when the user clicks on the Close button."""
        self.vprint(_('Shutting down.'))
        self.close()

    def view_from_dropdown(self, value):
        """Maps the View dropdown item text to a valid view name."""
        # Escape potentially user interface breaking characters
        value = html.escape(value, quote=True)
        if value and value in dataview.DATAVIEWS:
            return value
        self._log.error('Invalid View dropdown value: %s' % value)

    def vprint(self, text):
        """Helper function for verbose printing to console."""
        if self._args.verbose:
            print(text)


def detect_url(link):
    """Returns whether input text starts with a simple and common URL type.
    
    Args:
        link (str): potential URL.

    Returns:
        bool: True if URL detected, False otherwise.
    """
    if link and link.startswith(('https:', 'http:')):
        return True
    return False


def setup():
    """Sets up the debugging context for the main application.
    
    Args:
        args (:obj:`argparse.Namespace`): program arguments.
    """
    # Disables traceback output by default to be end user friendly
    sys.excepthook = partial(set_exception_handler, debug_flag=False)
    args = commandline.options(gui=True).parse_args()
    # - unless the user states they want to see it.
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
            log = get_log('ledger_web')
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
        'ledger_web', localedir=mo_path, languages=ledger.user_lang(args.lang), 
        fallback=True)
    global _
    _ = translate.gettext


def main(args):
    """Starts the main application.
    
    Args:
        args (:obj:`argparse.Namespace`): program arguments.
    """
    # Use ths same types of critical inputs and validation as the Ledger 
    # program.
    checked_args = ledger.validate_inputs(args, gui=True)
    # Start the graphical user interface.
    start(
        LedgerWeb, title=_('Family Ledger - Ledger Web'), standalone=False, 
        userdata=(args, checked_args))


if __name__ == '__main__':
    setup()
