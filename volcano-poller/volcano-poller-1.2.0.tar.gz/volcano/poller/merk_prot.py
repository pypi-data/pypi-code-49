#!/usr/bin/python3

from . import merk_ctx
from . import merk_dev
from . import base_prot
from . import tools


class MerkProtocol(base_prot.BaseProtocol):
    def __init__(self, my_xml_node, comm_channel, proposed_name, parent_log):
        super().__init__(my_xml_node, comm_channel, merk_ctx.MerkCtx(comm_channel), proposed_name, parent_log)

        for node in my_xml_node.findall('Device'):
            dev = merk_dev.MerkDevice(node, tools.unique_name('meter_', lambda x: not self.find_device(x)), self.log())
            self.add_device(dev)
