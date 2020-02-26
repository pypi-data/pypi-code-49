import struct
from threading import Thread
from typing import List, Optional

import serial

from gbrpi.constants.rs232 import BAUD_RATE, DEFAULT_ALGO, DOUBLE_SIZE


class RS232:

    def __init__(self, dev_name: str, algo_list: List[str]):
        self.conn: serial.Serial = serial.Serial(dev_name, baudrate=BAUD_RATE)
        self.algo: str = DEFAULT_ALGO
        self.latest_data: Optional[List[int]] = None
        self.algo_list: List[str] = algo_list
        self.handler_map = {
            0: (self.ping_handler, 0),
            1: (self.get_handler, 0),
            2: (self.set_algo_handler, 1)
        }
        self.handler_thread: Optional[Thread] = None

    def send_success(self):
        self.conn.write(bytes("\x01", encoding="ascii"))

    def send_fail(self):
        self.conn.write(bytes("\x00", encoding="ascii"))

    def start_handler_thread(self):
        self.handler_thread = Thread(target=self.handler)
        self.handler_thread.setName("RS232Listenerd")
        self.handler_thread.setDaemon(True)
        self.handler_thread.start()
        print("Started listener")

    def handler(self):
        while True:
            req = self.conn.read(1)[0]
            if req in self.handler_map:
                curr_handler = self.handler_map[req]
                if curr_handler[1] != 0:
                    data = self.conn.read(curr_handler[1])
                else:
                    data = bytes()
                curr_handler[0](data)

    def ping_handler(self, data: bytes):
        self.send_success()

    def set_algo_handler(self, data: bytes):
        algo_index: int = data[0]
        if algo_index >= len(self.algo_list):
            self.send_fail()
            return
        self.algo = self.algo_list[algo_index]
        self.send_success()

    def get_handler(self, data: bytes):
        if self.latest_data is None or type(self.latest_data) != type([]) or len(self.latest_data) != 3:
            self.conn.write(bytes("\x00" * (1 + DOUBLE_SIZE * 3), encoding="ascii"))
            return
        self.send_success()
        for coord in self.latest_data:
            self.conn.write(bytearray(struct.pack(">d", coord)))
