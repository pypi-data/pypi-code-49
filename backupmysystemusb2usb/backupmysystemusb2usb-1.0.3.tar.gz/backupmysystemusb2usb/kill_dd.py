"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with the same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
from subprocess import Popen, CalledProcessError
from . import const


class kill_dd:
    def __init__(self, log):
        self.log = log

    def run(self):
        """
        Run sudo killall -9 dd
        """
        x = ['sudo', 'killall', '-9', 'dd']
        try:
            cmd_list = x
            cmd = Popen(cmd_list)
            cmd.wait()
        except CalledProcessError:
            self.log.add_log(const.ERR_KILL_DD)
