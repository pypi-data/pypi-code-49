#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Masked version of SerialCommunication for testing purposes.
"""

from queue import Queue

from hvl_ccb.comm import SerialCommunication
from hvl_ccb.dev import (
    CryLasLaserSerialCommunication,
    HeinzingerSerialCommunication,
    NewportSMC100PPSerialCommunication,
    PfeifferTPGSerialCommunication,
)


class LoopSerialCommunication(SerialCommunication):
    """
    Serial communication for the tests with "loop://" port. Masks `write_text` method
    and adds `put_text` method to put actual values for the serial communication
    protocol to read with the `read_text` method.
    """

    def __init__(self, configuration):
        super().__init__(configuration)

        self._write_buffer = Queue()

    def _write_text_unsafe(self, text: str):
        self._write_buffer.put(text)

    def put_text(self, text: str):
        super()._write_text_unsafe(text)

    def _write_bytes_unsafe(self, data: bytes):
        self._write_buffer.put(data)

    def put_bytes(self, data: bytes):
        super()._write_bytes_unsafe(data)

    def get_written(self):
        return self._write_buffer.get() if not self._write_buffer.empty() else None


class HeinzingerLoopSerialCommunication(HeinzingerSerialCommunication,
                                        LoopSerialCommunication):
    pass


class LoopCryLasLaserSerialCommunication(CryLasLaserSerialCommunication,
                                         LoopSerialCommunication):
    pass


class NewportLoopSerialCommunication(NewportSMC100PPSerialCommunication,
                                     LoopSerialCommunication):
    pass


class PfeifferTPGLoopSerialCommunication(PfeifferTPGSerialCommunication,
                                         LoopSerialCommunication):
    pass
