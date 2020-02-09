"""
Utilities
=====
Assorted utilities for the Platea package.
"""

import time
import warnings
import functools
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Timer:
    """
    Timer.

    A convenient class for timing things.

    Attributes
    ----------
    None

    Methods
    -------
    None

    Examples
    --------
    >>> with pla.utilities.Timer()
    >>>     do someting
    """

    def __init__(self):
        """ initialize object """
        self._t0 = None

    def __enter__(self):
        """ start timing """
        self._t0 = time.time()

    def __exit__(self, *args):
        """ stop timing and print results """
        print("Elapsed time: %0.2fs" % (time.time() - self._t0))

def deprecated(func):
    """
    A decorator used to mark functions that are deprecated with a warning.

    Examples
    --------
    >>> @deprecated
    >>> def foo():
    >>>     do something
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # https://stackoverflow.com/questions/2536307/decorators-in-the-python-standard-lib-deprecated-specifically
        # may not want to turn filter on and off
        warnings.simplefilter("always", DeprecationWarning)  # turn off filter
        primary_message = "Call to deprecated function {}.".format(func.__name__)
        warnings.warn(primary_message, category=DeprecationWarning, stacklevel=2)
        warnings.simplefilter("default", DeprecationWarning)  # reset filter
        return func(*args, **kwargs)
    return wrapper
