#!/usr/bin/env python3
"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with the same space disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>

    This file copy disk to disk
    Need to be run by root user
"""
import os
from subprocess import CalledProcessError
import yaml
from .backup_system import backup_system
from .blkid import blkid
from .dd import dd
from .e2label import e2label
from .gui import gui
from .print_log import print_log
from .kill_dd import kill_dd
from .umount import umount
from . import const


class usb2usb:
    def __init__(self, config_file):
        # Loading Yaml
        try:
            self.bs = backup_system(config_file)
        except yaml.YAMLError:
            exit()

    def backup(self):
        """
        Run backup copy master to img, img to slave for root user
        """
        # Log file
        LOG = self.bs.data[const.YML_TEMP_LOG]

        # Log remove
        try:
            os.remove(LOG)
        except FileNotFoundError:
            pass
        # Log touch
        try:
            log = open(LOG, 'w')
            log.write('')
        except IOError:
            pass
        # Log init
        log = print_log(LOG)
        # Log add
        log.add_log(const.TTY_INTRO)
        log.add_log('')
        log.add_log(const.TTY_YML_SUCCESS)
        log.add_log('')
        log.add_log(const.TTY_YML_VARIABLES_USED)
        for key in self.bs.data:
            log.add_log(const.TTY_YML_VARIABLE % (key, self.bs.data[key]))

        # If same UUID and same label, failed
        UUID_1_MASTER = self.bs.data[const.YML_UUID_1_MASTER]
        UUID_1_SLAVE = self.bs.data[const.YML_UUID_1_SLAVE]
        try:
            b = blkid(UUID_1_MASTER, UUID_1_SLAVE, log)
        except CalledProcessError as error:
            log.add_log(error)
            exit()
        except Exception:
            exit()
        log.add_log('')
        log.add_log(const.TTY_MASTER % (b.master))
        log.add_log(const.TTY_SLAVE % (b.slave))
        log.add_log('')

        try:
            # Umount drivers
            umount(b, log)
            if self.bs.data[const.YML_KILL_DD]:
                # Kill all dd on the system
                k = kill_dd(log)
                k.run()
                log.add_log('')
            # Init dd
            d = dd(b, self.bs.data[const.YML_TEMP_IMG], log)
            # dd master to img
            d.copy_master_to_img()
            # dd img to slave
            d.copy_img_to_slave()
            # Init e2label
            e = e2label(b, log)
            # Write label
            e.write_time_stamp_label_to_master()
            log.add_log('')
            # Umount drivers
            umount(b, log)
            # All ok
            log.add_log(const.TTY_ALL_OK)
            log.add_log('')
        except IOError as error:
            log.add_log(error)
            exit()
        except CalledProcessError as error:
            log.add_log(error)
            exit()

    def gui(self):
        """
        Run gui for non root user
        """
        g = gui(self.bs.data[const.YML_TEMP_LOG],
                const.SERVICE)
        g.run()
