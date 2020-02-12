#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chime_frb_api import frb_master
import pytest

master = frb_master.FRBMaster(base_url="http://localhost:8001")


def test_get_event_full_header():
    event = master.events.get_event(event_number=9386707, full_header=True)
    assert event["event_register"]["event_no"] == 9386707


def test_get_event():
    event = master.events.get_event(9386707)
    assert event["id"] == 9386707


def test_exception_measured_parameters():
    with pytest.raises(NameError):
        master.events.add_measured_parameters()


def test_name_error_meas_params():
    parameters = {
        "dm": 1.0,
        "dm_error": 1.0,
        "galactic_dm": {},
        "expected_spectrum": [],
        "beam_number": 1123,
        "bad_parameter": "asda",
    }
    with pytest.raises(NameError):
        master.events.add_measured_parameters(
            event_number="9386707", measured_parameters=parameters
        )


def test_type_error_meas_param():
    parameters = {
        "pipeline": {
            "name": "test",
            "status": "test",
            "log": "test",
            "version": "test",
        },
        "dm": 1.0,
        "dm_error": 1.0,
        "galactic_dm": {},
        "expected_spectrum": [],
        "beam_number": 1.0,
    }
    with pytest.raises(TypeError):
        master.events.add_measured_parameters(
            event_number="9386707", measured_parameters=parameters
        )


def test_bad_meas_param():
    parameters = {
        "pipeline": {
            "name": "test",
            "status": "test",
            "log": "test",
            "version": "test",
        },
        "dm": 1,
    }
    with pytest.raises(TypeError):
        master.events.add_measured_parameters(
            event_number="5000000", measured_parameters=parameters
        )
    parameters = {
        "pipeline": {
            "name": "test",
            "status": "test",
            "log": "test",
            "version": "test",
        },
        "galactic_dm": [],
    }
    with pytest.raises(TypeError):
        master.events.add_measured_parameters(
            event_number="5000000", measured_parameters=parameters
        )
    parameters = {
        "pipeline": {
            "name": "test",
            "status": "test",
            "log": "test",
            "version": "test",
        },
        "gain": 1,
    }
    with pytest.raises(TypeError):
        master.events.add_measured_parameters(
            event_number="5000000", measured_parameters=parameters
        )


def test_measured_parameters():
    parameters = {
        "pipeline": {
            "name": "test",
            "status": "test",
            "log": "test",
            "version": "test",
        },
        "dm": 1.0,
        "dm_error": 1.0,
        "galactic_dm": {},
        "expected_spectrum": [],
        "beam_number": 1123,
    }
    status = master.events.add_measured_parameters(
        event_number=9386707, measured_parameters=parameters
    )
    assert status["replaced"] == 1


def test_no_event():
    event = master.events.get_event()
    assert event == "event_number is required."
