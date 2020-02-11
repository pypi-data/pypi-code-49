#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A simple interface for command line input handling.

A simple class that encapsulates all application command line
prompts following a consistent format. Prompts the user for
input, validates, and returns the values. Methods automatically
handle the global 'Q' quit key.

Examples
--------
.. code-block:: python
    :caption: Create an instance using a context manager (recommended)

    with Prompter() as prompt:
        my_data = prompt.get_input(<validator>, True)
        confirm = prompt.confirm(<validator>)
        ...

.. code-block:: python
    :caption: Create an instance directly

    prompt = Prompter()
    my_data = prompt.get_input(<validator>, True)
    confirm = prompt.confirm(<validator>)
    ...

"""

# standard library modules
import sys
import datetime
import re


class Prompter():
    """A simple interface for command line input handling."""

    def __init__(self):
        """Initialize a Prompter object and it's properties."""
        # A dictionary with ANSI escape codes used in format substitutions.
        # The ** prefix operator is used to unpack the dictionary into
        # keyword arguments for the format function.
        self.FORMATTERS = {
            'red': '\033[31m',
            'purple': '\033[35m',
            'lightgrey': '\033[37m',
            'lightred': '\033[91m',
            'yellow': '\033[93m',
            'pink': '\033[95m',
            'reset': "\033[0m",
            'bold': '\033[1m',
            'italic': '\033[3m',
            'underline': '\033[4m'
        }

        # A dictionary with specifically formatted strings used throughout this class.
        self.STRINGS = {
            'prompt_msg': ' {bold}[{yellow}?{lightgrey}]{reset} ',
            'error_msg': ' {bold}[{pink}X{lightgrey}]{reset} Invalid input ................... : ',
            'quit_msg': '\n Quitting... bye!\n'
        }

        # A dictionary with the individual validators that can be used for input prompts.
        # Each validator is a list with the following values:
        #   1. Validation type (regex, values, datetime)
        #   2. The validation test (regex expression, list of values, format, etc)
        #   3. A custom prompt for the input function
        #   4. A custom error message
        self.VALIDATORS = {
            'frequency': [
                'regex',
                r'^(?=.)([+-]?([0-9]*)(\.([0-9]+))?)$',
                'Frequency in kHz........(required): ',
                'Value must be a number'
            ],
            'utc': [
                'regex',
                '^(0[0-9]|1[0-9]|2[0-3])[0-5][0-9]$',
                'Universal Time..........(optional): ',
                'Requires a 4 digit value between 0000 and 2359'
            ],
            'dbu': [
                'regex',
                r'^\d+?$',
                'Signal in dBu...........(required): ',
                'Value must be a one or two digit integer'
            ],
            'key': [
                'regex',
                '^[0-9]+$',
                'Database Key............(required): ',
                'Value must be an integer'
            ],
            'local': [
                'datetime',
                '%H:%M',
                'Local Time [HH:MM]......(optional): ',
                ''
            ],
            'save': [
                'values',
                ['y', 'Y', 'n', 'N'],
                'Save SWLing Session..........(Y/N): ',
                'Value must be [Y]es or [N]o'
            ],
            'history': [
                'values',
                ['y', 'Y', 'n', 'N'],
                'View SWLing History..........(Y/N): ',
                'Value must be [Y]es or [N]o'
            ]
        }

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def get_input(self, validator, required):
        """Prompt for input, validate, and return value.

        :param validator: A dictionary key representing a built-in validation method.
        :type validator: string
        :param required: Indicates if input is required or can be empty.
        :type required: bool
        """
        while True:
            try:
                prompt = self.STRINGS['prompt_msg'] + self.VALIDATORS[validator][2]
                input_value = input(prompt.format(**self.FORMATTERS))
                if input_value in ['q', 'Q']:
                    print(self.STRINGS['quit_msg'])
                    sys.exit(0)
                if required is False and len(input_value) == 0:
                    input_value = None
                    break
                if self.VALIDATORS[validator][0] == 'regex':
                    result = re.match(self.VALIDATORS[validator][1], input_value)
                    if result is None:
                        raise TypeError
                if self.VALIDATORS[validator][0] == 'datetime':
                    datetime.datetime.strptime(input_value, self.VALIDATORS[validator][1])
            except (TypeError, ValueError) as err:
                error_message = self.STRINGS['error_msg'] + self.VALIDATORS[validator][3]
                print(error_message.format(**self.FORMATTERS), err)
                continue
            else:
                break
        return input_value

    def confirm(self, validator):
        """Prompt for Yes or No confirmation, validate, and return value.

        :param validator: A dictionary key representing a built-in validation method.
        :type validator: string
        """
        while True:
            try:
                prompt = self.STRINGS['prompt_msg'] + self.VALIDATORS[validator][2]
                response = input(prompt.format(**self.FORMATTERS))
                if response in ['q', 'Q']:
                    print(self.STRINGS['quit_msg'])
                    sys.exit(0)
                if response not in self.VALIDATORS[validator][1]:
                    raise ValueError
            except ValueError as value_error:
                error_message = self.STRINGS['error_msg'] + self.VALIDATORS[validator][3]
                print(error_message.format(**self.FORMATTERS), value_error)
                continue
            else:
                break
        return response.lower()
