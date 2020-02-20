
import re
import os
import platform
from utils.system import get_ip_address
from tool.device.library.nvme_cmd import ControllerDataStructure, NamespaceDataStructure, SmartHealth
from utils.system import get_root_path
from tool.device import NVME

class Environment(object):

    def __init__(self, dev="/dev/nvme0n1"):
        self.dev = dev
        self.dev_name, self.nsid = None, None
        self.nvme = self.get_nvme()

    def get_nvme(self):
        if self.get_operating_system() == "Windows":
            self.dev_name, self.nsid = self._get_windows_dev_name_nsid(self.dev)
            nvme = NVME(self.nsid)
        else:
            self.dev_name, self.nsid = self._get_linux_dev_name_nsid(self.dev)
            dev_index = self.get_linux_dev_index(self.dev_name)
            nvme = NVME(dev_index)
        return nvme

    @staticmethod
    def get_linux_dev_index(dev_name):
        ret = re.findall("nvme(\w+)", dev_name)
        dev_index = ret[0] if ret else 0
        return dev_index

    def get_environments(self):
        env_args = {
            "vendor": self.get_vendor(),
            "vendor_name": self.get_vendor_name(self.get_vendor()),
            "ip": self.get_ip_addr(),
            "operating_system": self.get_operating_system(),
            "capacity": self.get_capacity_unit_gb(),
            "dev_name": self.dev,
            "fw_version": self.get_fw_version()
        }
        return env_args

    def _get_windows_dev_name_nsid(self, dev):
        namespace_id = None
        rets = re.findall("Drive(\d+)", dev)
        if rets:
            namespace_id = rets[0]
        return dev, int(namespace_id)

    def _get_linux_dev_name_nsid(self, dev):
        dev_name, namespace_id = None, None
        rets = re.findall("([\w\/]+\d)n(\d)", dev)
        if rets:
            dev_name, namespace_id = rets[0]
        return dev_name, int(namespace_id)

    def get_vendor(self):
        cns = 1
        cntid = 0
        nsid = 1
        _, ctl_prp = self.nvme.identify(cns, cntid, nsid, ControllerDataStructure)
        ctl_identify = ctl_prp.convert(ControllerDataStructure)
        vid = ctl_identify.vid
        return vid

    @staticmethod
    def get_vendor_name(vendor_id):
        vendor_id = hex(int(vendor_id)).replace("0x", "")
        vendor_name = ""
        pci_ids_file = os.path.join(get_root_path(), "configuration", "pci.ids")
        with open(pci_ids_file, encoding='UTF-8') as pci_file:
            while True:
                line = pci_file.readline()
                if line:
                    if not line.startswith("\t"):
                        if vendor_id.lower() in line.lower():
                            vendor_name = line.split(vendor_id)[1].strip()
                            break
                else:
                    break
        return vendor_name

    def get_fw_version(self):
        cns = 1
        cntid = 0
        nsid = 1
        _, ctl_prp = self.nvme.identify(cns, cntid, nsid, ControllerDataStructure)
        version = ctl_prp.ascii_to_string(64, 8)
        return version

    def get_ip_addr(self):
        ip_addr = get_ip_address()
        return ip_addr

    def get_operating_system(self):
        system = "Windows" if platform.system() == 'Windows' else "Linux"
        return system

    def get_capacity_unit_gb(self):
        _, ns_identify_prp = self.nvme.identify(0x11, 0, 1, NamespaceDataStructure)
        ns_identify = ns_identify_prp.convert(NamespaceDataStructure)
        namespace_size = ns_identify.ns
        formatted_lba_size = ns_identify.flbaf & 0x7
        lba_data_size = ns_identify.lbaf[int(formatted_lba_size)].lbads
        lba_size = 2**(int(lba_data_size))
        size = (namespace_size*lba_size)/1024/1024/1024
        print("ssd size:", size)
        return size

    def get_temperature(self):
        _, prp = self.nvme.getlog(lid=0x2, nsid=self.nsid, numdu=128)
        smart_health = prp.convert(SmartHealth)
        print(smart_health.ct)
        return float('%.2f' % (smart_health.ct-273.15))

    def get_ns_identify(self):
        pass

    def get_log_page(self):
        pass

    def get_project(self):
        pass
