#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Tools for OPC testing
"""

from opcua import Server
from opcua.ua import NodeId, Variant


class DemoServer(Server):

    def __init__(self, namespace, cube_type: str, port: int = 4840, shelffile=None,
                 iserver=None):
        super().__init__(shelffile, iserver)

        self.set_endpoint(f'opc.tcp://0.0.0.0:{port}/freeopcua/server/')

        self._ns = namespace
        self._cube_type = cube_type

        self._root = self.get_objects_node().add_object(
            self._ns, 'Supercube {}'.format(self._cube_type)
        )

    def add_var(self, id, val, writable: bool):
        var = self._root.add_variable(
            NodeId(identifier=str(id),
                   namespaceidx=self._ns),
            str(id),
            Variant(val)
        )
        var.set_writable(writable)
        return var

    def set_var(self, id, val):
        self.get_node(
            NodeId(identifier=str(id),
                   namespaceidx=self._ns),
        ).set_value(Variant(val))

    def get_var(self, id):
        return self.get_node(
            NodeId(identifier=str(id),
                   namespaceidx=self._ns),
        ).get_value()
