import threading
import time

from tracker_master.app_master.master import SlavesConfigurer
from tracker_master.app_master.notifier import Notifier


class ConfigurerConsumer(threading.Thread):

    def __init__(self, msg_queue, device_manager):
        assert isinstance(device_manager, SlavesConfigurer)
        super(ConfigurerConsumer, self).__init__()
        self.msg_queue = msg_queue
        self.device_manager = device_manager
        self.is_running = True
        return

    def run(self):
        while self.is_running:
            if not self.msg_queue.empty():
                self.device_manager.register_slave(self.msg_queue.get())
                time.sleep(1)
        return

    def stop_working(self):
        self.is_running = False


class MainConsumer(threading.Thread):

    def __init__(self, msg_queue, tracker_master):
        super(MainConsumer, self).__init__()
        assert isinstance(tracker_master, Notifier)
        self.msg_queue = msg_queue
        self.tracker_master = tracker_master
        self.is_running = True
        return

    def run(self):
        while self.is_running:
            if not self.msg_queue.empty():
                msg = self.msg_queue.get()
                self.tracker_master.receive_message(msg)
                time.sleep(1)
        return

    def stop_working(self):
        self.is_running = False
