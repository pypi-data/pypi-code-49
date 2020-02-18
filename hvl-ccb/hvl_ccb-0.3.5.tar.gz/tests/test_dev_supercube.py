#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Test module for the Supercube base device class.
"""

import pytest

from hvl_ccb.dev.supercube import constants
from hvl_ccb.dev.supercube.base import SupercubeBase
from tests.opctools import DemoServer


@pytest.fixture(scope='module')
def dev_config():
    return {
        'namespace_index': 3,
    }


@pytest.fixture(scope='module')
def com_config():
    return {
        'host': 'localhost',
        'port': 14123,
        'endpoint_name': '',
        'update_period': 10,
    }


@pytest.fixture(scope='module')
def demo_opcua_server(dev_config):
    opcua_server = DemoServer(dev_config['namespace_index'], 'B', 14123)
    opcua_server.start()

    # add socket nodes
    for socket in constants.GeneralSockets:
        opcua_server.add_var(socket, False, True)

    # add support input and output nodes
    for support in constants.GeneralSupport:
        opcua_server.add_var(support, False, True)

    for i, alarm in enumerate(constants.Alarms):
        opcua_server.add_var(alarm, bool(i % 2), False)

    opcua_server.add_var(constants.OpcControl.active, False, True)

    yield opcua_server

    opcua_server.stop()


@pytest.fixture(scope='module')
def cube(com_config, dev_config, demo_opcua_server: DemoServer):
    cube = SupercubeBase(com_config, dev_config)
    cube.start()
    yield cube
    cube.stop()


def test_set_remote_control(cube: SupercubeBase, demo_opcua_server: DemoServer):
    cube.set_remote_control(False)
    assert demo_opcua_server.get_var(constants.OpcControl.active) is False
    cube.set_remote_control(True)
    assert demo_opcua_server.get_var(constants.OpcControl.active) is True


def test_get_support_input(cube: SupercubeBase):
    assert cube.get_support_input(1, 1) is False


def test_support_output(cube: SupercubeBase):
    cube.set_support_output(1, 1, False)
    assert cube.get_support_output(1, 1) is False
    cube.set_support_output(1, 1, True)
    assert cube.get_support_output(1, 1) is True


def test_set_support_output_impulse(cube: SupercubeBase):
    cube.set_support_output_impulse(2, 2, 0.01, True)


def test_get_t13_socket(cube: SupercubeBase):
    assert cube.get_t13_socket(1) is False
    cube.set_t13_socket(1, True)
    assert cube.get_t13_socket(1) is True

    with pytest.raises(ValueError):
        cube.get_t13_socket(4)


def test_set_t13_socket(cube: SupercubeBase):
    cube.set_t13_socket(1, True)

    with pytest.raises(ValueError):
        cube.set_t13_socket(4, False)

    with pytest.raises(ValueError):
        cube.set_t13_socket(1, 'on')


def test_get_cee16(cube: SupercubeBase):
    cube.set_cee16_socket(False)
    assert cube.get_cee16_socket() is False
    cube.set_cee16_socket(True)
    assert cube.get_cee16_socket() is True


def test_set_cee16(cube: SupercubeBase):
    cube.set_cee16_socket(True)
    cube.set_cee16_socket(False)

    with pytest.raises(ValueError):
        cube.set_cee16_socket(1)

    with pytest.raises(ValueError):
        cube.set_cee16_socket('on')


def test_get_status(cube: SupercubeBase, demo_opcua_server: DemoServer):
    demo_opcua_server.add_var(constants.Safety.status, 1, False)
    assert cube.get_status() == constants.SafetyStatus.GreenNotReady

    demo_opcua_server.set_var(constants.Safety.status, 2)
    assert cube.get_status() == constants.SafetyStatus.GreenReady


def test_ready(cube: SupercubeBase, demo_opcua_server: DemoServer):
    demo_opcua_server.add_var(constants.Safety.switchto_ready, False, True)
    cube.ready(True)
    assert demo_opcua_server.get_var(constants.Safety.switchto_ready) is True


def test_operate(cube: SupercubeBase, demo_opcua_server: DemoServer):
    demo_opcua_server.add_var(constants.Safety.switchto_operate, False, True)
    cube.operate(True)
    assert demo_opcua_server.get_var(constants.Safety.switchto_operate) is True


def test_get_measurement_ratio(cube: SupercubeBase, demo_opcua_server: DemoServer):
    demo_opcua_server.add_var(constants.MeasurementsDividerRatio.input_1, 123.4, False)
    assert cube.get_measurement_ratio(1) == 123.4


def test_get_measurement_voltage(cube: SupercubeBase, demo_opcua_server: DemoServer):
    demo_opcua_server.add_var(constants.MeasurementsScaledInput.input_1, 110_000, False)
    assert cube.get_measurement_voltage(1) == 110_000.0


def test_get_earthing_status(cube: SupercubeBase, demo_opcua_server: DemoServer):
    demo_opcua_server.add_var(constants.EarthingStick.status_1, 1, False)
    assert cube.get_earthing_status(1) == constants.EarthingStickStatus(1)


def test_earthing_manual(cube: SupercubeBase, demo_opcua_server: DemoServer):
    demo_opcua_server.add_var(constants.EarthingStick.manual_1, False, True)
    assert cube.get_earthing_manual(1) is False
    cube.set_earthing_manual(1, True)
    assert cube.get_earthing_manual(1) is True


def test_quit_error(cube: SupercubeBase, demo_opcua_server: DemoServer):
    demo_opcua_server.add_var(constants.Errors.quit, False, True)
    cube.quit_error()
    assert demo_opcua_server.get_var(constants.Errors.quit) is False


def test_get_door_status(cube: SupercubeBase, demo_opcua_server: DemoServer):
    demo_opcua_server.add_var(constants.Door.status_1, 2, False)
    assert cube.get_door_status(1) == constants.DoorStatus(2)
