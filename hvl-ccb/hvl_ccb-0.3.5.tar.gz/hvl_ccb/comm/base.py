#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Module with base classes for communication protocols.
"""

from abc import ABC, abstractmethod
from threading import Lock

from ..configuration import ConfigurationMixin


class CommunicationProtocol(ConfigurationMixin, ABC):
    """
    Communication protocol abstract base class.

    Specifies the methods to implement for communication protocol, as well as
    implements some default settings and checks.
    """

    def __init__(self, config) -> None:
        """
        Constructor for CommunicationProtocol. Takes a configuration dict or
        configdataclass as single parameter.

        :param config: Configdataclass or dictionary to be used with the default
            config dataclass.
        """

        super().__init__(config)

        #: Access lock to use with context manager when
        #: accessing the communication protocol (thread safety)
        self.access_lock = Lock()

    @abstractmethod
    def open(self):
        """
        Open communication protocol
        """
        pass  # pragma: no cover

    @abstractmethod
    def close(self):
        """
        Close the communication protocol
        """
        pass  # pragma: no cover

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
