#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Communication protocol for serial ports. Makes use of the `pySerial
<https://pythonhosted.org/pyserial/index.html>`_ library.
"""

from typing import Union, cast

# Note: PyCharm does not recognize the dependency correctly, it is added as pyserial.
import serial

from .base import CommunicationProtocol
from ..configuration import configdataclass
from ..utils.enum import ValueEnum, unique

Number = Union[int, float]


class SerialCommunicationIOError(IOError):
    """Serial communication related I/O errors."""


@unique
class SerialCommunicationParity(ValueEnum):
    """
    Serial communication parity.
    """

    EVEN = serial.PARITY_EVEN
    MARK = serial.PARITY_MARK
    NAMES = serial.PARITY_NAMES
    NONE = serial.PARITY_NONE
    ODD = serial.PARITY_ODD
    SPACE = serial.PARITY_SPACE


@unique
class SerialCommunicationStopbits(ValueEnum):
    """
    Serial communication stopbits.
    """

    ONE = serial.STOPBITS_ONE
    ONE_POINT_FIVE = serial.STOPBITS_ONE_POINT_FIVE
    TWO = serial.STOPBITS_TWO


@unique
class SerialCommunicationBytesize(ValueEnum):
    """
    Serial communication bytesize.
    """

    FIVEBITS = serial.FIVEBITS
    SIXBITS = serial.SIXBITS
    SEVENBITS = serial.SEVENBITS
    EIGHTBITS = serial.EIGHTBITS


@configdataclass
class SerialCommunicationConfig:
    """
    Configuration dataclass for :class:`SerialCommunication`.
    """

    Parity = SerialCommunicationParity
    Stopbits = SerialCommunicationStopbits
    Bytesize = SerialCommunicationBytesize

    #: Port is a string referring to a COM-port (e.g. ``'COM3'``) or a URL.
    #: The full list of capabilities is found `on the pyserial documentation
    #: <https://pythonhosted.org/pyserial/url_handlers.html>`_.
    port: str

    #: Baudrate of the serial port
    baudrate: int

    #: Parity to be used for the connection.
    parity: Union[str, SerialCommunicationParity]

    #: Stopbits setting, can be 1, 1.5 or 2.
    stopbits: Union[Number, SerialCommunicationStopbits]

    #: Size of a byte, 5 to 8
    bytesize: Union[int, SerialCommunicationBytesize]

    #: The terminator character. Typically this is ``b'\r\n'`` or ``b'\n'``, but can
    #: also be ``b'\r'`` or other combinations.
    terminator: bytes = b"\r\n"

    #: Timeout in seconds for the serial port
    timeout: Number = 2

    def clean_values(self):
        if not isinstance(self.parity, SerialCommunicationParity):
            self.force_value("parity", SerialCommunicationParity(self.parity))

        if not isinstance(self.stopbits, SerialCommunicationStopbits):
            self.force_value("stopbits", SerialCommunicationStopbits(self.stopbits))

        if not isinstance(self.bytesize, SerialCommunicationBytesize):
            self.force_value("bytesize", SerialCommunicationBytesize(self.bytesize))

        if self.timeout < 0:
            raise ValueError("Timeout has to be >= 0.")

    def create_serial_port(self) -> serial.Serial:
        """
        Create a serial port instance according to specification in this configuration

        :return: Closed serial port instance
        """

        ser = serial.serial_for_url(self.port, do_not_open=True)
        assert not ser.is_open

        ser.baudrate = self.baudrate
        ser.parity = cast(SerialCommunicationParity, self.parity).value
        ser.stopbits = cast(SerialCommunicationStopbits, self.stopbits).value
        ser.bytesize = cast(SerialCommunicationBytesize, self.bytesize).value
        ser.timeout = self.timeout

        return ser


class SerialCommunication(CommunicationProtocol):
    """
    Implements the Communication Protocol for serial ports.
    """

    ENCODING = "utf-8"
    UNICODE_HANDLING = "replace"

    def __init__(self, configuration):
        """
        Constructor for SerialCommunication.
        """

        super().__init__(configuration)

        self._serial_port = self.config.create_serial_port()

    @staticmethod
    def config_cls():
        return SerialCommunicationConfig

    def open(self):
        """
        Open the serial connection.

        :raises SerialCommunicationIOError: when communication port cannot be opened.
        """

        # open the port
        with self.access_lock:
            try:
                self._serial_port.open()
            except serial.SerialException as exc:
                # ignore when port is already open
                if str(exc) != "Port is already open.":
                    raise SerialCommunicationIOError from exc

    def close(self):
        """
        Close the serial connection.
        """

        # close the port
        with self.access_lock:
            self._serial_port.close()

    @property
    def is_open(self) -> bool:
        """
        Flag indicating if the serial port is open.

        :return: `True` if the serial port is open, otherwise `False`
        """
        return self._serial_port.is_open

    def _write_text_unsafe(self, text: str):
        """
        Write text to the serial port. The text is encoded and terminated by
        the configured terminator.

        :param text: Text to send to the port.
        :raises SerialCommunicationIOError: when communication port is not opened
        """
        try:
            self._serial_port.write(
                text.encode(self.ENCODING, self.UNICODE_HANDLING)
                + self.config.terminator
            )
        except serial.SerialException as exc:
            raise SerialCommunicationIOError from exc

    def write_text(self, text: str):
        """
        Write text to the serial port. The text is encoded and terminated by
        the configured terminator.

        This method uses `self.access_lock` to ensure thread-safety.

        :param text: Text to send to the port.
        :raises SerialCommunicationIOError: when communication port is not opened
        """

        with self.access_lock:
            self._write_text_unsafe(text)

    def _read_text_unsafe(self) -> str:
        """
        Read one line of text from the serial port. The input buffer may
        hold additional data afterwards, since only one line is read.

        :return: String read from the serial port; `''` if there was nothing to read.
        :raises SerialCommunicationIOError: when communication port is not opened
        """

        try:
            return self._serial_port.readline().decode(self.ENCODING)
        except serial.SerialException as exc:
            raise SerialCommunicationIOError from exc

    def read_text(self) -> str:
        """
        Read one line of text from the serial port. The input buffer may
        hold additional data afterwards, since only one line is read.

        This method uses `self.access_lock` to ensure thread-safety.

        :return: String read from the serial port; `''` if there was nothing to read.
        :raises SerialCommunicationIOError: when communication port is not opened
        """

        with self.access_lock:
            decoded = self._read_text_unsafe()

        return decoded

    def _read_bytes_unsafe(self, size: int = 1) -> bytes:
        """
        Read the specified number of bytes from the serial port.
        The input buffer may hold additional data afterwards.

        :param size: number of bytes to read
        :return: Bytes read from the serial port; `b''` if there was nothing to read.
        :raises SerialCommunicationIOError: when communication port is not opened
        """

        try:
            return self._serial_port.read(size)
        except serial.SerialException as exc:
            raise SerialCommunicationIOError from exc

    def read_bytes(self, size: int = 1) -> bytes:
        """
        Read the specified number of bytes from the serial port.
        The input buffer may hold additional data afterwards.

        This method uses `self.access_lock` to ensure thread-safety.

        :param size: number of bytes to read
        :return: Bytes read from the serial port; `b''` if there was nothing to read.
        :raises SerialCommunicationIOError: when communication port is not opened
        """

        with self.access_lock:
            b = self._read_bytes_unsafe(size)
        return b

    def _write_bytes_unsafe(self, data: bytes) -> int:
        """
        Write bytes to the serial port.


        :param data: data to write to the serial port
        :return: number of bytes written
        :raises SerialCommunicationIOError: when communication port is not opened
        """

        try:
            return self._serial_port.write(data)
        except serial.SerialException as exc:
            raise SerialCommunicationIOError from exc

    def write_bytes(self, data: bytes) -> int:
        """
        Write bytes to the serial port.

        This method uses `self.access_lock` to ensure thread-safety.

        :param data: data to write to the serial port
        :return: number of bytes written
        :raises SerialCommunicationIOError: when communication port is not opened
        """

        with self.access_lock:
            n = self._write_bytes_unsafe(data)
        return n
