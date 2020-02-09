"""Tests for MIDI utils."""

from unittest import mock

import pytest

from midiroute import midiutils


@pytest.fixture
def mock_input_port():
    with mock.patch("midiroute.midiutils.mido") as mock_mido:
        mock_mido.get_input_names.return_value = ["input"]
        mock_mido.open_input.return_value = MockPort()
        yield mock_mido


class MockPort:
    callback = None

    def close(self):
        pass


class TestMIDIUtils:
    @pytest.mark.parametrize(
        "port_name, valid_names", (("p", ["alpha", "beta"]), ("g", ["gamma", "delta"]))
    )
    def test_valid_port_name(self, port_name, valid_names) -> None:
        with pytest.raises(midiutils.InvalidPortName):
            midiutils._check_valid_port_name(port_name, valid_names)
