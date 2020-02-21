# -*- coding: utf-8 -*-
"""__init__ for mkpreview."""
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from .version import __version__
__all__ = ['config', 'database']
