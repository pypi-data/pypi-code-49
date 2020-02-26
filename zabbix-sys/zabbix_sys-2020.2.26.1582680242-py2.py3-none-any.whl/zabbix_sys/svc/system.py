
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

import sys
import psutil
import platform


# TODO: Refactoring
# TODO: Add debug messages
class System:

    def __init__(self, cfg, logger):
        self.cfg = cfg
        self.logger = logger
        self.platform = str(platform.system()).lower()

    def discovery_cpu(self):
        """
        :return: CPU Cores count
        """
        try:
            cpu_count = psutil.cpu_count()
        except Exception as err:
            self.logger.error(msg=err, exc_info=False)
            sys.exit(1)

        result = {"data": []}
        for i in range(cpu_count):
            result["data"].append({"_": "", "cpu_core": i, "platform": self.platform})

        self.logger.debug("system::discovery::cpu result: " + str(result))
        return result

    def discovery_fs(self):
        """
        :return: Filesystem mount points
        """
        try:
            fs = psutil.disk_partitions()
        except Exception as err:
            self.logger.error(msg=err, exc_info=False)
            sys.exit(1)

        result = {"data": []}

        for partition in fs:
            result['data'].append({
                "_": "",
                "fs_mount": str(partition.mountpoint),
                "fs_type": str(partition.fstype),
                "fs_device": str(partition.device),
                "platform": self.platform
            })
        self.logger.debug("system::discovery::fs result: " + str(result))
        return result

    def discovery_platform(self):
        """
        :return: Platform name ( linux | windows | osx | ...)
        """
        result = {"data": [{
            "_": "",
            "os_platform": self.platform,
        }]}

        self.logger.debug("system::discovery::platform result: " + str(result))
        return result
