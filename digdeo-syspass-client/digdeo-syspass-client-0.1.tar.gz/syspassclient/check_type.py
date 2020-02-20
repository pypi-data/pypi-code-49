#!/usr/bin/env python
# -*- coding: utf-8 -*-


# This file is part of SysPass Client
#
# Copyright (C) 2020  DigDeo SAS
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


import re
from syspassclient.constants import dd


def is_str_or_raise(obj=None):
    if not isinstance(obj, str):
        raise TypeError("{0} must be a str type".format(str(obj)))


def is_int_or_raise(obj=None):
    if not isinstance(obj, int):
        raise TypeError("{0} must be a int type".format(str(obj)))


def is_float_or_raise(obj=None):
    if not isinstance(obj, float):
        raise TypeError("{0} must be a float type".format(str(obj)))


def is_dict_or_raise(obj=None):
    if not isinstance(obj, dict):
        raise TypeError("{0} must be a dict type".format(str(obj)))


def is_list_or_raise(obj=None):
    if not isinstance(obj, list):
        raise TypeError("{0} must be a list type".format(str(obj)))


def is_bool_or_raise(obj=None):
    if not isinstance(obj, bool):
        raise TypeError("{0} must be a bool type".format(str(obj)))


def is_url_or_raise(string_url=None):
    """
    Test if a string url is a valide url

    Note if ``string_url`` is set to None the function return FAlse, that because None is not a valide URL.
    :param string_url: a url to check
    :type string_url: str or None
    :return: True if ``string`` contain only valid ASCII character or False if not
    :rtype: bool
    """
    is_str_or_raise(string_url)

    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if re.match(regex, string_url) is None:
        raise ValueError("'api_url' must be a valid URL")


def is_ascii_or_raise(string_data=None):
    """
    Test if a string contain only ASCCI char.

    If ``string_data`` is set to None , the function just raise a TypeError, because None is not a ASCII char.

    :param string_data: the string to check
    :type string_data: str
    :raise TypeError: when string_data is not a str
    :raise ValueError: when string_data contain a none ascii char
    """
    is_str_or_raise(string_data)

    for character in string_data:
        if character not in dd.ascii_all:
            raise ValueError("{0} must be contain only ascii char".format(str(string_data)))
