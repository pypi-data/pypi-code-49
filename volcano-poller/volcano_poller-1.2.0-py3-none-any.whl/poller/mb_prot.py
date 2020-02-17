from . import mb_ctx
from . import mb_dev
from . import base_prot
from . import tools


class MbProtocol(base_prot.BaseProtocol):
    def __init__(self, my_xml_node, comm_channel, proposed_name, parent_log):
        super().__init__(my_xml_node, comm_channel, mb_ctx.MbCtx(comm_channel), proposed_name, parent_log)

        for node in my_xml_node.findall('Device'):
            dev = mb_dev.MbDevice(node, tools.unique_name('device_', lambda x: not self.find_device(x)), self.log())
            if not dev.empty():
                self.add_device(dev)
