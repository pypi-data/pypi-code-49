import threading
import time

import serial

import tracker_master.config as CFG
from tracker_master import util
from tracker_master.model.Message import Message


def parse(message_string):
    return Message(hw_id=int(message_string[0:6]),
                   _type=int(message_string[8]) + 1,    # Python Enum starts from 1
                   charge=float(message_string[9:13]))


class SlaveReaderThread(threading.Thread):

    def __init__(self, msg_queue):
        super(SlaveReaderThread, self).__init__()
        self.logger = util.get_com_port_logger()
        self.msg_queue = msg_queue
        self.is_running = True
        self.setDaemon(True)

    def run(self):
        with serial.Serial(CFG.slave_com_port(), CFG.slave_com_port_baudrate()) as ser:
            while self.is_running:
                msg = ser.readline().decode().strip()
                if not self.is_running:
                    return
                self.logger.info(msg)
                self.msg_queue.put(parse(msg))

    def stop_working(self):
        self.is_running = False


class VirtualSlaveReaderThread(threading.Thread):
    def __init__(self, msg_queue):
        super(VirtualSlaveReaderThread, self).__init__()
        self.logger = util.get_com_port_logger()
        self.msg_queue = msg_queue
        self.setDaemon(True)
        self.is_running = True

    def run(self):
        while self.is_running:
            if not self.msg_queue.full():
                message_str = '1012013012.77532'
                self.logger.info(message_str)
                self.msg_queue.put(parse(message_str))
                time.sleep(2)
        return

    def stop_working(self):
        self.is_running = False