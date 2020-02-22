from tracker_master.model.Message import Message

import threading
import time
import serial
import tracker_master.config as CFG

def parse(message_string):
    return Message(hw_id=int(message_string[0:6]),
                   _type=int(message_string[8]),
                   charge=float(message_string[9:13]))

class SlaveReaderThread(threading.Thread):

    def __init__(self, msg_queue):
        super(SlaveReaderThread, self).__init__()
        self.msg_queue = msg_queue
        self.is_running = True

    def run(self):
        with serial.Serial(CFG.slave_com_port(), CFG.slave_com_port_baudrate()) as ser:
            while True:
                self.msg_queue.put(parse(ser.readline().strip()))

    def stop_working(self):
        self.is_running = False

class ProducerThread(threading.Thread):
    def __init__(self, msg_queue):
        super(ProducerThread, self).__init__()
        self.msg_queue = msg_queue
        self.is_running = True

    def run(self):
        while self.is_running:
            if not self.msg_queue.full():
                message_str = '0000012212.34255'
                self.msg_queue.put(parse(message_str))

                message_str = '0000172212.34255'
                self.msg_queue.put(parse(message_str))

                message_str = '0000232212.34255'
                self.msg_queue.put(parse(message_str))

                time.sleep(2)
        return

    def stop_working(self):
        self.is_running = False