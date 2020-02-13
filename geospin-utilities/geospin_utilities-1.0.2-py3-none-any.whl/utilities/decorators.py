"""A collection of useful decorators."""

import time
import sys
import logging

from functools import wraps
from logging.handlers import RotatingFileHandler


def retry(exception, tries=4, delay=3, backoff=2):
    """
    Retry calling the decorated function using an exponential backoff in case
    of a specific exception.

    :param Exception exception: The exception type to be caught.
    :param int tries: Number of retries before giving up catching the exception.
    :param int delay: Delay before first retry in seconds.
    :param int backoff: Factor to multiply the retry delay by each time.
    :return function outer_retry: Wrapped original function.

    .. seealso::
       http://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
    """
    def outer_retry(func):

        @wraps(func)
        def inner_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except exception:
                    print('Retrying in {:.2f} seconds...'.format(mdelay))
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return func(*args, **kwargs)

        return inner_retry

    return outer_retry


class Log(object):
    """
    Emulate a file object as required by ``logprint``.

    .. seealso::
       https://wiki.python.org/moin/PythonDecoratorLibrary#Redirects_stdout_printing_to_python_standard_logging # noqa: E501
    """
    def __init__(self):
        self.logger = logging.getLogger('print')
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            handler = RotatingFileHandler('print.log', maxBytes=5000,
                                          backupCount=10)
            self.logger.addHandler(handler)

    def write(self, text):
        """
        Passes input text to logger object.
        :param str text: Text output by the wrapped function's print calls.
        """
        self.logger.info(text)


def log_print(func):
    """
    Instead of printing, logs all calls to print at the INFO level and stores to
    `print.log` in chunks of 5kB.

    :param function func: The function or method to be wrapped.
    """
    def wrapper(*arg, **kwargs):
        stdout_backup = sys.stdout
        sys.stdout = Log()
        try:
            return func(*arg, **kwargs)
        finally:
            sys.stdout = stdout_backup
    return wrapper
