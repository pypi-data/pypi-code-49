#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Alexey Strokach.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""

from ipywidgets import DOMWidget
from traitlets import List, Unicode

from ._frontend import module_name, module_version


class MSAView(DOMWidget):
    """Widget controlling the display of a multiple sequence alignment."""

    _model_name = Unicode("MSAModel").tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode("MSAView").tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    value = List().tag(sync=True)
