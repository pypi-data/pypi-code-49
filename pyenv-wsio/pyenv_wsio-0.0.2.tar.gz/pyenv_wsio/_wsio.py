# -*- coding: utf-8 -*-

from ._events import EventEmitter
import websocket
import Queue as queue
import _packet
import threading
import signal

import six

original_signal_handler = None
connected_clients = []

OPCODE_CONT = 0x0
OPCODE_TEXT = 0x1
OPCODE_BINARY = 0x2
OPCODE_CLOSE = 0x8
OPCODE_PING = 0x9
OPCODE_PONG = 0xa


def signal_handler(sig, frame):
    for client in connected_clients[:]:
        client.disconnect(abort=True)

    if callable(original_signal_handler):
        return original_signal_handler(sig, frame)
    else:  # pragma: no cover
        # Handle case where no original SIGINT handler was present.
        return signal.default_int_handler(sig, frame)

class ConnectionError(Exception):
    pass

class Wsio(EventEmitter):
    events = ['connect', 'disconnect', 'message']

    def __init__(self):
        EventEmitter.__init__(self)

        global original_signal_handler
        if original_signal_handler is None:
            original_signal_handler = signal.signal(
                signal.SIGINT, signal_handler)

        self.ping_interval = None
        self.ping_timeout = None
        self.pong_received = True
        self.ws = None
        self.read_loop_task = None
        self.write_loop_task = None
        self.ping_loop_task = None
        self.ping_loop_event = None
        self.queue = None
        self.sid = None
        self.state = 'disconnected'

    def connect(self, url, headers={}):
        if(self.state != 'disconnected'):
            self.emit('error', ValueError('Client is not in a disconnected state'))
            return False

        self.queue=self.create_queue()

        try:
            ws=websocket.create_connection(url, headers=headers)
        except (IOError, websocket.WebSocketException) as e:
            self.emit('error', e)
            return False

        try:
            # handshake packet
            p=ws.recv()

        except Exception as e:
            self.emit('error', e)
            ws.close()
            return False

        handshake_packet=_packet.Packet(encoded_packet=p)

        if handshake_packet.packet_type != _packet.HANDSHAKE:
            self.emit('error', ConnectionError('no OPEN packet'))
            return False

        self.sid=handshake_packet.data[u'sid']
        self.ping_interval=handshake_packet.data[u'pingInterval']/1000.0
        self.ping_timeout=handshake_packet.data[u'pingTimeout']/1000.0

        self.state='connected'
        connected_clients.append(self)
        self.emit('connect')

        self.ws=ws
        self.ping_loop_task=self.start_background_task(self._ping_loop)
        self.write_loop_task=self.start_background_task(self._write_loop)
        self.read_loop_task=self.start_background_task(self._read_loop)
        return True

    def send(self, data):
        if self.state != 'connected':
            return

        self.queue.put(data)

    def create_queue(self, *args, **kwargs):
        q=queue.Queue(*args, **kwargs)
        q.Empty=queue.Empty
        return q

    def create_event(self, *args, **kwargs):
        return threading.Event(*args, **kwargs)

    def start_background_task(self, target, *args, **kwargs):
        th=threading.Thread(target=target, args=args, kwargs=kwargs)
        th.setDaemon(True)
        th.start()
        return th

    def disconnect(self, abort=False):
        if self.state == 'connected':
            self.queue.put(None)
            self.state='disconnecting'
            self.emit('disconnect')
            self.ws.close()

            if not abort:
                self.read_loop_task.join()

            self.state='disconnected'

            try:
                connected_clients.remove(self)
            except ValueError:
                pass

        self._reset()

    def _ping_loop(self):
        self.pong_received=True

        if self.ping_loop_event is None:
            self.ping_loop_event=self.create_event()
        else:
            self.ping_loop_event.clear()

        while(self.state == 'connected' and self.ws.connected):
            if not self.pong_received:
                self.ws.close(timeout=0)
                self.queue.put(None)
                break
            self.pong_received=False
            self.ws.ping()
            self.ping_loop_event.wait(timeout=self.ping_interval)

    def _write_loop(self):
        while self.state == 'connected' and self.ws.connected:
            timeout=max(self.ping_interval, self.ping_timeout)+5
            packets=None

            try:
                packets=[self.queue.get(timeout=timeout)]
            except self.queue.Empty:
                break

            if packets == [None]:
                self.queue.task_done()
                packets=[]
            else:
                while True:
                    try:
                        packets.append(self.queue.get(block=False))
                    except self.queue.Empty:
                        break

                    if packets[-1] is None:
                        packets=packets[:-1]
                        self.queue.task_done()
                        break

            if not packets:
                break

            try:
                for pkt in packets:
                    self.ws.send(pkt)
                    self.queue.task_done()
            except websocket.WebSocketConnectionClosedException:
                break

    def _read_loop(self):
        while self.state == 'connected' and self.ws.connected:
            opcode=None
            data=None

            try:
                opcode, data=self.ws.recv_data(True)
            except websocket.WebSocketConnectionClosedException:
                self.queue.put(None)
                break
            except Exception as e:
                self.emit('error', e)
                self.queue.put(None)
                break

            if six.PY3 and opcode == OPCODE_TEXT:
                data=data.decode("utf-8")
            
            # print 'recv:',data
            if opcode in (OPCODE_BINARY, OPCODE_TEXT):
                self.emit('message', data)
            elif opcode == OPCODE_PONG:
                self.pong_received=True
            elif opcode == OPCODE_CLOSE:
                self.disconnect(abort=True)

        self.write_loop_task.join()
        if self.ping_loop_event:
            self.ping_loop_event.set()
        self.ping_loop_task.join()

        if self.state == 'connected':
            self.emit('disconnect')
            try:
                connected_clients.remove(self)
            except ValueError:
                pass

            self._reset()

    def _reset(self):
        self.state='disconnected'
        self.sid=None
