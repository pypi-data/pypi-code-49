# Copyright © 2020 R.A. Stern
# SPDX-License-Identifier: LGPL-3.0-or-later

import logging
import logging.handlers
import sys

from .__about__ import (__author__, __build__, __copyright__, __description__,
                        __license__, __title__, __version__)
from .core import _msg, log, init, get_attr, set_attr
from .util import _caller



__all__ = [
    '__author__',
    '__build__',
    '__copyright__',
    '__description__',
    '__license__',
    '__title__',
    '__version__',
    '_msg',
    'init',
    'get_attr',
    'log',
    'set_attr'
]
