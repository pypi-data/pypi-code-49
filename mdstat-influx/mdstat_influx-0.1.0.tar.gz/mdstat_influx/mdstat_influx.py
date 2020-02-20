#! /usr/bin/env python3

import os
import platform
import mdstat

class MdDevice:

    def line_message(self):
        """ returns a formatted line message """
        tags = {
            "device_name": self.name,
            "raid_type": self.personality,
            "hostname": platform.node(),
        }

        disks = len(self.disks)
        faulty = self.faulty_disk_cnt()

        fields = {
            "disks": "{}i".format(disks),
            "faulty_disks": "{}i".format(faulty),
            "replacement_disks": "{}i".format(self.replacement_disk_cnt()),
            "spare_disks": "{}i".format(self.spare_disk_cnt()),
            "faulty_pct": float(faulty) / float(disks),
        }

        return "mdstat,{all_tags} {all_fields}".format(
            all_tags=",".join(["{}={}".format(k,v) for k,v in tags.items()]),
            all_fields=",".join(["{}={}".format(k,v) for k,v in fields.items()]),
        )

    def __disk_type_cnt(self, disk_type):
        """ counts the number of disks with a positive value """
        return sum(map(lambda x: int(x[1].get(disk_type, False)), self.disks.items()))

    def faulty_disk_cnt(self):
        """ number of faulty devices """
        return self.__disk_type_cnt("faulty")

    def replacement_disk_cnt(self):
        """ number of replacement devices """
        return self.__disk_type_cnt("replacement")

    def spare_disk_cnt(self):
        """ number of spare devices """
        return self.__disk_type_cnt("spare")

    def __init__(self, device_name, device_info):
        self.name = device_name
        self.active = device_info.get('active', False)
        self.personality = device_info.get('personality', None)
        self.disks = device_info.get('disks', {})
        self.read_only = device_info.get('read_only', False)


class MdData:

    def get_messages(self):
        """ get line messages for all devices """
        return os.linesep.join(map(lambda x: x.line_message(), self.devices))

    def __init__(self, md_data=None):

        if md_data:
            md = md_data
        else:
            md = mdstat.parse()

        self.personalities = set(md.get('personalities', []))
        self.unused_devices = md.get('unused_devices', [])

        self.devices = [MdDevice(k, v) for k, v in md.get('devices', {}).items()]

