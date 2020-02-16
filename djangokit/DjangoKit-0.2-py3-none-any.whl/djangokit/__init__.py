#
# Copyright (c) 2018, Grigoriy Kramarenko
# All rights reserved.
# This file is distributed under the BSD 3-Clause License.
#
"""A set of extensions for Django used in the construction of complex web
applications.
"""
import os
from djangokit.utils import version

VERSION = (0, 2, 0, 'final', 0)


def get_version():
    path = os.path.dirname(os.path.abspath(__file__))
    return version.get_version(VERSION, path)


__version__ = get_version()
