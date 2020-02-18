#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Tests for the .comm.labjack_ljm subpackage.
"""

import logging

import pytest

from hvl_ccb.comm import (
    LJMCommunication,
    LJMCommunicationConfig,
    LJMCommunicationError,
)

logging.disable(logging.ERROR)


@pytest.fixture(scope="module")
def testconfig():
    return {
        # identifier = -2 specifies LJM DEMO mode, see
        # https://labjack.com/support/software/api/ljm/demo-mode
        # however `ljm.getHandleInfo(-2)` raises
        # `LJMError: LJM library error code 1224 LJME_DEVICE_NOT_OPEN`
        "identifier": "-2"
    }


@pytest.fixture
def com(testconfig):
    with LJMCommunication(testconfig) as com:
        yield com


def test_labjack_config_cleaning():
    with pytest.raises(ValueError):
        LJMCommunicationConfig(device_type="T5")

    with pytest.raises(ValueError):
        LJMCommunicationConfig(device_type="T7-Pro")
    config = LJMCommunicationConfig(device_type="T7_PRO")
    assert config.device_type is LJMCommunicationConfig.DeviceType.T7_PRO

    with pytest.raises(ValueError):
        LJMCommunicationConfig(connection_type="Gardena")
    config = LJMCommunicationConfig(connection_type="TCP")
    assert config.connection_type is LJMCommunicationConfig.ConnectionType.TCP


def test_labjack_config_enums():
    config = LJMCommunicationConfig(device_type=LJMCommunicationConfig.DeviceType.T4)
    assert config.device_type == "T4"
    device_type = LJMCommunicationConfig.DeviceType.get_by_p_id(config.device_type.p_id)
    assert device_type is LJMCommunicationConfig.DeviceType.T4
    # test device with unambiguous Product ID
    config = LJMCommunicationConfig(
        device_type=LJMCommunicationConfig.DeviceType.T7_PRO
    )
    assert config.device_type == "T7_PRO"
    device_types = LJMCommunicationConfig.DeviceType.get_by_p_id(
        config.device_type.p_id
    )
    assert device_types == [
        LJMCommunicationConfig.DeviceType.T7,
        LJMCommunicationConfig.DeviceType.T7_PRO,
    ]

    config = LJMCommunicationConfig(
        connection_type=LJMCommunicationConfig.ConnectionType.TCP
    )
    assert config.connection_type == "TCP"


def test_open(testconfig):
    com = LJMCommunication(testconfig)
    assert not com.is_open
    com.open()
    assert com.is_open
    com.open()
    assert com.is_open
    com.close()
    assert not com.is_open

    failing_config = dict(testconfig)
    failing_config["identifier"] = "this_is_an_invalid_identifier"
    com = LJMCommunication(failing_config)
    assert not com.is_open
    with pytest.raises(LJMCommunicationError):
        com.open()
    assert not com.is_open

    # opening T7-Pro version works same as opening T7
    working_config = dict(testconfig)
    for device_type in ("T7_PRO", LJMCommunicationConfig.DeviceType.T7_PRO):
        working_config["device_type"] = device_type
        assert not com.is_open
        with LJMCommunication(working_config) as com:
            assert com.is_open
        assert not com.is_open


def test_read_name(com):
    with pytest.raises(LJMCommunicationError):
        com.read_name("SERIAL_NUMBER")

    with pytest.raises(LJMCommunicationError):
        com.read_name("SERIAL_NUMBER", "SERIAL_NUMBER")

    with pytest.raises(LJMCommunicationError):
        com.read_name("SERIAL_NUMBER", return_num_type=int)

    with pytest.raises(TypeError):
        com.read_name(123)


def test_write_name(com):
    with pytest.raises(LJMCommunicationError):
        com.write_name("test", 0)

    with pytest.raises(LJMCommunicationError):
        com.write_names({"test1": 1, "test2": 2})

    with pytest.raises(TypeError):
        com.write_name(123, 456)


# def test_write_address(com):
#     with pytest.raises(LJMCommunicationError):
#         com.write_address(1234, 5678)
