"""This is the nester.py module, and it provides one function called
    print_list() which prints lists that may or may not include nested lists."""


def print_list(the_list):

    """This function takes a positional argument called “the_list", which is any
    Python list (of, possibly, nested lists). Each data item in the provided list
    is (recursively) printed to the screen on its own line."""

    for each_items in the_list:
        if isinstance(each_items, list):
            print_list(each_items)
        else:
            print(each_items)