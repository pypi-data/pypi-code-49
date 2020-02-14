"""
A module to support use of the built-in logging facility.

Copyright (C) 2020, fondlez "Anuber"-Kronos, fondlez at protonmail.com
"""
import logging
import sys


def configure_root_logger(
        log_file=None, log_level=None, format=None, date_format=None):
    """Configures basic logging of the root logger.
    
    If a log filename is supplied, the root logger is configured to log to file,
    otherwise it is configured to log to ``sys.stderr``.
    
    Args:
        log_file (str): log filename.
        log_level (int): log level.
        format (str): log message format.
        date_format (str): datetime format.
    """
    log_level = log_level or logging.WARNING
    format = format or '%(asctime)s %(name)-16s %(levelname)-8s %(message)s'
    date_format = date_format or '%Y-%m-%dT%H:%M:%S%z'
    if log_file:
        logging.basicConfig(filename=log_file, level=log_level, 
            format=format, datefmt=date_format)
    else:
        logging.basicConfig(stream=sys.stderr, level=log_level,
            format=format, datefmt=date_format)


def get_log(name=''):
    """Returns a named logger object or the root logger."""
    return logging.getLogger(name)


def disable_logging():
    """Disables logging globally."""
    logging.disable(sys.maxsize)


def re_enable_logging():
    """Re-enables logging globally."""
    logging.disable(logging.NOTSET)
