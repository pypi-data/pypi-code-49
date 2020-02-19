# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Create: May 09, 2018
# Modifi: May 09, 2018

# Import system standard modules
import json

from siki.basics import FileUtils as fileutil
from siki.basics import Convert as convert

def parse_json_str(string):
    """
    Load data from json file

    Args: 
    ``filename`` (str), filename with path  
    Returns:  
    ``(dict)``, if load success. None, failed, empty data
    """    
    if string:
        dictionary = json.loads(string)
        return dictionary
    return None


def load_json_file(filename):
    """
    Create a blank file or load data from json file

    Args:  
    ``filename`` (str), filename with path
    Returns:  
    ``dict``, if load success. None, failed, empty data
    """
    # load json file from given filename
    raw = fileutil.read_file(filename)
    if raw:
        return parse_json_str(convert.binary_to_string(raw))
    else:
        return {}


def write_json_file(dictionary, filename):
    """
    Write dictionary to json file
    
    Args: 
    ``dictionary`` (dict), key value pairs  
    ``filename`` (str), filename with path  
    """
    if len(dictionary) > 0:
        raw = convert.string_to_binary(json.dumps(dictionary))
        fileutil.write_file(filename, raw)
