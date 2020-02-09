"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with the same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import re
from subprocess import Popen, PIPE, STDOUT, CalledProcessError
from . import const

UUID = const.UUID
DEVICE = const.DEVICE
PARTITION = const.PARTITION
LABEL = const.LABEL


class blkid:
    def __init__(self, uuid_1_master, uuid_1_slave, log):
        self.master = {}
        self.slave = {}
        self.master[UUID] = uuid_1_master
        self.slave[UUID] = uuid_1_slave
        self.log = log
        self.__compute()

    def __compute(self):
        """
        This method:
            - Execute "sudo blkid"
            - Create a dict, and another one with 2 dimensions, and another one
              with the list of detected device(s)
            - Print in the console the list of available device(s)
        """
        global BLKIDOUTPUT
        x = 'sudo blkid'
        try:
            cmd = Popen(x, stdout=PIPE, stderr=STDOUT, shell=True)
        except CalledProcessError:
            self.log.add_log(const.ERR_BLKID_COMPUTE)
        BLKIDOUTPUT = cmd.communicate()[0]
        array = str(BLKIDOUTPUT.decode('UTF-8')).split('\n')
        blkid_list = []
        for i, a in enumerate(array):
            # Create dict only if device detected
            pattern = r'\/dev\/sd([a-z]+)'
            if not re.search(pattern, a) is None:
                for f in re.findall(pattern, a):
                    blkid_list.append(i)
                    blkid_list[i] = {}
                    blkid_list[i][DEVICE] = '/dev/sd' + f
            else:
                continue
            pattern = r'\/dev\/sd([a-z][0-9]+)'
            if not re.search(pattern, a) is None:
                for f in re.findall(pattern, a):
                    blkid_list[i][PARTITION] = '/dev/sd' + f
            else:
                blkid_list[i][PARTITION] = None
            pattern = '(?<= UUID=")([^"]*)'
            if not re.search(pattern, a) is None:
                for f in re.findall(pattern, a):
                    blkid_list[i][UUID] = f
            else:
                blkid_list[i][UUID] = None
            pattern = '(?<=LABEL=")([^"]*)'
            if not re.search(pattern, a) is None:
                for f in re.findall(pattern, a):
                    blkid_list[i][LABEL] = f
            else:
                blkid_list[i][LABEL] = None
        # Array 2 dimenssions with dict
        blkid_l_g = []
        i = -1
        for b in blkid_list:
            if i > 0:
                if blkid_l_g[i][DEVICE] == b[DEVICE]:
                    j = len(blkid_l_g[i]) + 1
                    blkid_l_g[i][j] = {}
                    blkid_l_g[i][j][PARTITION] = b[PARTITION]
                    blkid_l_g[i][j][UUID] = b[UUID]
                    blkid_l_g[i][j][LABEL] = b[LABEL]
                    continue
            i += 1
            blkid_l_g.append(i)
            blkid_l_g[i] = {}
            blkid_l_g[i][DEVICE] = b[DEVICE]
            blkid_l_g[i][0] = {}
            blkid_l_g[i][0][PARTITION] = b[PARTITION]
            blkid_l_g[i][0][UUID] = b[UUID]
            blkid_l_g[i][0][LABEL] = b[LABEL]
        self.log.add_log('')
        self.log.add_log(const.TTY_BLKID_DEVICE_LIST)
        for b in blkid_l_g:
            self.log.add_log(str(b))
        self.log.add_log('')
        # Remove if no UUID matches with the variable in config.yml on first
        # number of UUID array (occurs 0 in py, or occurs 1 in the terminal
        # with sudo blkid)
        i = 0
        blkid_match = []
        for b in blkid_l_g:
            if b[0][UUID] == self.master[UUID] or \
               b[0][UUID] == self.slave[UUID]:
                blkid_match.append(i)
                blkid_match[i] = {}
                blkid_match[i][DEVICE] = b[DEVICE]
                blkid_match[i][UUID] = b[0][UUID]
                blkid_match[i][LABEL] = b[0][LABEL]
                i += 1
        self.log.add_log(const.TTY_BLKID_DEVICE_LIST_MATCH % (i))
        for b in blkid_match:
            self.log.add_log(str(b))
        self.log.add_log('')
        try:
            if i != 2:
                raise Exception(const.ERR_COUNT)
        except Exception as error:
            self.log.add_log(error)
            self.log.add_log(const.ERR_BLKID_NO_OPERATION_IF % (i))
            exit()
        # Detect master and slave
        try:
            if self.master[UUID] == self.slave[UUID]:
                if blkid_match[0][LABEL] == blkid_match[1][LABEL]:
                    raise Exception(const.ERR_SAME_LABEL)
                for i in range(0, 1):
                    if len(blkid_match[i][LABEL]) != len(const.YYYYMMDDHHMMSS):
                        raise Exception(const.ERR_UNKNOW_LABEL)
                if int(blkid_match[0][LABEL]) > int(blkid_match[1][LABEL]):
                    self.master[DEVICE] = blkid_match[0][DEVICE]  # + '1'
                    self.master[LABEL] = blkid_match[0][LABEL]
                    self.slave[DEVICE] = blkid_match[1][DEVICE]  # + '1'
                    self.slave[LABEL] = blkid_match[1][LABEL]
                else:
                    self.master[DEVICE] = blkid_match[1][DEVICE]  # + '1'
                    self.master[LABEL] = blkid_match[1][LABEL]
                    self.slave[DEVICE] = blkid_match[0][DEVICE]  # + '1'
                    self.slave[LABEL] = blkid_match[0][LABEL]
            else:
                for i in range(0, 1):
                    if self.master[UUID] == blkid_match[i][UUID]:
                        self.master[DEVICE] = blkid_match[i][DEVICE]  # + '1'
                        self.master[LABEL] = blkid_match[i][LABEL]
                    if self.slave[UUID] == blkid_match[i][UUID]:
                        self.slave[DEVICE] = blkid_match[i][DEVICE]  # + '1'
                        self.slave[LABEL] = blkid_match[i][LABEL]
        except Exception as error:
            self.log.add_log(error)
            exit()
