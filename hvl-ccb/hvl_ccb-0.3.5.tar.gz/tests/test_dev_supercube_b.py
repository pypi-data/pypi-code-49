#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Test module for the Supercube Variant B class.
"""

import pytest

from hvl_ccb.dev.supercube import SupercubeB


@pytest.fixture(scope='module')
def com_config():
    return {
        'host': '127.0.0.1',
    }


def test_instantiation(com_config):
    cube = SupercubeB(com_config)
    assert cube is not None
