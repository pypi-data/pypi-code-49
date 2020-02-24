"""
StdOut and StdErr log maker
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
import logging
import sys


class _LessThanFilter(logging.Filter):
    """Logging filter for messages below a certain level"""

    def __init__(self, exclusive_maximum, name=""):
        """Initialize this instance to filter messages below the maximum

        :param exclusive_maximum: max level
        :param name: filter name (optional)
        """
        super(_LessThanFilter, self).__init__(name)
        self.max_level = exclusive_maximum

    def filter(self, record):
        """Filter log records

        :param record: log record
        :return: 1 if record is to be shown, 0 otherwise
        """
        return 1 if record.levelno < self.max_level else 0

    def __str__(self):
        return "LessThan " + self.max_level


def make_logger_by_verbose_arg(name):
    """Makes a logger which prints info into stdout, and all others to stderr
    If '--verbose' appears in the scrip arguments, debug is also sent to stdout

    :param name: logger name
    :return: logger
    """
    return make_logger(name, '--verbose' in sys.argv)


def make_logger(name, is_verbose):
    """Makes a logger which prints info into stdout, and all others to stderr
    If isVerbose' is set, debug is also sent to stdout

    :param is_verbose: Should debug appear in log
    :param name: logger name
    :return: logger
    """
    new_logger = logging.getLogger(name)
    if is_verbose:
        new_logger.setLevel(logging.DEBUG)
    else:
        new_logger.setLevel(logging.INFO)

    logging_handler_out = logging.StreamHandler(sys.stdout)
    logging_handler_out.setLevel(logging.DEBUG)
    logging_handler_out.addFilter(_LessThanFilter(logging.WARNING))
    new_logger.addHandler(logging_handler_out)

    logging_handler_err = logging.StreamHandler(sys.stderr)
    logging_handler_err.setLevel(logging.WARNING)
    new_logger.addHandler(logging_handler_err)
    return new_logger
