#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Test module for the Supercube Variant A class.
"""

import pytest

from hvl_ccb.dev.supercube import SupercubeWithFU, constants
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
        'port': 14124,
        'endpoint_name': ''
    }


@pytest.fixture(scope='module')
def demo_server(dev_config):
    opcua_server = DemoServer(dev_config['namespace_index'], 'B', 14124)
    opcua_server.start()

    # add socket nodes
    for socket in constants.GeneralSockets:
        opcua_server.add_var(socket, False, True)

    # add support input and output nodes
    for support in constants.GeneralSupport:
        opcua_server.add_var(support, False, True)

    opcua_server.add_var(constants.OpcControl.active, False, True)

    yield opcua_server

    opcua_server.stop()


@pytest.fixture(scope='module')
def cube(com_config, dev_config, demo_server):
    cube = SupercubeWithFU(com_config, dev_config)
    cube.start()
    yield cube
    cube.stop()


def test_instantiation(com_config):
    cube = SupercubeWithFU(com_config)
    assert cube is not None


def test_set_target_voltage(cube: SupercubeWithFU, demo_server: DemoServer):
    demo_server.add_var(constants.Power.voltage_target, 0.0, True)
    cube.set_target_voltage(20)
    assert demo_server.get_var(constants.Power.voltage_target) == 20.0


def test_get_target_voltage(cube: SupercubeWithFU):
    cube.set_target_voltage(23.2e3)
    assert cube.get_target_voltage() == 23.2e3


def test_get_max_voltage(cube: SupercubeWithFU, demo_server: DemoServer):
    demo_server.add_var(constants.Power.voltage_max, 80, False)
    assert cube.get_max_voltage() == 80.0


def test_set_slope(cube: SupercubeWithFU, demo_server: DemoServer):
    demo_server.add_var(constants.Power.voltage_slope, 1.5, True)
    cube.set_slope(5.5)
    assert demo_server.get_var(constants.Power.voltage_slope) == 5.5


def test_get_primary_voltage(cube: SupercubeWithFU, demo_server: DemoServer):
    demo_server.add_var(constants.Power.voltage_primary, 23.2, False)
    assert cube.get_primary_voltage() == 23.2


def test_get_primary_current(cube: SupercubeWithFU, demo_server: DemoServer):
    demo_server.add_var(constants.Power.current_primary, 1.2, False)
    assert cube.get_primary_current() == 1.2


def test_get_frequency(cube: SupercubeWithFU, demo_server: DemoServer):
    demo_server.add_var(constants.Power.frequency, 50, False)
    assert cube.get_frequency() == 50.0


def test_get_power_setup(cube: SupercubeWithFU, demo_server: DemoServer):
    demo_server.add_var(constants.Power.setup, 1, False)
    assert cube.get_power_setup() == constants.PowerSetup(1)


def test_get_fso_active(cube: SupercubeWithFU, demo_server: DemoServer):
    demo_server.add_var(constants.BreakdownDetection.activated, True, False)
    assert cube.get_fso_active() is True


def test_fso_reset(cube: SupercubeWithFU, demo_server: DemoServer):
    demo_server.add_var(constants.BreakdownDetection.reset, False, True)
    cube.fso_reset()
    assert demo_server.get_var(constants.BreakdownDetection.reset) is False
