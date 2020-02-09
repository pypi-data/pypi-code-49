"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with the same space disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
from subprocess import Popen, CalledProcessError
from . import const

DEVICE = const.DEVICE


class umount:
    def __init__(self, dict_blkid, log):
        self.b = dict_blkid
        self.log = log
        self.__umount()

    def __umount(self):
        """
        Umount disks
        """
        self.log.add_log(const.TTY_UMOUNT % (self.b.master[DEVICE],
                                             self.b.slave[DEVICE]))
        x = 'sudo umount %s'
        try:
            # 18.11.2019
            # This is crap... i have to do a forloop for all device to umout
            # But i commit on git today a major bug fix of dd
            xx = x % (self.b.master[DEVICE])
            cmd_list = ['sudo', 'umount', self.b.master[DEVICE] + '1']
            cmd = Popen(cmd_list)
            cmd.wait()
            xx = x % (self.b.slave[DEVICE])
            cmd_list = ['sudo', 'umount', self.b.slave[DEVICE] + '1']
            cmd = Popen(cmd_list)
            cmd.wait()
        except CalledProcessError:
            self.log.add_log(const.ERR_UMOUNT)
            self.log.add_log(const.ERR_CMD % (xx))
