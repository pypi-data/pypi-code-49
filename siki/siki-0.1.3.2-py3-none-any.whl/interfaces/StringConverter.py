# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Created: Feb 13, 2020
# LastChg: Feb 18, 2020

import re

from siki.basics import Validators as valid


def convert_string_none(value):
    """
    this method will convert string none to the python none type
    """
    if type(value) is str:
        val = value.lower() # convert all characters to lower case

        if val == "none" or val == "null":
            return None
    
    return value


def convert_string_boolean(value):
    """
    this method will convert string boolean to the python boolean type
    """
    if type(value) is str:
        val = value.lower() # convert all characters to lower case

        if val == "yes" or val == "true":
            return True
        elif val == "no" or val == "false":
            return False

    return False # to prevent other invalid cases


def convert_string_number(value):
    """
    this method will convert string data to python number
    """
    if type(value) is str:
        if valid.check_number(value):
            return int(value)
    
    return 0 # to prevent other invalid cases


def convert_string_float(value):
    """
    this method will convert string data to python float
    """
    if type(value) is str:
        if valid.check_float(value):
            return float(value)

    return 0.0 # to prevent other invalid cases