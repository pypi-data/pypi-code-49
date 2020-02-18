#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Tests for the Device SE ILS2T stepper motor.
"""

from queue import Queue
from typing import Any

import pytest

from hvl_ccb.comm import ModbusTcpCommunication, ModbusTcpConnectionFailedException
from hvl_ccb.dev import (
    ILS2T,
    ILS2TConfig,
    IoScanningModeValueError,
    ScalingFactorValueError,
    ILS2TException,
)


class MaskedModbusTcpCommunication(ModbusTcpCommunication):
    def __init__(self, configuration):
        super().__init__(configuration)

        self.simulate_running = True
        self.simulate_enabled = True
        self.simulate_error = False

        self._write_buffer = Queue()

    def open(self):
        pass

    def close(self):
        pass

    def write_registers(self, address: int, values: Any):
        pair = (address, values)
        self._write_buffer.put(pair)

    def get_written(self):
        return self._write_buffer.get() if not self._write_buffer.empty() else None

    def read_holding_registers(self, address: int, count: int):
        if address == ILS2T.RegAddr.IO_SCANNING and count == 8:
            # read IOscanning registers
            if self.simulate_running and self.simulate_enabled:
                # {'mode': 3, 'action': 2, 'ref_16': 1500, 'ref_32': 16000000,
                # 'state': 6, 'halt': False, 'turning_positive': True,
                # 'turning_negative': False}
                return [547, 1500, 244, 9216, 6, 816, 16512, 0]
            elif not self.simulate_running and self.simulate_enabled:
                # {'mode': 3, 'action': 2, 'ref_16': 1500, 'ref_32': 0, 'state': 6,
                # 'fault': False, 'warn': False, 'halt': False, 'motion_zero': True,
                # 'turning_positive': False, 'turning_negative': False}
                return [675, 1500, 0, 0, 24582, 49968, 2112, 0]
            else:
                # {'mode': 3, 'action': 2, 'ref_16': 1500, 'ref_32': 0, 'state': 4,
                # 'halt': True, 'turning_positive': False, 'turning_negative': False}
                return [291, 1500, 0, 0, 57348, 816, 2112, 0]

        return [i for i in range(count)]

    def read_input_registers(self, address: int, count: int):
        if address == ILS2T.RegAddr.TEMP and count == 2:
            # read out temperature
            return [0, 35]

        if address == ILS2T.RegAddr.POSITION and count == 2:
            # read out position
            return [1, 2_599]

        if address == ILS2T.RegAddr.VOLT and count == 2:
            # read out DC voltage
            return [0, 480]  # 48.0 V

        if address == ILS2T.RegAddr.FLT_INFO and count == 22:
            return [0] * count if self.simulate_error else [i for i in range(count)]

        return [i for i in range(count)]


@pytest.fixture(scope="module")
def com_config():
    return {
        "host": "127.0.0.1",
        "unit": 0,
        "port": 502,
    }


@pytest.fixture(scope="module")
def dev_config():
    return {
        "wait_sec_post_enable": 0.01,
        "wait_sec_post_relative_step": 0.01,
        "wait_sec_post_absolute_position": 0.01,
    }


@pytest.fixture
def testdev(com_config, dev_config):
    modbus_tcp = MaskedModbusTcpCommunication(com_config)
    motor = ILS2T(modbus_tcp, dev_config)
    assert motor is not None
    motor.start()
    assert modbus_tcp.get_written() == (motor.RegAddr.ACCESS_ENABLE.value, [0, 1])
    assert modbus_tcp.get_written() == (
        motor.RegAddr.RAMP_N_MAX.value,
        [0, ILS2TConfig.rpm_max_init],
    )
    yield motor
    motor.stop()


@pytest.mark.parametrize(
    "config_key,wrong_value",
    [
        ("rpm_max_init", 0),
        ("rpm_max_init", -1),
        ("rpm_max_init", 3001),
        ("wait_sec_post_enable", 0),
        ("wait_sec_post_enable", -1),
        ("wait_sec_post_relative_step", 0),
        ("wait_sec_post_absolute_position", 0),
    ],
)
def test_wrong_config_value(com_config, dev_config, config_key, wrong_value):
    wrong_config = dict(dev_config)
    wrong_config[config_key] = wrong_value
    with pytest.raises(ValueError):
        ILS2T(com_config, wrong_config)


def test_clean_ioscanning_mode_values(testdev: ILS2T):
    default_values = testdev.DEFAULT_IO_SCANNING_CONTROL_VALUES

    # default values need to work
    assert testdev._clean_ioscanning_mode_values(default_values) == default_values

    # missing key that gets loaded from defaults
    other_values = dict(default_values)
    other_values.pop("mode")
    assert testdev._clean_ioscanning_mode_values(other_values) == default_values

    # additional key that is not needed
    other_values = dict(default_values)
    other_values["some_other_key"] = None
    with pytest.raises(ValueError):
        testdev._clean_ioscanning_mode_values(other_values)

    # invalid mode
    other_values = dict(default_values)
    other_values["mode"] = -1
    with pytest.raises(IoScanningModeValueError):
        testdev._clean_ioscanning_mode_values(other_values)

    # with mode 1: JOG
    # ----------------
    other_values = dict(default_values)
    other_values["mode"] = 1

    # action has to be 0
    other_values["action"] = -1
    with pytest.raises(IoScanningModeValueError):
        testdev._clean_ioscanning_mode_values(other_values)

    other_values["action"] = 0
    # action is 0, but ref_16 is still 1500
    with pytest.raises(IoScanningModeValueError):
        testdev._clean_ioscanning_mode_values(other_values)

    # one of the valid values for ref_16 in JOG mode
    other_values["ref_16"] = 1
    assert testdev._clean_ioscanning_mode_values(other_values) == other_values

    # action and ref_16 valid, but ref_32 not `0`
    other_values["ref_32"] = 1
    with pytest.raises(IoScanningModeValueError):
        testdev._clean_ioscanning_mode_values(other_values)

    # with mode 3: Point to Point
    # ---------------------------
    other_values = dict(default_values)
    other_values["mode"] = 3

    # action has to be 1, 2 or 3
    other_values["action"] = 4
    with pytest.raises(IoScanningModeValueError):
        testdev._clean_ioscanning_mode_values(other_values)

    other_values["action"] = 1

    # too high RPM
    other_values = dict(default_values)
    other_values["ref_16"] = 4000  # too high RPM
    with pytest.raises(IoScanningModeValueError):
        testdev._clean_ioscanning_mode_values(other_values)

    other_values["ref_16"] = 1500
    # needs to work
    assert testdev._clean_ioscanning_mode_values(other_values) == other_values


def test_32bit_decode():
    assert ILS2T._decode_32bit([2 ** 15, 1], signed=False) == 2_147_483_649
    assert ILS2T._decode_32bit([2 ** 15, 1], signed=True) == -2_147_483_647


def test_toggle(testdev: ILS2T):
    actual = testdev._mode_toggle_mt
    testdev._toggle()
    assert actual is not testdev._mode_toggle_mt


def test_start_stop_failing(com_config):
    test_device = ILS2T(com_config)

    with pytest.raises(ModbusTcpConnectionFailedException):
        test_device.start()

    with pytest.raises(ModbusTcpConnectionFailedException):
        test_device.stop()


def test_get_dc_volt(testdev: ILS2T):
    assert testdev.get_dc_volt() == 48.0


def test_get_temperature(testdev: ILS2T):
    assert testdev.get_temperature() == 35


def test_get_position(testdev: ILS2T):
    assert testdev.get_position() == 68_135


def test_enable(testdev: ILS2T):
    testdev.enable()
    assert testdev.com.get_written() == (
        testdev.RegAddr.IO_SCANNING.value,
        testdev._generate_control_registers(enable_driver_en=1),
    )


def test_disable(testdev: ILS2T):
    testdev.com.simulate_running = False
    testdev.disable()
    assert testdev.com.get_written() == (
        testdev.RegAddr.IO_SCANNING.value,
        testdev._generate_control_registers(disable_driver_di=1),
    )

    testdev.com.simulate_running = True
    testdev.disable()
    assert testdev.com.get_written() is None


def test_relative_step(testdev: ILS2T):
    testdev.com.simulate_enabled = False
    testdev.com.simulate_running = False
    testdev.com.simulate_error = False

    testdev.relative_step(16_000)

    with pytest.raises(IoScanningModeValueError):
        testdev.relative_step(5_000_000_000)

    testdev.relative_step_and_wait(50_000)

    testdev.com.simulate_error = True
    testdev.relative_step_and_wait(10000)


def test_absolute_position(testdev: ILS2T):
    testdev.com.simulate_enabled = False
    testdev.com.simulate_running = False
    testdev.com.simulate_error = False

    testdev.absolute_position(0)

    with pytest.raises(IoScanningModeValueError):
        testdev.absolute_position(5_000_000_000)

    testdev.com.simulate_running = False

    testdev.absolute_position_and_wait(100_000)

    testdev.com.simulate_error = True
    testdev.absolute_position_and_wait(10000)


def test_set_max_rpm(testdev: ILS2T):
    testdev.set_max_rpm(500)
    assert testdev.com.get_written() == (testdev.RegAddr.RAMP_N_MAX.value, [0, 500])

    with pytest.raises(ILS2TException):
        testdev.set_max_rpm(-100)
    assert testdev.com.get_written() is None


def test_set_ramp_type(testdev: ILS2T):
    testdev.set_ramp_type(0)
    assert testdev.com.get_written() == (testdev.RegAddr.RAMP_TYPE.value, [0, 0])


def test_user_steps(testdev: ILS2T):
    testdev.user_steps(10, 1)
    assert testdev.com.get_written() == (testdev.RegAddr.SCALE.value, [0, 10, 0, 1])

    with pytest.raises(ScalingFactorValueError):
        testdev.user_steps(5.5, 3)
    assert testdev.com.get_written() is None

    with pytest.raises(ScalingFactorValueError):
        testdev.user_steps(5, 3.75)
    assert testdev.com.get_written() is None


def test_quickstop(testdev: ILS2T):
    testdev.com.simulate_running = True
    testdev.quickstop()
    testdev.reset_error()


def test_get_status(testdev: ILS2T):
    testdev.get_status()


def test_jog_run(testdev: ILS2T):
    for running in (True, False):
        for enabled in (True, False):
            testdev.com.simulate_enabled = enabled
            testdev.com.simulate_running = running
            testdev.jog_run(direction=True)
            testdev.jog_run(direction=False)
            testdev.jog_run(direction=True, fast=True)
            testdev.jog_run(direction=False, fast=True)
            testdev.jog_stop()


def test_set_jog_speed(testdev: ILS2T):
    testdev.set_jog_speed(1, 1000)
    assert testdev.com.get_written() == (testdev.RegAddr.JOGN_SLOW.value, [0, 1])
    assert testdev.com.get_written() == (testdev.RegAddr.JOGN_FAST.value, [0, 1000])


def test_set_max_acceleration(testdev: ILS2T):
    testdev.set_max_acceleration(5000)
    assert testdev.com.get_written() == (testdev.RegAddr.RAMP_ACC.value, [0, 5000])


def test_set_max_deceleration(testdev: ILS2T):
    testdev.set_max_deceleration(5000)
    assert testdev.com.get_written() == (testdev.RegAddr.RAMP_DECEL.value, [0, 5000])
