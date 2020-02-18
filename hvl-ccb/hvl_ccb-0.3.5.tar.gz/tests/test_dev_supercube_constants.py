#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Test module for the supercube constants enums.
"""

import pytest

from hvl_ccb.dev.supercube import constants


def test_support_output():
    assert constants.GeneralSupport.output(1, 1) == constants.GeneralSupport.out_1_1
    assert constants.GeneralSupport.output(5, 2) == constants.GeneralSupport.out_5_2
    with pytest.raises(AttributeError):
        constants.GeneralSupport.output(3, 3)


def test_support_input():
    assert constants.GeneralSupport.input(1, 1) == constants.GeneralSupport.in_1_1
    assert constants.GeneralSupport.input(5, 2) == constants.GeneralSupport.in_5_2
    with pytest.raises(AttributeError):
        constants.GeneralSupport.input(3, 3)


def test_measurements_scaled_input():
    assert (constants.MeasurementsScaledInput.get(1) ==
            constants.MeasurementsScaledInput.input_1)
    assert (constants.MeasurementsScaledInput.get(3) ==
            constants.MeasurementsScaledInput.input_3)
    with pytest.raises(AttributeError):
        constants.MeasurementsScaledInput.get(5)


def test_measurements_divider_ratio():
    assert (constants.MeasurementsDividerRatio.get(1) ==
            constants.MeasurementsDividerRatio.input_1)
    assert (constants.MeasurementsDividerRatio.get(3) ==
            constants.MeasurementsDividerRatio.input_3)
    with pytest.raises(AttributeError):
        constants.MeasurementsDividerRatio.get(5)


def test_earthing_stick_status():
    assert (constants.EarthingStick.status(3) ==
            constants.EarthingStick.status_3)
    with pytest.raises(AttributeError):
        constants.MeasurementsDividerRatio.status(7)


def test_earthing_stick_manual():
    assert (constants.EarthingStick.manual(2) ==
            constants.EarthingStick.manual_2)
    with pytest.raises(AttributeError):
        constants.EarthingStick.manual(7)


def test_alarms():
    assert constants.Alarms.get(33) == constants.Alarms.Alarm33
    with pytest.raises(AttributeError):
        constants.Alarms.get(0)


def test_door():
    assert constants.Door.get(3) == constants.Door.status_3
    with pytest.raises(AttributeError):
        constants.Door.get(0)


def test_alarm_text():
    assert constants.AlarmText.get(1) == constants.AlarmText.Alarm1
    assert constants.AlarmText.get(1000) == constants.AlarmText.not_defined
