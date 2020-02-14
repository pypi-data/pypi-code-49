"""
A module for exception handling utilities.

Copyright (C) 2020, fondlez "Anuber"-Kronos, fondlez at protonmail.com
"""
import sys


def set_exception_handler(
        exception_type, exception, traceback, debug_hook=sys.excepthook,
        debug_flag=False):
    """Sets the default exception handler based on an argument flag.
    
    Args:
        exception_type (object): exception type.
        exception (object): exception instance.
        traceback (:obj:`types.TracebackType`): traceback object.
        debug_hook (function): hook.
        debug_flag (bool): flag to determine whether to set a default exception
            handler or to create customized output.
    """
    if debug_flag:
        debug_hook(exception_type, exception, traceback)
    else:
        print('{} {}'.format(exception_type.__name__, exception))
