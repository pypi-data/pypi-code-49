import asynchat
import asyncore
import logging
import socket
from collections import OrderedDict
from threading import Thread, Event, Lock

import numpy

from kamzik3.constants import *
from kamzik3.snippets.snippetsTimer import CallbackTimer
from kamzik3.snippets.snippetsTimer import PreciseCallbackTimer


# TODO: Look for possibility to use event loop

class PortReadLoop(PreciseCallbackTimer):

    def __init__(self, interval=5):
        self.interval = interval
        self.lock = Lock()
        self.logger = logging.getLogger(u"Console.PortReadLoop")
        PreciseCallbackTimer.__init__(self, interval, self.handle_interval_timeout)
        self.map = []
        self.stopped = Event()

    def run(self):
        self.logger.info(u"Starting port readout loop Thread")
        PreciseCallbackTimer.run(self)

    def add_device(self, device):
        with self.lock:
            if device not in self.map:
                self.map.append(device)
                return True
            else:
                return False

    def remove_device(self, device):
        with self.lock:
            if device in self.map:
                self.map.remove(device)
                return True
            else:
                return False

    def handle_interval_timeout(self):
        with self.lock:
            for device in self.map:
                try:
                    device.handle_read()
                except IOError:
                    device.handle_response_error(u"Port read error")

    def stop(self):
        self.logger.info(u"Stopping port readout loop Thread")
        PreciseCallbackTimer.stop(self)


class DeviceConnectionPoller(CallbackTimer):

    def __init__(self, interval=2000):
        self.connecting_devices = []
        self.connected_devices = []
        self.lock = Lock()
        self.interval = interval
        self.logger = logging.getLogger(u"Console.DeviceConnectionPoller")
        PreciseCallbackTimer.__init__(self, self.interval, self.check_devices_connection_timeout, with_correction=False)

    def run(self):
        self.logger.info(u"Starting devices connection poller Thread")
        CallbackTimer.run(self)

    def add_connecting_device(self, device):
        with self.lock:
            if device not in self.connecting_devices:
                self.connecting_devices.append(device)

    def remove_connecting_device(self, device):
        with self.lock:
            try:
                self.connecting_devices.remove(device)
            except ValueError:
                pass  # device was removed already

    def check_devices_connection_timeout(self):
        for device in self.connecting_devices[:]:
            if not device.connected and not device.connecting and device.allow_reconnect and (
                    device.response_error or device.connection_error):
                device.reconnect()
            elif device.connecting_time >= device.connection_timeout:
                if not device.allow_reconnect:
                    self.remove_connecting_device(device)
                device.handle_connection_error(u"Connection timeout")
            elif device.connected:
                self.remove_connecting_device(device)
                self.connected_devices.append(device)
            else:
                device.connecting_time += self.interval
        for device in self.connected_devices:
            if not device.is_alive():
                self.connected_devices.remove(device)
                if device.allow_reconnect and (device.response_error or device.connection_error):
                    self.add_connecting_device(device)

    def stop(self):
        self.logger.info(u"Stopping devices connection poller Thread")
        CallbackTimer.stop(self)


class DevicePoller(PreciseCallbackTimer):

    def __init__(self, interval=5):
        self.interval = interval
        self.commands_buffer = {}
        self.lock = Lock()
        self.logger = logging.getLogger(u"Console.DevicePoller")
        self.polling_schedule = OrderedDict()
        self.schedule = []
        self.schedule_at = numpy.uint64(0)
        PreciseCallbackTimer.__init__(self, self.interval, self.timer_tick, with_correction=True)

    def run(self):
        self.logger.info(u"Starting devices poller Thread")
        PreciseCallbackTimer.run(self)

    def timer_tick(self):
        with self.lock:
            for pollAt in self.schedule:
                if self.schedule_at % pollAt == 0:
                    for device, attributes in self.polling_schedule[pollAt].items():
                        if device.accepting_commands() and device in self.commands_buffer:
                            self.commands_buffer[device] += attributes

            for device, commands in self.commands_buffer.items():
                if commands and device.accepting_commands():
                    self.commands_buffer[device] = device.send_command(commands)
                    device.set_value(ATTR_BUFFERED_COMMANDS, len(self.commands_buffer[device]))

            self.schedule_at += self.interval

    def set_timeout(self, timeout):
        PreciseCallbackTimer.set_timeout(self, timeout)
        self.interval = timeout
        self.schedule_at = 0

    def stop(self):
        self.logger.info(u"Stopping devices poller Thread")
        PreciseCallbackTimer.stop(self)

    def add(self, device, attribute, poll_at, callback=None, returning=True, force_add=False):
        with self.lock:
            if poll_at not in self.polling_schedule:
                self.polling_schedule[poll_at] = OrderedDict()
            if device not in self.polling_schedule[poll_at]:
                self.polling_schedule[poll_at][device] = []
            if device not in self.commands_buffer:
                self.commands_buffer[device] = []

            polling_quadruplet = (attribute, None, callback, returning)
            if force_add or polling_quadruplet not in self.polling_schedule[poll_at][device]:
                self.polling_schedule[poll_at][device].append(polling_quadruplet)

            self.schedule = sorted(self.polling_schedule.keys())

    def remove(self, device, attribute, poll_at, callback=None, returning=True):
        with self.lock:
            try:
                self.polling_schedule[poll_at][device].remove((attribute, None, callback, returning))
                if len(self.polling_schedule[poll_at][device]) == 0:
                    del self.polling_schedule[poll_at][device]
                    del self.commands_buffer[device]
                if len(self.polling_schedule[poll_at]) == 0:
                    del self.polling_schedule[poll_at]

                self.schedule = sorted(self.polling_schedule.keys())
            except (ValueError, KeyError):
                pass

    def stop_polling(self, device):
        with self.lock:
            if device in self.commands_buffer:
                del self.commands_buffer[device]
            for polledDevices in self.polling_schedule.values():
                try:
                    if device in polledDevices:
                        del polledDevices[device]
                except (ValueError, KeyError):
                    pass  # device is no longer within polled devices

    def prepare_command(self, device, command):
        with self.lock:
            try:
                self.commands_buffer[device].append(command)
            except KeyError:
                self.commands_buffer[device] = []
                self.commands_buffer[device].append(command)

    def prepend_command(self, device, command):
        with self.lock:
            try:
                self.commands_buffer[device].insert(0, command)
            except KeyError:
                self.commands_buffer[device] = []
                self.commands_buffer[device].insert(0, command)


class DeviceAsyncoreLoop(Thread):
    dummy_device = None

    def __init__(self):
        self.logger = logging.getLogger(u"Console.DeviceAsyncoreLoop")
        super(DeviceAsyncoreLoop, self).__init__()
        self.dummy_device = asynchat.async_chat()
        self.dummy_device.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.dummy_device.socket.setblocking(False)
        self.setDaemon(True)

    def run(self):
        self.logger.info(u"Starting devices asyncore loop Thread")
        asyncore.loop(use_poll=True, timeout=0.05)

    def stop(self):
        self.logger.info(u"Stopping devices asyncore loop Thread")
        if self.is_alive():
            self.dummy_device.close()

        asyncore.close_all()


control_asyncore_loop = DeviceAsyncoreLoop()
control_device_connection_poller = DeviceConnectionPoller()
control_device_poller = DevicePoller()
control_port_read_loop = PortReadLoop()
