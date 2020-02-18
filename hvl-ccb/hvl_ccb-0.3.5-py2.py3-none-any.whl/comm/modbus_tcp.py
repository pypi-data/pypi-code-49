#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Communication protocol for modbus TCP ports. Makes use of the
`pymodbus <https://pymodbus.readthedocs.io/en/latest/>`_ library.
"""

import logging
from typing import List, Union

from IPy import IP
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.exceptions import ConnectionException

from .base import CommunicationProtocol
from ..configuration import configdataclass


class ModbusTcpConnectionFailedException(ConnectionException):
    """
    Exception raised when the connection failed.
    """
    pass


@configdataclass
class ModbusTcpCommunicationConfig:
    """
    Configuration dataclass for :class:`ModbusTcpCommunication`.
    """

    #: Host is the IP address of the connected device.
    host: str

    #: Unit number to be used when connecting with Modbus/TCP. Typically this is used
    #: when connecting to a relay having Modbus/RTU-connected devices.
    unit: int

    #: TCP port
    port: int = 502

    def clean_values(self):
        # host, raises ValueError on its own if not suitable
        IP(self.host)


class ModbusTcpCommunication(CommunicationProtocol):
    """
    Implements the Communication Protocol for modbus TCP.
    """

    def __init__(self, configuration):
        """Constructor for modbus"""
        super().__init__(configuration)

        # create the modbus port specified in the configuration
        logging.debug(
            'Create ModbusTcpClient with host: "{}", Port: "{}", Unit: "{}"'.format(
                self.config.host,
                self.config.port,
                self.config.unit,
            )
        )
        self.client = ModbusTcpClient(
            self.config.host, port=self.config.port, unit=self.config.unit
        )

    @staticmethod
    def config_cls():
        return ModbusTcpCommunicationConfig

    def open(self) -> None:
        """
        Open the Modbus TCP connection.

        :raises ModbusTcpConnectionFailedException: if the connection fails.
        """

        # open the port
        logging.debug('Open Modbus TCP Port.')

        with self.access_lock:
            if not self.client.connect():
                raise ModbusTcpConnectionFailedException

    def close(self):
        """
        Close the Modbus TCP connection.
        """

        # close the port
        logging.debug('Close Modbus TCP Port.')

        with self.access_lock:
            self.client.close()

    def write_registers(self, address: int, values: Union[List[int], int]):
        """
        Write values from the specified address forward.

        :param address: address of the first register
        :param values: list with all values
        """

        logging.debug(
            'Write registers {address} with values {values}'.format(
                address=address,
                values=values,
            )
        )

        with self.access_lock:
            try:
                self.client.write_registers(address=address, values=values,
                                            unit=self.config.unit)
            except ConnectionException as e:
                raise ModbusTcpConnectionFailedException from e

    def read_holding_registers(self, address: int, count: int) -> List[int]:
        """
        Read specified number of register starting with given address and return
        the values from each register.

        :param address: address of the first register
        :param count: count of registers to read
        :return: list of `int` values
        """

        logging.debug(
            'Read holding registers {address} with count {count}.'.format(
                address=address,
                count=count,
            )
        )

        with self.access_lock:
            try:
                registers = self.client.read_holding_registers(
                    address=address,
                    count=count
                ).registers
            except ConnectionException as e:
                raise ModbusTcpConnectionFailedException from e

        logging.debug(
            'Returned holding registers {address}: {registers}'.format(
                address=address,
                registers=registers,
            )
        )

        return registers

    def read_input_registers(self, address: int, count: int) -> List[int]:
        """
        Read specified number of register starting with given address and return
        the values from each register in a list.

        :param address: address of the first register
        :param count: count of registers to read
        :return: list of `int` values
        """

        logging.debug(
            'Read input registers {address} with count {count}.'.format(
                address=address,
                count=count,
            )
        )

        with self.access_lock:
            try:
                registers = self.client.read_input_registers(
                    address=address,
                    count=count
                ).registers
            except ConnectionException as e:
                raise ModbusTcpConnectionFailedException from e

        logging.debug(
            'Returned input registers {address}: {registers}'.format(
                address=address,
                registers=registers,
            )
        )

        return registers
