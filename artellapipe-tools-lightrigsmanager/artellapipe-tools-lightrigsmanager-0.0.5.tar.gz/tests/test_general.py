#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for artellapipe-tools-lightrigsmanager
"""

import pytest

from artellapipe.tools.lightrigsmanager import __version__


def test_version():
    assert __version__.__version__
