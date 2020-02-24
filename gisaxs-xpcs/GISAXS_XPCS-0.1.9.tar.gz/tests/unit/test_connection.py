# -*- coding: utf-8 -*-
import pytest
from gisaxs_xpcs import h5_manager, MONETA_DIR


def test_moneta_connection():
    assert MONETA_DIR.path.is_dir()


def test_h5_path():
    assert h5_manager.path.is_file()


def test_xpcs_path():
    assert h5_manager.xpcs_path.parent.is_dir()
