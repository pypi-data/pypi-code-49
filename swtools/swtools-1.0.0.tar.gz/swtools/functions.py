# -*- coding: utf-8 -*-

"""Miscellaneous utility functions.

A toolbox of re-usable functions that provides helpers
for use across the application's modules and classes.

"""

# standard library modules
import os
import sys
import re
import argparse
import datetime

# 3rd party modules
import tzlocal


def convert_to_local(time):
    """Convert UTC time to local time.

    :param time: The time in UTC format (%H%M).
    :type time: str

    :returns: The time in military (24-hour) format (%H:%M).
    :rtype: str
    """
    offset = get_offset_hours()
    in_time = datetime.datetime.strptime(time, '%H%M') + datetime.timedelta(hours=offset)
    return datetime.datetime.strftime(in_time, '%H:%M')


def convert_to_utc(time):
    """Convert local time to UTC time.

    :param time: The time in military (24-hour) format (%H:%M).
    :type time: str

    :returns: The time in UTC format (%H%M).
    :rtype: str
    """
    offset = get_offset_hours()
    in_time = datetime.datetime.strptime(time, '%H:%M') - datetime.timedelta(hours=offset)
    return datetime.datetime.strftime(in_time, '%H%M')


def get_offset_hours():
    """Find the number of offset hours from UTC.

    :returns: The number of hours offset from UTC based on current time zone.
    :rtype: int
    """
    tz = tzlocal.get_localzone()
    d = datetime.datetime.now(tz)
    offset = d.utcoffset().total_seconds() / 60 / 60
    return offset


def first_digit(str):
    """Find the index of the first digit in a string.

    :param str: The string to parse.
    :type str: str

    :returns: The position of the first digit found.
    :rtype: int
    """
    for i, c in enumerate(str):
        if c.isdigit():
            return i
            break


def generate_argparser(app_name):
    """Create a generic argument parser object with help and version options only.

    :param app_name: A string representing the application name to display.
    :type app_name: string

    :returns: An argument parser object.
    :rtype: obj
    """
    parser = argparse.ArgumentParser(
        description=app_name,
        formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=36),
        add_help=False,
        allow_abbrev=False)
    parser.add_argument(
        '-h',
        '--help',
        action='store_true',
        dest='help',
        default=argparse.SUPPRESS)
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version=program_version(app_name))
    return parser


def program_version(app_name):
    """Return the package version for use with argparse.

    The version number is found in __init__.py.

    :param app_name: A string representing the application name to display.
    :type app_name: str

    :returns: A string with the application name, version, location, and the Python version.
    :rtype: str
    """
    root = os.path.dirname(__file__)
    version_re = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')
    with open(os.path.join(root, '__init__.py'), 'rt', encoding='utf8') as f:
        version = version_re.search(f.read()).group(1)
    python_version = ".".join(map(str, sys.version_info[:3]))
    location = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    message = u'{} {} from {} (Python {})'
    return message.format(app_name, version, location, python_version)
