#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Tests for the dev.base module classes.
"""

import pytest

from hvl_ccb.dev import Device, DeviceSequenceMixin, DeviceExistingException

# make Device instantiable
Device.__abstractmethods__ = frozenset()


class DeviceSequence(DeviceSequenceMixin):
    pass


def test_device_sequence_access():

    dev = Device()

    ddict = {'dev': dev}

    dseq = DeviceSequence(ddict)

    assert dseq.get_device('dev') is dev

    for name, device in dseq.get_devices():
        assert ddict[name] is device

    # same devices, same sequence
    assert dseq == DeviceSequence(ddict)

    with pytest.raises(ValueError):
        dseq.remove_device('not there')

    with pytest.raises(DeviceExistingException):
        dseq.add_device('dev', dev)

    dev2 = Device()
    dseq.add_device('dev2', dev2)
    assert dseq.get_device('dev2') is dev2
    assert dseq != DeviceSequence(ddict)


def test_device_sequence_dot_lookup():

    dev1 = Device()
    dev2 = Device()

    ddict = {
        'dev1': dev1,
        'dev2': dev2,
    }

    seq = DeviceSequence(ddict)

    assert seq.dev1 is dev1
    assert seq.dev2 is dev2

    # adding device which name over-shadows attr/method
    with pytest.raises(ValueError):
        DeviceSequence({'dev1': dev1, '_devices': dev2})

    # adding single device which name over-shadows an attr/method
    with pytest.raises(ValueError):
        seq.add_device('start', Device())
