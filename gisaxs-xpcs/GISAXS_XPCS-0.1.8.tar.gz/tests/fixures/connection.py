# -*- coding: utf-8 -*-

import pytest
from gisaxs_xpcs import h5_manager, MONETA_DIR

__all__ = ['moneta_connnection', 'h5_raw_data_path', 'h5_xpcs']


@pytest.fixture(scope='session', autouse=True)
def moneta_connnection():
    MONETA_DIR._set_default_dir()


@pytest.fixture(scope='session', autouse=True)
def h5_raw_data_path():
    h5_manager.set_path('/media/vladimir/data1/GISAXS_DATA/test_raw_data.h5')


@pytest.fixture(scope='session', autouse=True)
def h5_xpcs():
    h5_manager.set_xpcs_path('/media/vladimir/data1/GISAXS_DATA/xpcs_data.h5')
