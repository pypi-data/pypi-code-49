"""
Fatal issue handler
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from .make_logger import make_logger_by_verbose_arg


def fatal(message, logger_object=None, exception_class=None):
    """Log and raise a fatal error

    :param message: error message
    :param logger_object: logger (optional, will be created if not supplied)
    :param exception_class: Exception class (optional, use Exception if not supplied)
    :exception: always raises an exception of the specified type with the specified message
    """
    (logger_object if logger_object else make_logger_by_verbose_arg('fatal')).error(message)
    raise (exception_class if exception_class else Exception)(message)
