# Imports
import time
import queue
from threading import Thread
# Local imports
from .transporter import Transport

class Communicator(Thread):

    def __init__(self, uarm, port, addr):
        Thread.__init__(self)
        self.interrupted = False
        self.daemon = True
        self.setName("uARM_Comm")
        self.uarm = uarm
        self.transport = Transport()
        self.transport.init(port, addr)
        self.command_queue = queue.Queue()

    def subscribeLoop(self):
        while not self.is_interrupted():
            try:
                self.parse_update(self.transport.receive())
            except IOError:
                print("[uarm_serial] - Parser failed.")
                self.interrupted = True
                raise

    def publishLoop(self):
        while not self.is_interrupted():
            try:
                self.sendAll()
                time.sleep(1) # TODO: is needed?
            except IOError:
                print("[uarm_serial] - Parser failed.")
                self.interrupted = True
                raise

    def parse_update(self, message):
        if message == "":
            return

        op = int(message)

        if op == 0: # Idle
            self.uarm.set_idle()
        elif op == 1: # Running
            self.uarm.set_running()
        else:
            print("[uarm_serial] - Unknown command.")

    def is_interrupted(self):
        return self.interrupted

    def set_interrupted(self, interrupted):
        self.interrupted = interrupted

    """
    Add a message to the queue for transmission
    """
    def send(self, message):
        self.command_queue.put(message)

    def sendAll(self):
        while not self.command_queue.empty():
            self.transport.send(self.command_queue.get())
