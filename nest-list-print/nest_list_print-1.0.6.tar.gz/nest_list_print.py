#!/usr/bin/env python3

"""
    This is "nester.py" module which provides a function named as "print_lol()"
    This function can print each separate items within a list which may or may
    not include nesting lists. The print function supports following features:
    
    - Indent as specified when encounting a nesting list.
    - The number of indentions can be modified.
    - Can save data into file.
    
"""


def print_lol(source_list, indent=False, level=0, fn='sys.stdout'):
    """ Prints out each item of the source list.
    Args:
        source_list: A list waiting to be print out.

    Returns: None.
    """
    for each_item in source_list:
        if isinstance(each_item, list):
            # If the fetched item is a list, do recursion.
            print_lol(each_item, indent, level + 1, fn)
        else:
            # If the fetched item is not a list, print directly
            # If indent is turned on, indent TABs firstly.
            # Save data to specified file.
            if indent:
                print("\t" * level, end="", file=fn)
            print(each_item, file=fn)
