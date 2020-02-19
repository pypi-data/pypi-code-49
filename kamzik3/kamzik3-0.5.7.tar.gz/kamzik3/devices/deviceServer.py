import json
import logging
from collections import deque
from threading import Thread, Event
from time import perf_counter_ns

import zmq

import kamzik3
from kamzik3 import SEP, CommandFormatException, DeviceServerError, DeviceError
from kamzik3.constants import *
from kamzik3.snippets.snippetDataAccess import rgetattr
from kamzik3.snippets.snippetsJson import JsonPintHook
from kamzik3.snippets.snippetsTimer import PreciseCallbackTimer
from kamzik3.snippets.snippetsYaml import YamlSerializable


class DeviceServer(YamlSerializable):

    def __init__(self, host, server_port, publisher_port):
        self.logger = logging.getLogger(u"Console.DeviceServer@{}:{}".format(host, server_port))
        self.host = host
        self.server_port = server_port
        self.publisher_port = publisher_port
        self.close_event = Event()
        self.messages_queue = deque()
        self.publisher_events = {}
        self.devices = {}
        self._init_publisher()
        self._init_server()
        kamzik3.session.set_device_server(self)

    def _init_server(self):
        """
        Initialize connection to Device server as a client.
        Connection is done via ZMQ REP socket.
        :return: None
        """
        self.logger.info(u"Initializing server thread")
        self.server_socket = zmq.Context.instance().socket(zmq.REP)
        # Set receive timeout to 1000 ms
        self.server_socket.setsockopt(zmq.RCVTIMEO, 1000)
        # Don't let socket linger after close
        # This is VERY IMPORTANT not to set to anything but 0
        self.server_socket.setsockopt(zmq.LINGER, 0)
        self.server_socket.bind("tcp://{}:{}".format(self.host, self.server_port))
        self.server_thread = Thread(target=self._server_thread)
        self.server_thread.start()

    def _server_thread(self):
        while not self.close_event.isSet():
            if self.server_socket.poll(1e3):
                try:
                    data = self.server_socket.recv().decode().split(SEP)
                    device_id, instruction = data[0], data[1]

                    # Execute command directly on devices
                    if instruction == COMMAND:
                        command, with_token = data[2], int(data[3])
                        token = self.get_device(device_id).command(command, with_token=int(with_token))
                        status, response = RESPONSE_OK, len(data[3])

                    # Get devices attribute
                    elif instruction == GET:
                        attribute = json.loads(data[2], object_hook=JsonPintHook)
                        response = self.get_device(device_id)._get(attribute)
                        response = json.dumps(response, ensure_ascii=True)
                        status, token = RESPONSE_OK, 0

                    # Set devices attribute
                    elif instruction == SET:
                        attribute, attribute_value = json.loads(data[2], object_hook=JsonPintHook)
                        set_token = self.get_device(device_id).set_attribute(attribute, attribute_value)
                        status, token, response = RESPONSE_OK, set_token, len(data[2])

                    # Execute devices method with attributes
                    elif instruction == METHOD:
                        method, attributes = data[2], json.loads(data[3], object_hook=JsonPintHook)
                        device = self.get_device(device_id)
                        response = rgetattr(device, method)(**attributes)
                        response = json.dumps(response, ensure_ascii=True)
                        status, token = RESPONSE_OK, 0

                    # Poll devices for activity
                    elif instruction == POLL:
                        status, token, response = RESPONSE_OK, 0, 1

                    # Init devices
                    elif instruction == INIT:
                        device = self.get_device(device_id)

                        if device is None:
                            raise DeviceServerError(
                                "Device {} is not registered on the server or publisher is not ready".format(device_id))
                        elif self.publisher_port is None:
                            raise DeviceServerError("Server publisher is not ready")
                        elif not device.in_statuses(READY_DEVICE_STATUSES):
                            raise DeviceServerError("Device is not ready")
                        else:
                            response = json.dumps(
                                (self.publisher_port, device.attributes, device.attributes_sharing_map,
                                 device.exposed_methods, device.qualified_name),
                                ensure_ascii=True)
                            status, token = RESPONSE_OK, 0

                    # None of above, request not implemented
                    else:
                        status, token, response = RESPONSE_ERROR, 0, len(data[3])

                    self.server_socket.send(SEP.join((str(status), str(token), str(response))).encode())
                except CommandFormatException:
                    status, token, response = RESPONSE_ERROR, 0, u"Command format error"
                    self.server_socket.send(SEP.join((str(status), str(token), str(response))).encode())
                except DeviceServerError:
                    status, token, response = RESPONSE_ERROR, 0, u"Device server error"
                    self.server_socket.send(SEP.join((str(status), str(token), str(response))).encode())
                except DeviceError as e:
                    status, token, response = RESPONSE_ERROR, 0, u"Command error: {}".format(e)
                    self.server_socket.send(SEP.join((str(status), str(token), str(response))).encode())
                except (AttributeError, KeyError) as e:
                    status, token, response = RESPONSE_ERROR, 0, u"Attribute error: {}".format(e)
                    self.server_socket.send(SEP.join((str(status), str(token), str(response))).encode())

        self.handle_closing_server()

    def _init_publisher(self):
        self.logger.info(u"Initializing publisher thread")
        self.publisherSocket = zmq.Context.instance().socket(zmq.PUB)
        self.publisherSocket.bind("tcp://{}:{}".format(self.host, self.publisher_port))
        self.publisher_timer = PreciseCallbackTimer(5, self._publish_messages)
        self.publisher_timer.start()

    def _publish_messages(self):
        publish_time = perf_counter_ns()
        while self.messages_queue:
            header, message, min_timeout = self.messages_queue.popleft()
            last_message_event = self.publisher_events.get(header, None)
            if (last_message_event is None) or (publish_time - last_message_event[0]) >= min_timeout:
                self._publish_message(header, message)
                self.publisher_events[header] = [publish_time, [header, None, min_timeout]]
            else:
                last_message_event[1][1] = message

        for event in list(self.publisher_events.values()):
            if (publish_time - event[0]) >= event[1][2]:
                if event[1][1] is not None:
                    self._publish_message(event[1][0], event[1][1])
                    self.publisher_events[event[1][0]] = [publish_time, [event[1][0], None, event[1][2]]]
                else:
                    del self.publisher_events[event[1][0]]

    def _publish_message(self, header, message):
        try:
            out_message = header + SEP + json.dumps(message, ensure_ascii=True)
            self.publisherSocket.send(out_message.encode())
        except TypeError:
            print(message)

    def add_device(self, device):
        self.logger.info(u"Adding {} into server".format(device.device_id))
        if device.device_id not in self.devices:
            self.devices[device.device_id] = device
            device.set_device_server(self)
            return True
        else:
            return False

    def remove_device(self, device):
        self.logger.info(u"Removing {} from server".format(device.device_id))
        try:
            del self.devices[device.device_id]
            device.clear_device_server()
            return True
        except ValueError:
            return False

    def get_device(self, device_id):
        return self.devices.get(device_id, None)

    def push_message(self, header, message, token=None, min_timeout=100e6):
        try:
            if token is not None:
                header += u"." + str(token)
            self.messages_queue.append((header, message, min_timeout))
        except TypeError:
            self.logger.exception(u"Error pushing message to client")

    def handle_closing_server(self):
        if self.server_socket:
            self.server_socket.close()

    def close(self):
        self.logger.info(u"Closing server")
        self.publisher_timer.stop()
        self.close_event.set()
        if self.server_thread is not None:
            self.server_thread.join(1)
