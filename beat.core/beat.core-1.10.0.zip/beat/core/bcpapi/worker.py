# vim: set fileencoding=utf-8 :

###################################################################################
#                                                                                 #
# Copyright (c) 2019 Idiap Research Institute, http://www.idiap.ch/               #
# Contact: beat.support@idiap.ch                                                  #
#                                                                                 #
# Redistribution and use in source and binary forms, with or without              #
# modification, are permitted provided that the following conditions are met:     #
#                                                                                 #
# 1. Redistributions of source code must retain the above copyright notice, this  #
# list of conditions and the following disclaimer.                                #
#                                                                                 #
# 2. Redistributions in binary form must reproduce the above copyright notice,    #
# this list of conditions and the following disclaimer in the documentation       #
# and/or other materials provided with the distribution.                          #
#                                                                                 #
# 3. Neither the name of the copyright holder nor the names of its contributors   #
# may be used to endorse or promote products derived from this software without   #
# specific prior written permission.                                              #
#                                                                                 #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND #
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED   #
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE          #
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE    #
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL      #
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR      #
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER      #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,   #
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE   #
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.            #
#                                                                                 #
###################################################################################


"""BEAT Computation worker"""

import logging
import time
import zmq

# BEAT Computation protocol constants:
from . import BCP

from .zhelpers import dump

logger = logging.getLogger(__name__)


class BeatComputationWorker(object):
    """BEAT Computation Protocol Worker API, Python version
    """

    HEARTBEAT_LIVENESS = 3  # 3-5 is reasonable

    def __init__(self, poller, broker, service, verbose=False):
        if isinstance(service, str):
            service = service.encode("utf-8")

        self.heartbeat_at = (
            0
        )  # When to send HEARTBEAT (relative to time.time(), so in seconds)
        self.liveness = 0  # How many attempts left
        self.heartbeat = 2500  # Heartbeat delay, msecs
        self.reconnect = 2500  # Reconnect delay, msecs
        self.timeout = 2500  # poller timeout

        self.reply_to = None  # Return address, if any

        self.worker = None
        self.broker = broker
        self.service = service
        self.verbose = verbose
        self.ctx = zmq.Context()
        self.poller = poller

        self.reconnect_to_broker()

    def reconnect_to_broker(self):
        """Connect or reconnect to broker"""
        if self.worker:
            self.poller.unregister(self.worker)
            self.worker.close()
        self.worker = self.ctx.socket(zmq.DEALER)
        self.worker.linger = 0
        self.worker.connect(self.broker)
        self.poller.register(self.worker, zmq.POLLIN)
        if self.verbose:
            logger.info("I: connecting to broker at %s…", self.broker)

        # Register service with broker
        self.send_to_broker(BCP.BCPW_READY, self.service, [])

        # If liveness hits zero, queue is considered disconnected
        self.liveness = self.HEARTBEAT_LIVENESS
        self.heartbeat_at = time.time() + 1e-3 * self.heartbeat

    def send_to_broker(self, command, option=None, msg=None):
        """Send message to broker.

        If no msg is provided, creates one internally
        """
        if msg is None:
            msg = []
        elif not isinstance(msg, list):
            msg = [msg]

        if option:
            msg = [option] + msg

        msg = [b"", BCP.BCPW_WORKER, command] + msg
        if self.verbose:
            logger.info("I: sending %s to broker", command)
            dump(msg)
        self.worker.send_multipart(msg)

    def send(self, reply):
        """Send reply to broker"""
        assert self.reply_to is not None  # nosec
        reply = [self.reply_to, b"", self.service] + reply
        self.send_to_broker(BCP.BCPW_REPLY, msg=reply)

    def process(self):
        msg = self.worker.recv_multipart()
        if self.verbose:
            logger.info("I: received message from broker: ")
            dump(msg)

        self.liveness = self.HEARTBEAT_LIVENESS
        # Don't try to handle errors, just assert noisily
        assert len(msg) >= 3  # nosec

        empty = msg.pop(0)
        assert empty == b""  # nosec

        header = msg.pop(0)
        assert header == BCP.BCPW_WORKER  # nosec

        command = msg.pop(0)
        if command == BCP.BCPW_REQUEST:
            # We should pop and save as many addresses as there are
            # up to a null part, but for now, just save one…
            self.reply_to = msg.pop(0)
            # pop empty
            empty = msg.pop(0)
            assert empty == b""  # nosec

            return msg  # We have a request to process
        elif command == BCP.BCPW_HEARTBEAT:
            # Do nothing for heartbeats
            pass
        elif command == BCP.BCPW_DISCONNECT:
            self.reconnect_to_broker()
        else:
            logger.error("E: invalid input message: ")
            dump(msg)

        # Send HEARTBEAT if it's time
        if time.time() > self.heartbeat_at:
            self.send_to_broker(BCP.BCPW_HEARTBEAT)
            self.heartbeat_at = time.time() + 1e-3 * self.heartbeat

        return None

    def recv(self):
        """Wait for next request."""

        while True:
            # Poll socket for a reply, with timeout
            try:
                items = dict(self.poller.poll(self.timeout))
            except KeyboardInterrupt:
                break  # Interrupted

            if items:
                msg = self.worker.recv_multipart()
                if self.verbose:
                    logger.info("I: received message from broker: ")
                    dump(msg)

                self.liveness = self.HEARTBEAT_LIVENESS
                # Don't try to handle errors, just assert noisily
                assert len(msg) >= 3  # nosec

                empty = msg.pop(0)
                assert empty == b""  # nosec

                header = msg.pop(0)
                assert header == BCP.BCPW_WORKER  # nosec

                command = msg.pop(0)
                if command == BCP.BCPW_REQUEST:
                    # We should pop and save as many addresses as there are
                    # up to a null part, but for now, just save one...
                    self.reply_to = msg.pop(0)
                    # pop empty
                    empty = msg.pop(0)
                    assert empty == b""  # nosec

                    return msg  # We have a request to process
                elif command == BCP.BCPW_HEARTBEAT:
                    # Do nothing for heartbeats
                    pass
                elif command == BCP.BCPW_DISCONNECT:
                    self.reconnect_to_broker()
                else:
                    logger.error("E: invalid input message: ")
                    dump(msg)
            else:
                self.liveness -= 1
                if self.liveness == 0:
                    if self.verbose:
                        logger.warn("W: disconnected from broker - retrying…")
                    try:
                        time.sleep(1e-3 * self.reconnect)
                    except KeyboardInterrupt:
                        break
                    self.reconnect_to_broker()

            # Send HEARTBEAT if it's time
            if time.time() > self.heartbeat_at:
                self.send_to_broker(BCP.BCPW_HEARTBEAT)
                self.heartbeat_at = time.time() + 1e-3 * self.heartbeat

        logger.warn("W: interrupt received, killing worker…")
        return None

    def destroy(self):
        # context.destroy depends on pyzmq >= 2.1.10
        self.ctx.destroy(0)
