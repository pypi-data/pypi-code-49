# # -*- coding: utf-8 -*-

import signal
import random

from ._wsio import *
from . import _packet
from . import _namespace

reconnecting_clients = []


def _signal_handler(sig, frame):
    for client in reconnecting_clients[:]:
        client._reconnect_abort.set()

    if callable(_original_signal_handler):
        return _original_signal_handler(sig, frame)
    else:  # pragma: no cover
        # Handle case where no original SIGINT handler was present.
        return signal.default_int_handler(sig, frame)


_original_signal_handler = signal.signal(signal.SIGINT, _signal_handler)


class Client():
    def __init__(self, reconnection=True, reconnection_attempts=0,
                 reconnection_delay=1, reconnection_delay_max=5,
                 randomization_factor=0.5):

        self.reconnection = reconnection
        self.reconnection_attempts = reconnection_attempts
        self.reconnection_delay = reconnection_delay
        self.reconnection_delay_max = reconnection_delay_max
        self.randomization_factor = randomization_factor

        self.eio = Wsio()
        self.eio.on('connect', self._on_eio_connect)
        self.eio.on('message', self._on_eio_message)
        self.eio.on('disconnect', self._on_eio_disconnect)
        self.eio.on('error', self._on_eio_error)

        self.connection_url = None
        self.connection_headers = None
        self.sid = None

        self.connected = False
        self.namespaces = {}
        self._binary_packet = None
        self._reconnect_task = None
        self._reconnect_abort = self.eio.create_event()

    def connect(self, url, headers={}):
        self.connection_url = url
        self.connection_headers = headers
        self.connected=self.eio.connect(url, headers=headers)
        return self.connected

    def disconnect(self):
        self.reconnection = False
        self._reconnect_abort.set()
        for n in self.namespaces:
            nsp = self.namespaces[n]
            nsp.on_disconnect()
            self._send_packet(_packet.Packet(_packet.DISCONNECT, namespace=n))

        self.connected = False
        self.eio.disconnect()

    def of(self, name):
        if name in self.namespaces:
            namespace = self.namespaces[name]
        else:
            namespace = _namespace.ClientNamespace(name, self)
            self.namespaces[name] = namespace
        return namespace

    def _send_packet(self, pkt):
        encoded_packet = pkt.encode()
        print encoded_packet
        if isinstance(encoded_packet, list):
            for ep in encoded_packet:
                print '_send_packet:', ep
                self.eio.send(ep)
        else:
            self.eio.send(encoded_packet)

    def _on_eio_connect(self):
        self.sid = self.eio.sid

    def _on_eio_message(self, data):
        if self._binary_packet:
            pkt = self._binary_packet
            if pkt.add_attachment(data):
                self._binary_packet = None
                if pkt.packet_type == _packet.BINARY_EVENT:
                    self._do_event(pkt.namespace, pkt.id, pkt.data)
                else:
                    self._do_ack(pkt.namespace, pkt.id, pkt.data)
        else:
            pkt = _packet.Packet(encoded_packet=data)
            # print 'type:', pkt.packet_type
            if pkt.packet_type == _packet.CONNECT:
                self._do_connect(pkt.namespace)
            elif pkt.packet_type == _packet.DISCONNECT:
                self._do_disconnect(pkt.namespace)
            elif pkt.packet_type == _packet.EVENT:
                self._do_event(pkt.namespace, pkt.id, pkt.data)
            elif pkt.packet_type == _packet.ACK:
                self._do_ack(pkt.namespace, pkt.id, pkt.data)
            elif pkt.packet_type == _packet.BINARY_EVENT or pkt.packet_type == _packet.BINARY_ACK:
                self._binary_packet = pkt
            elif pkt.packet_type == _packet.ERROR:
                self._do_error(pkt.namespace, pkt.data)

    def _on_eio_disconnect(self):

        if self.connected:
            for n in self.namespaces:
                nsp = self.namespaces[n]
                nsp.on_disconnect()

            self.connected = False

        self._binary_packet = None
        self.sid = None

        if self.eio.state == 'connected' and self.reconnection and self._reconnect_task == None:
            self._reconnect_task = self.eio.start_background_task(
                self._do_reconnect)

    def _on_eio_error(self, e):
        if isinstance(e, ValueError) or isinstance(e, ConnectionError):
            return
        else:
            self._reconnect_task = None

        self._on_eio_disconnect()

    def _do_connect(self, namespace):
        namespace = namespace or '/'
        if namespace in self.namespaces:
            nsp = self.namespaces[namespace]
            nsp.on_connect()

        if namespace == '/':
            for n in self.namespaces:
                nsp = self.namespaces[n]
                if n != '/' and nsp.connected == False:
                    self._send_packet(_packet.Packet(
                        _packet.CONNECT, namespace=n))

    def _do_disconnect(self, namespace):
        if not self.connected:
            return

        namespace = namespace or '/'

        if namespace == '/':
            for n in self.namespaces:
                nsp = self.namespaces[n]
                nsp.on_disconnect()

            self.connected = False

        else:
            if namespace in self.namespaces:
                nsp = self.namespaces[namespace]
                nsp.on_disconnect()

    def _do_ack(self, namespace, id, data):
        namespace = namespace or '/'

        if namespace in self.namespaces:
            nsp = self.namespaces[namespace]
            nsp.on_ack(id, data)

    def _do_event(self, namespace, id, data):
        namespace = namespace or '/'

        if namespace in self.namespaces:
            nsp = self.namespaces[namespace]
            nsp.on_event(id, data)

    def _do_error(self, namespace, data):
        namespace = namespace or '/'

        if namespace in self.namespaces:
            nsp = self.namespaces[namespace]
            nsp.on_error(data)

    def _do_reconnect(self):
        self._reconnect_abort.clear()
        reconnecting_clients.append(self)
        attempt_count = 0
        current_delay = self.reconnection_delay

        while self.reconnection:
            delay = current_delay
            current_delay *= 2
            if delay > self.reconnection_delay_max:
                delay = self.reconnection_delay_max

            delay += self.randomization_factor * (2*random.random()-1)

            if self._reconnect_abort.wait(delay):
                break

            attempt_count += 1
            if self.connect(self.connection_url, self.connection_headers):
                break

            if self.reconnection_attempts and attempt_count >= self.reconnection_attempts:
                break
        
        reconnecting_clients.remove(self)
        self._reconnect_task = None
