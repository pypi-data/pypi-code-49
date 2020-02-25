# -*- coding: utf-8 -*-

__title__ = 'PyBoa'
__version__ = '0.1'
__author__ = 'Pythux'

# Version synonym
VERSION = __version__

from .boa_obj import to_boa
from .json_and_yaml import json, yaml

# rename shorter for convenience
boa = to_boa
