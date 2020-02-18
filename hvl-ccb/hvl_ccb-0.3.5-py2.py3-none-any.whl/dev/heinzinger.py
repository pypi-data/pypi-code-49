#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Device classes for Heinzinger Digital Interface I/II and Heinzinger PNC power supply.

The Heinzinger Digital Interface I/II is used for many Heinzinger power units.
Manufacturer homepage:
https://www.heinzinger.com/products/accessories-and-more/digital-interfaces/

The Heinzinger PNC series is a series of high voltage direct current power supplies.
The class HeinzingerPNC is tested with two PNChp 60000-1neg and a PNChp 1500-1neg.
Check the code carefully before using it with other PNC devices, especially PNC3p
or PNCcap.
Manufacturer homepage:
https://www.heinzinger.com/products/high-voltage/universal-high-voltage-power-supplies/
"""

import logging
import re
from abc import ABC, abstractmethod
from enum import IntEnum
from time import sleep
from typing import Union

from .base import SingleCommDevice
from ..comm import SerialCommunication, SerialCommunicationConfig
from ..comm.serial import (
    SerialCommunicationParity,
    SerialCommunicationStopbits,
    SerialCommunicationBytesize,
)
from ..configuration import configdataclass
from ..utils.enum import AutoNumberNameEnum

Number = Union[int, float]


@configdataclass
class HeinzingerSerialCommunicationConfig(SerialCommunicationConfig):
    #: Baudrate for Heinzinger power supplies is 9600 baud
    baudrate: int = 9600

    #: Heinzinger does not use parity
    parity: Union[str, SerialCommunicationParity] = SerialCommunicationParity.NONE

    #: Heinzinger uses one stop bit
    stopbits: Union[int, SerialCommunicationStopbits] = SerialCommunicationStopbits.ONE

    #: One byte is eight bits long
    bytesize: Union[
        int, SerialCommunicationBytesize
    ] = SerialCommunicationBytesize.EIGHTBITS

    #: The terminator is LF
    terminator: bytes = b"\n"

    #: use 3 seconds timeout as default
    timeout: Number = 3

    #: time to wait between attempts of reading a non-empty text
    wait_sec_read_text_nonempty: Number = 0.5

    def clean_values(self):
        super().clean_values()

        if self.wait_sec_read_text_nonempty <= 0:
            raise ValueError(
                "Wait time between attempts to read a non-empty text must be be a "
                "positive value (in seconds)."
            )


class HeinzingerSerialCommunication(SerialCommunication):
    """
    Specific communication protocol implementation for
    Heinzinger power supplies.
    Already predefines device-specific protocol parameters in config.
    """

    @staticmethod
    def config_cls():
        return HeinzingerSerialCommunicationConfig

    def read_text_nonempty(self, n_attempts_max: int = 40,) -> str:
        """
        Reads from the serial port, until a non-empty line is found, or the number of
        attempts is exceeded.

        :param n_attempts_max: maximum number of read attempts
        :param attempt_interval_sec: interval between subsequent attempts in seconds
        :return: String read from the serial port; `''` if number of attempts is
            exceeded or serial port is not opened.
        """
        answer = self.read_text().strip()
        n_attempts_left = n_attempts_max if self.is_open else 0
        attempt_interval_sec = self.config.wait_sec_read_text_nonempty
        while len(answer) == 0 and n_attempts_left > 0:
            sleep(attempt_interval_sec)
            answer = self.read_text().strip()
            n_attempts_left -= 1
        return answer


@configdataclass
class HeinzingerConfig:
    """
    Device configuration dataclass for Heinzinger power supplies.
    """

    class RecordingsEnum(IntEnum):
        ONE = 1
        TWO = 2
        FOUR = 4
        EIGHT = 8
        SIXTEEN = 16

    #: default number of recordings used in averaging the current
    #  or the voltage [1, 2, 4, 8, 16]
    default_number_of_recordings: Union[int, RecordingsEnum] = 1

    #: number of decimals sent for setting the current limit or the voltage, between 1
    #  and 10
    number_of_decimals: int = 6

    #: Time to wait after subsequent commands during stop (in seconds)
    wait_sec_stop_commands: Number = 0.5

    def clean_values(self):
        if not isinstance(self.default_number_of_recordings, self.RecordingsEnum):
            self.force_value(
                "default_number_of_recordings",
                self.RecordingsEnum(self.default_number_of_recordings),
            )

        if self.number_of_decimals not in range(1, 11):
            raise ValueError(
                "The number of decimals should be " "an integer between 1 and 10."
            )

        if self.wait_sec_stop_commands <= 0:
            raise ValueError(
                "Wait time after subsequent commands during stop must be be a "
                "positive value (in seconds)."
            )


class HeinzingerDI(SingleCommDevice, ABC):
    """
    Heinzinger Digital Interface I/II device class

    Sends basic SCPI commands and reads the answer.
    Only the standard instruction set from the manual is implemented.
    """

    def __init__(self, com, dev_config=None):

        # Call superclass constructor
        super().__init__(com, dev_config)

        # Version of the interface (will be retrieved after com is opened)
        self._interface_version = ""

    def __repr__(self):
        return f"HeinzingerDI({self._interface_version})"

    @staticmethod
    def default_com_cls():
        return HeinzingerSerialCommunication

    @staticmethod
    def config_cls():
        return HeinzingerConfig

    @abstractmethod
    def start(self):
        """
        Opens the communication protocol.

        :raises SerialCommunicationIOError: when communication port cannot be opened.
        """

        logging.info("Starting device " + str(self))
        super().start()

        self._interface_version = self.get_interface_version()

    def stop(self) -> None:
        """
        Stop the device. Closes also the communication protocol.
        """

        logging.info("Stopping device " + str(self))
        self.set_voltage(0)
        sleep(self.config.wait_sec_stop_commands)
        self.output_off()
        sleep(self.config.wait_sec_stop_commands)
        super().stop()

    def reset_interface(self) -> None:
        """
        Reset of the digital interface; only Digital Interface I:
        Power supply is switched to the Local-Mode (Manual operation)

        :raises SerialCommunicationIOError: when communication port is not opened
        """
        self.com.write_text("*RST")

    def get_interface_version(self) -> str:
        """
        Queries the version number of the digital interface.

        :raises SerialCommunicationIOError: when communication port is not opened
        """
        self.com.write_text("VERS?")
        return self.com.read_text_nonempty()

    def get_serial_number(self) -> str:
        """
        Ask the device for its serial number and returns the answer as a string.

        :return: string containing the device serial number
        :raises SerialCommunicationIOError: when communication port is not opened
        """
        self.com.write_text("*IDN?")
        return self.com.read_text_nonempty()

    def output_on(self) -> None:
        """
        Switch DC voltage output on.

        :raises SerialCommunicationIOError: when communication port is not opened
        """
        self.com.write_text("OUTP ON")

    def output_off(self) -> None:
        """
        Switch DC voltage output off.

        :raises SerialCommunicationIOError: when communication port is not opened
        """
        self.com.write_text("OUTP OFF")

    def get_number_of_recordings(self) -> int:
        """
        Queries the number of recordings the device is using for average value
        calculation.

        :return: int number of recordings
        :raises SerialCommunicationIOError: when communication port is not opened
        """
        self.com.write_text("AVER?")
        answer = self.com.read_text_nonempty()
        return int(answer)

    def set_number_of_recordings(
        self, value: Union[int, HeinzingerConfig.RecordingsEnum],
    ) -> None:
        """
        Sets the number of recordings the device is using for average value
        calculation. The possible values are 1, 2, 4, 8 and 16.

        :raises SerialCommunicationIOError: when communication port is not opened
        """
        value = self.config.RecordingsEnum(value).value
        self.com.write_text(f"AVER {value}")

    def measure_voltage(self) -> float:
        """
        Ask the Device to measure its output voltage and return the measurement result.

        :return: measured voltage as float
        :raises SerialCommunicationIOError: when communication port is not opened
        """
        self.com.write_text("MEAS:VOLT?")
        answer = self.com.read_text_nonempty()
        return float(answer)

    def set_voltage(self, value: Union[int, float]) -> None:
        """
        Sets the output voltage of the Heinzinger PNC to the given value.

        :param value: voltage expressed in `self.unit_voltage`
        :raises SerialCommunicationIOError: when communication port is not opened
        """

        self.com.write_text(
            f"VOLT {{:.{self.config.number_of_decimals}f}}".format(value)
        )

    def get_voltage(self) -> float:
        """
        Queries the set voltage of the Heinzinger PNC (not the measured voltage!).

        :raises SerialCommunicationIOError: when communication port is not opened
        """
        self.com.write_text("VOLT?")
        answer = self.com.read_text_nonempty()
        return float(answer)

    def measure_current(self) -> float:
        """
        Ask the Device to measure its output current and return the measurement result.

        :return: measured current as float
        :raises SerialCommunicationIOError: when communication port is not opened
        """
        self.com.write_text("MEAS:CURR?")
        answer = self.com.read_text_nonempty()
        return float(answer)

    def set_current(self, value: Union[int, float]) -> None:
        """
        Sets the output current of the Heinzinger PNC to the given value.

        :param value: current expressed in `self.unit_current`
        :raises SerialCommunicationIOError: when communication port is not opened
        """

        self.com.write_text(
            f"CURR {{:.{self.config.number_of_decimals}f}}".format(value)
        )

    def get_current(self) -> float:
        """
        Queries the set current of the Heinzinger PNC (not the measured current!).

        :raises SerialCommunicationIOError: when communication port is not opened
        """
        self.com.write_text("CURR?")
        answer = self.com.read_text_nonempty()
        return float(answer)


class HeinzingerPNC(HeinzingerDI):
    """
    Heinzinger PNC power supply device class.

    The power supply is controlled over a Heinzinger Digital Interface I/II
    """

    class UnitCurrent(AutoNumberNameEnum):
        UNKNOWN = ()
        mA = ()
        A = ()

    class UnitVoltage(AutoNumberNameEnum):
        UNKNOWN = ()
        V = ()
        kV = ()

    def __init__(self, com, dev_config=None):

        # Call superclass constructor
        super().__init__(com, dev_config)

        # Serial number of the device (will be retrieved after com is opened)
        self._serial_number = ""
        # model of the device (derived from serial number)
        self._model = ""
        # maximum output current of the hardware (unit mA or A, depending on model)
        self._max_current_hardware = 0
        # maximum output voltage of the hardware (unit V or kV, depending on model)
        self._max_voltage_hardware = 0
        # maximum output current set by user (unit mA or A, depending on model)
        self._max_current = 0
        # maximum output voltage set by user (unit V or kV, depending on model)
        self._max_voltage = 0
        # current unit: 'mA' or 'A', depending on model
        self._unit_current = self.UnitCurrent.UNKNOWN
        # voltage unit: 'V' or 'kV', depending on model
        self._unit_voltage = self.UnitVoltage.UNKNOWN

    def __repr__(self):
        return (
            f"HeinzingerPNC({self._serial_number}), with "
            f"HeinzingerDI({self._interface_version})"
        )

    @property
    def max_current_hardware(self) -> Union[int, float]:
        return self._max_current_hardware

    @property
    def max_voltage_hardware(self) -> Union[int, float]:
        return self._max_voltage_hardware

    @property
    def unit_voltage(self) -> UnitVoltage:  # noqa: F821
        return self._unit_voltage

    @property
    def unit_current(self) -> UnitCurrent:  # noqa: F821
        return self._unit_current

    @property
    def max_current(self) -> Union[int, float]:
        return self._max_current

    @max_current.setter
    def max_current(self, value: Union[int, float]):
        if not 0 <= value <= self._max_current_hardware:
            raise ValueError(
                "max_current must positive " "and below max_current_hardware."
            )
        self._max_current = value

    @property
    def max_voltage(self) -> Union[int, float]:
        return self._max_voltage

    @max_voltage.setter
    def max_voltage(self, value: Union[int, float]):
        if not 0 <= value <= self._max_voltage_hardware:
            raise ValueError(
                "max_voltage must be positive " "and below max_voltage_hardware."
            )
        self._max_voltage = value

    def start(self) -> None:
        """
        Opens the communication protocol and configures the device.
        """

        # starting Heinzinger Digital Interface
        super().start()

        logging.info("Starting device " + str(self))

        # find out which type of source this is:
        self.identify_device()
        self.set_number_of_recordings(self.config.default_number_of_recordings)

    def identify_device(self) -> None:
        """
        Identify the device nominal voltage and current based on its serial number.

        :raises SerialCommunicationIOError: when communication port is not opened
        """
        serial_number = self.get_serial_number()
        # regex to find the model of the device
        regex_vc = r"(\d+)-(\d+)"  # voltage-current info
        regex_model = r"PNC.*?" + regex_vc + r"\s?[a-z]{3}"
        result = re.search(regex_model, serial_number)
        if result:
            self._serial_number = serial_number
            model = result.group()
            self._model = model
            # regex to find the nominal voltage and nominal current
            match = re.search(regex_vc, model)
            assert match  # already matched in regex_model expression
            voltage = int(match.group(1))
            current = int(match.group(2))
            # identifying the units to use for voltage and current
            if voltage < 100000:
                self._unit_voltage = self.UnitVoltage.V
                self._max_voltage_hardware = voltage
                self._max_voltage = voltage
            else:
                self._unit_voltage = self.UnitVoltage.kV
                self._max_voltage_hardware = int(voltage / 1000)
                self._max_voltage = int(voltage / 1000)
            if current < 1000:
                self._unit_current = self.UnitCurrent.mA
                self._max_current_hardware = current
                self._max_current = current
            else:
                self._unit_current = self.UnitCurrent.A
                self._max_current_hardware = int(current / 1000)
                self._max_current = int(current / 1000)
            logging.info(f"Device {model} successfully identified")
        else:
            raise HeinzingerPNCDeviceNotRecognizedException(serial_number)

    def set_voltage(self, value: Union[int, float]) -> None:
        """
        Sets the output voltage of the Heinzinger PNC to the given value.

        :param value: voltage expressed in `self.unit_voltage`
        :raises SerialCommunicationIOError: when communication port is not opened
        """
        if value > self.max_voltage:
            raise HeinzingerPNCMaxVoltageExceededException
        elif value < 0:
            raise ValueError("voltage must be positive")

        super().set_voltage(value)

    def set_current(self, value: Union[int, float]) -> None:
        """
        Sets the output current of the Heinzinger PNC to the given value.

        :param value: current expressed in `self.unit_current`
        :raises SerialCommunicationIOError: when communication port is not opened
        """
        if value > self.max_current:
            raise HeinzingerPNCMaxCurrentExceededException
        elif value < 0:
            raise ValueError("current must be positive")

        super().set_current(value)


class HeinzingerPNCError(Exception):
    """
    General error with the Heinzinger PNC voltage source.
    """

    pass


class HeinzingerPNCMaxVoltageExceededException(HeinzingerPNCError):
    """
    Error indicating that program attempted to set the voltage
    to a value exceeding 'max_voltage'.
    """

    pass


class HeinzingerPNCMaxCurrentExceededException(HeinzingerPNCError):
    """
    Error indicating that program attempted to set the current
    to a value exceeding 'max_current'.
    """

    pass


class HeinzingerPNCDeviceNotRecognizedException(HeinzingerPNCError):
    """
    Error indicating that the serial number of the device
    is not recognized.
    """

    pass
