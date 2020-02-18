#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Tests for .comm sub-package
"""
import dataclasses
import time

import pytest

from hvl_ccb.comm import (
    SerialCommunication,
    SerialCommunicationConfig,
    SerialCommunicationIOError,
)


@pytest.fixture(scope="module")
def testconfig():
    return SerialCommunicationConfig(
        port="loop://?logging=debug",
        baudrate=115200,
        parity=SerialCommunicationConfig.Parity.NONE,
        stopbits=SerialCommunicationConfig.Stopbits.ONE,
        bytesize=SerialCommunicationConfig.Bytesize.EIGHTBITS,
        terminator=b'\r\n',
        timeout=0.2
    )


def test_serial_config(testconfig):
    with pytest.raises(ValueError):
        dataclasses.replace(testconfig, parity='B')

    with pytest.raises(ValueError):
        dataclasses.replace(testconfig, stopbits=2.5)

    with pytest.raises(ValueError):
        dataclasses.replace(testconfig, bytesize=9)

    with pytest.raises(ValueError):
        dataclasses.replace(testconfig, timeout=-1)


def _decode_terminator(testconfig):
    return testconfig.terminator.decode(SerialCommunication.ENCODING)


def test_timeout(testconfig):
    with SerialCommunication(testconfig) as sc:
        started_at = time.time()
        assert sc.read_text() == ''
        elapsed = time.time() - started_at
        timeout = testconfig.timeout
        assert elapsed >= timeout
        assert elapsed < 1.25 * timeout


def _test_loop_serial_communication_text(testconfig, sc):
    # send some text
    test_strings = [
        "Test message 1",
        "testmessage2",
        "190testmessage: 3",
    ]

    for t in test_strings:
        # send line
        sc.write_text(t)
        # read back line
        answer = sc.read_text()
        assert answer == t + _decode_terminator(testconfig)


def _test_loop_serial_communication_bytes(testconfig, sc):
    # send some bytes
    test_bytes = [
        b"Test message 1",
        b"testmessage2",
        b"190testmessage: 3",
    ]

    for d in test_bytes:
        # send line
        n = sc.write_bytes(d)
        # read back bytes
        answer = sc.read_bytes(n)
        assert answer == d


def test_serial_open_error(testconfig):

    config_dict = dataclasses.asdict(testconfig)
    config_dict['port'] = '12345666'
    com = SerialCommunication(config_dict)
    with pytest.raises(SerialCommunicationIOError):
        com.open()


def test_serial_open_write_read_close(testconfig):
    """
    Tests SerialCommunication
    """

    # manually open/close port
    sc = SerialCommunication(testconfig)
    assert sc is not None
    assert not sc.is_open
    sc.open()
    assert sc.is_open
    sc.open()  # no error when re-opening an open port
    _test_loop_serial_communication_text(testconfig, sc)
    _test_loop_serial_communication_bytes(testconfig, sc)
    sc.close()
    assert not sc.is_open

    # or use with statement
    with SerialCommunication(testconfig) as sc:
        assert sc is not None
        assert sc.is_open
        _test_loop_serial_communication_text(testconfig, sc)


def test_serial_write_read_error(testconfig):

    sc = SerialCommunication(testconfig)

    # port not opened => errors
    assert not sc.is_open
    with pytest.raises(SerialCommunicationIOError):
        sc.write_text("anything")
    with pytest.raises(SerialCommunicationIOError):
        sc.read_text()
    with pytest.raises(SerialCommunicationIOError):
        sc.write_bytes(b"anything")
    with pytest.raises(SerialCommunicationIOError):
        sc.read_bytes(5)

    # nothing to read => empty output
    sc.open()
    assert sc.is_open
    assert sc.read_text() == ''
    assert sc.read_bytes(5) == b''
