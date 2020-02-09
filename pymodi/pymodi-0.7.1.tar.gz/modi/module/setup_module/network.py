"""Network module."""

from enum import Enum

from modi.module.setup_module.setup_module import SetupModule


class Network(SetupModule):
    class PropertyType(Enum):
        RESERVED = 0

    def __init__(self, id_, uuid, serial_write_q):
        super(Network, self).__init__(id_, uuid, serial_write_q)
        self._type = "network"
