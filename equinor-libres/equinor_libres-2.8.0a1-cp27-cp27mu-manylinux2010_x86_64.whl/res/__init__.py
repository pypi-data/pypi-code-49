#  Copyright (C) 2011  Equinor ASA, Norway.
#
#  The file '__init__.py' is part of ERT - Ensemble based Reservoir Tool.
#
#  ERT is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  ERT is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.
#
#  See the GNU General Public License at <http://www.gnu.org/licenses/gpl.html>
#  for more details.
"""
Ert - Ensemble Reservoir Tool - a package for reservoir modeling.
"""
import os.path
import sys
import platform
import ctypes
import ecl

import warnings
warnings.filterwarnings(
    action='always',
    category=DeprecationWarning,
    module=r'res|ert'
)

from cwrap import Prototype

from .version import version as __version__

_lib_path = os.path.join(os.path.dirname(__file__), ".libs")
if platform.system() == "Linux":
    _lib_path = os.path.join(_lib_path, "libres.so")
elif platform.system() == "Darwin":
    _lib_path = os.path.join(_lib_path, "libres.dylib")
else:
    raise NotImplementedError("Invalid platform")


class ResPrototype(Prototype):
    lib = ctypes.CDLL(_lib_path, ctypes.RTLD_GLOBAL)

    def __init__(self, prototype, bind=True):
        super(ResPrototype, self).__init__(ResPrototype.lib, prototype, bind=bind)

RES_LIB = ResPrototype.lib

from res.util import ResVersion
from ecl.util.util import updateAbortSignals

updateAbortSignals( )

def root():
    """
    Will print the filesystem root of the current ert package.
    """
    return os.path.abspath( os.path.join( os.path.dirname( __file__ ) , "../"))
