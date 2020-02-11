#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Shortwave listening (SWLING) reporting tool.

Simple menu interface to view reports built using the
data that is saved to a CSV file while using the
swlookup application.

Optional arguments:
    -h, --help     Show this help screen and exit.
    -v, --version  Show program version.

"""

# standard library modules
import sys
import os
import re
import argparse
import random

# local modules
from swtools.constants import FORMATTERS, SWLING, SWLING_LOGO
from swtools.functions import generate_argparser, program_version
from swtools.reports import Report


def main():
    """Main entry point of the application."""

    # generate an argument parser
    arg_parser = generate_argparser(SWLING)
    args = arg_parser.parse_args()

    # if the namespace help attribute exists, then
    # show help (the module doctring) and quit
    if hasattr(args, 'help'):
        print(__doc__)
        sys.exit(0)

    # print a pretty heading
    bad_colors = ['black', 'white', 'darkgrey', 'red', 'bold', 'underline', 'italic' 'reset']
    colors = [FORMATTERS[color] for color in FORMATTERS if color not in bad_colors]
    colored_lines = [random.choice(colors) + line for line in SWLING_LOGO.split('\n')]
    print('\n'.join(colored_lines), '\033[0m')

    # before we go any further, let's make sure the CSV data file is available
    f = os.path.join(os.path.dirname(__file__), 'data/swling.csv')
    if not os.path.exists(f):
        print(' The shortwave listening CSV file is not available. This could be\n'
              ' because no session data has been saved yet, or that the file has\n'
              ' been removed or deleted. Please save some session data first and\n'
              ' try again.\n'.format(**FORMATTERS))
        sys.exit(0)

    # the report choices are stored in a dictionary with the report key selection,
    # the report name and the report method to call after the class instantiation
    reports = {
        'A': ['Stations Summary Report', 'report_stations'],
        'B': ['Transmitters Summmary Report', 'report_transmitters'],
        'C': ['Frequencies Summary Report', 'report_frequencies'],
        'D': ['Frequency History', 'report_frequency_history'],
        'Q': ['Quit', '']
    }

    # create a simple menu to prompt the user for a report selection
    option = menu(reports)

    # because some reports require a parameter, we need to check if
    # the selected report option requires a prompt for data
    if option == 'D':
        param = input("\n {bold}[{yellow}?{lightgrey}]{reset} Frequency: ".format(**FORMATTERS))
    else:
        param = None

    # run the report by instantiating the report class and calling
    # the selected report method with any required parameters
    # errors in the class should bubble up here via __exit__
    try:
        with Report(f) as rpt:
            rpt.main(reports[option][1], param)
    except Exception as error:
        print('\n An error occured:', error, '\n')
        sys.exit(1)


def menu(reports):
    """Create the report selection menu.

    :param reports: A dictionary with the report choices.
    :type reports: dict
    """

    # print quick usage help
    print(' {italic}Please select a report from the list below.\n'
          ' You will prompted for parameters if required.{reset}\n'.format(**FORMATTERS))

    # loop the reports dictionary and print the report options and names
    for key in reports:
        menu_item = ' {bold}[{yellow}' + key + '{lightgrey}]{reset} '
        print(menu_item.format(**FORMATTERS) + str(reports[key][0]))

    # prompt the user, wait for an answer, and validate it
    # quit immediately if the user selects the quit option
    while True:
        try:
            choice = input("\n {bold}[{yellow}?{lightgrey}]{reset} ".format(**FORMATTERS))
            if choice in ['q', 'Q']:
                print('\n Quitting... bye!\n')
                sys.exit(0)
            is_valid = choice.upper() in reports.keys()
            if not is_valid:
                raise ValueError
        except ValueError:
            print('\n Please select a valid option: ' + str(list(reports.keys())))
            continue
        else:
            break

    # return the user's choice of report
    return choice.upper()


if __name__ == '__main__':
    main()
