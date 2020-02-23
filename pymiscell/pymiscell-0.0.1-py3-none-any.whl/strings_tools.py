"""Functions that operate in Python string objects.

Intended to be used within a Python 3 environment.
Developed by Rodrigo Rivero.
https://github.com/rodrigo1392

"""

import re
import string


def check_str_for_digits(input_string):
    """Check if a string contains digits.

    Parameters
    ----------
    input_string : str
        Strings to check.

    Returns
    -------
    bool
        True if any digit is found, False otherwise.
    """
    return any(char.isdigit() for char in input_string)


def extract_number_from_str(input_string):
    """Extract last integer (may have several digits) from string.

    Parameters
    ----------
    input_string : str
        String to extract integer from.

    Returns
    -------
    int
        Last number found in string. May contain multiple digits.
    """
    return int(re.findall(r'\d+', str(input_string))[-1])


def format_strings_for_cmd(input_list):
    """Transform a list of string into cmd compatible command.

    Parameters
    ----------
    input_list : list of strings
        Strings to transform.

    Returns
    -------
    str
        Command like string to be passed as command option.
    """
    return "['" + "', '".join(input_list) + "']"


def get_uniques_in_list_of_lists(input_list):
    """Generate flat list of unique values in a list of lists.

    Parameters
    ----------
    input_list : list of lists
        Object to filter from.

    Returns
    -------
    List
        Unique values in input object.
    """
    return list({item for sublist in input_list for item in sublist})


def list_characters(start_char='A', end_char='Z', capitalize=True):
    """Generate alphabetical chars, with MS Excel columns names format.

    List can be beyond Z, with AA, AB,... format.

    Parameters
    ----------
    start_char : str
        Char to start from.
    end_char : str
        Last char of list.
    capitalize : bool, optional
        If True, capitalize each char in output list. Default is True.

    Returns
    -------
    List of str
        List of generated chars.

    Raises
    ------
    AssertionError
        Bad data type in either `start_char` or `end_char`.
    """
    assert isinstance(start_char, str) and isinstance(end_char, str),\
        'Input data should be string type'

    # Get list of ascii characters and with 'aa', 'ab', etc.
    base_list = list(string.ascii_lowercase)
    for i in base_list:
        base_list = base_list + [i + c for c in string.ascii_lowercase]

    # Extract chars of interest and capitalize.
    output_list = base_list[base_list.index(start_char.lower()):
                            base_list.index(end_char.lower()) + 1]
    if capitalize is True:
        output_list = [c.upper() for c in output_list]
    return output_list


def sort_strings_by_digit(paths_list):
    """Try to sort strings by the digits present in them.

    If digits are not found in each of the strings, return the original
    list without changes.

    Parameters
    ----------
    paths_list : List of strings
        Strings to sort.

    Returns
    -------
    List of strings
        Sorted strings if possible.
    """
    # Extract integers and try to sort input list by them. Catch and
    # report digits error.
    try:
        numbers = [extract_number_from_str(i) for i in paths_list]
        paths_list = [x for _, x in sorted(zip(numbers, paths_list))]
    except IndexError:
        print('WARNING: COULD NOT SORT STRINGS LIST BY NUMBER')
    return paths_list
