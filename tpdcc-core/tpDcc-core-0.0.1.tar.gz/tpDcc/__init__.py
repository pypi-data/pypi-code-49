#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tpDcc-core
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from pkgutil import extend_path

if False:
    from tpDcc.abstract import dcc
    Dcc = dcc.AbstractDCC()

__path__ = extend_path(__path__, __name__)
