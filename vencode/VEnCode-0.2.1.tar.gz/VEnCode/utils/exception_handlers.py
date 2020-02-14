"""exception_handlers.py: module for handling exceptions."""
import logging
from VEnCode.utils import util


def argument_exception(error_args):
    """
    Handles mistakes in key arguments by letting the user re-insert the argument.
    :param error_args: the argument's name that had the mistake. Str
    :param logger: must log the mistake and the new argument. logging object
    :return: the new argument
    """
    arg_new = input("Argument {0} was not correct, please submit another argument: ".format(error_args))
    return arg_new
