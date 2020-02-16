"""
Argument type verification
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""

import os
import argparse
import re


def _string_to_version(arg_string):
    """Convert a string to a match with parts as groups

    :param arg_string: version string
    :return: match object with version parts as groups
    """
    return re.match(r'^(\d+).(\d+).(\d+).(\d+)$', arg_string)


def build_version(arg_string):
    """Argument verification for valid build versions

    :param arg_string: version string
    :return: match object with version parts as groups
    :exception: invalid version string
    """
    version = _string_to_version(arg_string)
    if version:
        return version
    raise argparse.ArgumentTypeError(f'Invalid version: {arg_string}')


def exiting_file(arg_string):
    """Argument verification for existing-file paths

    :param arg_string: full or relative file path
    :return: the path, as received
    :exception: illegal path or file doesn't exist
    """
    if arg_string and os.path.isfile(arg_string):
        return arg_string
    raise argparse.ArgumentTypeError(f'File {arg_string} not found')


def yes_or_no(arg_string):
    """Argument verification for 'yes'/'no' flags

    :param arg_string: parameter string
    :return: True of 'yes', false if 'no'
    :exception: other values
    """
    answer = arg_string.lower().strip()
    if answer == 'yes':
        return True
    if answer == 'no':
        return False
    raise argparse.ArgumentTypeError(f'Expected a yes/no value, got "{answer}"')
