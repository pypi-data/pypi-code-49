"""
Pykrete logging
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""

from .make_logger import make_logger, make_logger_by_verbose_arg
from .fatal import fatal

__all__ = ['make_logger', 'make_logger_by_verbose_arg', 'fatal']
