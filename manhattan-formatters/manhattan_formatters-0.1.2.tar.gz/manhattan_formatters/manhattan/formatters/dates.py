"""
NOTE: This file provides support for legacy applications, however, we warn
users they should upgrade their imports.
"""

import warnings

from . import chrono
from .chrono import *

from manhattan.utils.chrono import str_to_date, str_to_datetime

__all__ = set(chrono.__all__)
__all__.add('str_to_date')
__all__.add('str_to_datetime')
__all__ = tuple(__all__)


warnings.warn(
    'manhattan.formatters.{dates} should be replaced with chrono',
    FutureWarning
)
