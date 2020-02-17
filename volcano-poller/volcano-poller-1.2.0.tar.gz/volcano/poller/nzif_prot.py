#!/usr/bin/python3

from . import nzif_ctx
from . import nzif_dev
from . import base_prot
from . import tools


class NzifProtocol(base_prot.BaseProtocol):
    def __init__(self, my_xml_node, comm_channel, proposed_name, parent_log):
        super().__init__(my_xml_node, comm_channel, nzif_ctx.NzifCtx(comm_channel), proposed_name, parent_log)

        for node in my_xml_node.findall('Device'):
            dev = nzif_dev.NzifDevice(node, tools.unique_name('meter_', lambda x: not self.find_device(x)), self.log())
            self.add_device(dev)
