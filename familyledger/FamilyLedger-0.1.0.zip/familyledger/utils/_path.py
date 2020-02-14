"""
A module for retrieving and manipulating path information.

Copyright (C) 2020, fondlez "Anuber"-Kronos, fondlez at protonmail.com
"""
import fnmatch
import os


def extless(path):
    """Returns the filename without a file extension from a path."""
    return os.path.splitext(os.path.basename(path))[0]


def gen_find_file(filepat, top):
    """Yields the paths matching a file pattern.
    
    Args:
        filepat (str): Unix shell-style wildcard pattern.
        top (str): toplevel directory to begin recursively searching.
        
    Yields:
        str: matching path string.
    """
    for path, __, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def splitall(path):
    """Returns all the components of a path, including split on path separator.
    
    Args:
        path (str): path string.
        
    Returns:
        list: list of path components.
    """
    allparts = []
    while True:
        parts = os.path.split(path)
        if parts[0] == path:  # absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path:  # relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts
