""" Implementation based on: https://github.com/bitcoin/bitcoin/blob/master/contrib/zmq/zmq_sub.py """

import zmq.asyncio
import traceback
import binascii
import asyncio
import signal
import struct
import time
import sys
import zmq
import os

class ZMQNotifier():

    TOPIC_BLOCKHASH = 'hashblock'
    TOPIC_TXID = 'hashtx'
    TOPIC_RAWBLOCK = 'rawblock'
    TOPIC_RAWTX = 'rawtx'

    def __init__(self, zmq_address, topics=[TOPIC_BLOCKHASH, TOPIC_TXID, TOPIC_RAWBLOCK, TOPIC_RAWBLOCK], loop=None, verbose=False, **kwargs):
        self.auto = False
        self.verbose = verbose
        self.zmqContext = zmq.asyncio.Context()
        self.topic_set = set([s.strip() for s in topics])
        self.loop = loop if loop else asyncio.get_event_loop()

        earg = 'error_callback'
        ecb = [kwargs[earg]] if earg in kwargs else []
        self.listeners = {'__error__': ecb }

        self.zmqSubSocket = self.zmqContext.socket(zmq.SUB)
        self.zmqSubSocket.setsockopt(zmq.RCVHWM, 0)
        for topic in self.topic_set:
            targ = topic + '_callback'
            self.listeners[topic] = [kwargs[targ]] if targ in kwargs else[]
            self.zmqSubSocket.setsockopt_string(zmq.SUBSCRIBE, topic)

        self.zmqSubSocket.connect(zmq_address)

    def add_callback(self, topic, callback):
        self.listeners[topic].append(callback)

    def add_error_callback(self, callback):
        self.listeners['__error__'].append(callback)

    async def handle(self):
        try:
            msg = await self.zmqSubSocket.recv_multipart()
            topic = msg[0].decode('utf8')
            body = msg[1]
            if topic in self.topic_set:
                hex_body = binascii.hexlify(body)
                for callback in self.listeners[topic]:
                    if self.verbose:
                        if asyncio.iscoroutinefunction(callback):
                            self.loop.create_task(callback(hex_body, body))
                        else: callback(hex_body, body)
                    else:
                        if asyncio.iscoroutinefunction(callback):
                            self.loop.create_task(callback(hex_body.decode('utf-8')))
                        else: callback(hex_body.decode('utf-8'))
        except Exception as e:
            for callback in self.listeners['__error__']:
                if asyncio.iscoroutinefunction(callback):
                    tb = self.loop.create_task(callback(e))
                else: tb = callback(e)
                if tb: traceback.print_exc()
        if self.auto: self.loop.create_task(self.handle())

    def start(self, disable_signals=False):
        self.auto = True
        if not disable_signals:
            self.loop.add_signal_handler(signal.SIGTERM, self.stop)
            self.loop.add_signal_handler(signal.SIGINT, self.stop)
        self.loop.create_task(self.handle())
        self.loop.run_forever()
        return self.loop

    def stop(self):
        self.loop.stop()
        self.zmqContext.destroy()