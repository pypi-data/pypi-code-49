#!/usr/bin/env python
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


"""
================
Message handlers
================

This module implements a message handler that will be in charge with ZeroMQ
communication.
"""

import logging

import zmq
import simplejson
import threading

from ..dataformat import DataFormat
from ..exceptions import RemoteException

from .. import baseformat

from .helpers import make_data_format


logger = logging.getLogger(__name__)


class MessageHandler(threading.Thread):
    """A 0MQ message handler for our communication with other processes"""

    def __init__(
        self, host_address, data_sources=None, kill_callback=None, context=None
    ):

        super(MessageHandler, self).__init__()

        # An event unblocking a graceful stop
        self.stop = threading.Event()
        self.stop.clear()

        self.must_kill = threading.Event()
        self.must_kill.clear()

        # Either starts a 0MQ server or connect to an existing one
        self.context = context or zmq.Context.instance()
        self.socket = self.context.socket(zmq.PAIR)

        if not host_address.startswith("tcp://"):
            self.address = "tcp://" + host_address
        else:
            self.address = host_address

        if len(self.address.split(":")) == 2:
            port = self.socket.bind_to_random_port(self.address, min_port=50000)
            self.address += ":%d" % port
        else:
            self.socket.bind(self.address)

        logger.debug("zmq server bound to '%s'", self.address)

        self.poller = zmq.Poller()
        self.poller.register(self.socket, zmq.POLLIN)

        # Initialisations
        self.data_sources = None
        self.system_error = ""
        self.user_error = ""
        self.statistics = {}

        self.kill_callback = kill_callback

        # implementations
        self.callbacks = dict(don=self.done, err=self.error)

        if data_sources is not None:
            self.set_data_sources(data_sources)

    def destroy(self):
        self.socket.close()
        self.context.destroy()
        logger.debug("0MQ client finished")

    def __str__(self):
        return "MessageHandler(%s)" % self.address

    def set_data_sources(self, data_sources):
        self.data_sources = data_sources

        self.callbacks.update(dict(ifo=self.infos, get=self.get_data))

    def run(self):
        logger.debug("0MQ server thread started")

        while not self.stop.is_set():  # keep on

            if self.must_kill.is_set():
                if self.kill_callback is not None:
                    self.kill_callback()
                self.must_kill.clear()
                break

            timeout = 1000  # ms
            socks = dict(self.poller.poll(timeout))

            if self.socket in socks and socks[self.socket] == zmq.POLLIN:

                # incomming
                more = True
                parts = []
                while more:
                    parts.append(self.socket.recv())
                    more = self.socket.getsockopt(zmq.RCVMORE)
                command = parts[0].decode("utf-8")

                if command in self.callbacks:
                    try:  # to handle command
                        self.callbacks[command](*parts[1:])
                    except RemoteException as e:
                        if e.system_error != "":
                            self.send_error(e.system_error, kind="sys")
                            self.system_error = e.system_error
                        else:
                            self.send_error(e.user_error, kind="usr")
                            self.user_error = e.user_error
                        if self.kill_callback is not None:
                            self.kill_callback()
                        self.stop.set()
                        break
                    except RuntimeError:
                        import traceback

                        message = traceback.format_exc()
                        logger.error(message, exc_info=True)
                        self.send_error(message, kind="usr")
                        self.user_error = message
                        if self.kill_callback is not None:
                            self.kill_callback()
                        self.stop.set()
                        break
                    except Exception:
                        import traceback

                        def parser(s):
                            parsed = s if len(s) < 20 else s[:20] + b"..."
                            return parsed.decode("utf-8")

                        parsed_parts = " ".join([parser(k) for k in parts])
                        message = (
                            "A problem occurred while performing command `%s' "
                            "killing user process. Exception:\n %s"
                            % (parsed_parts, traceback.format_exc())
                        )
                        logger.error(message, exc_info=True)
                        self.send_error(message)
                        self.system_error = message
                        if self.kill_callback is not None:
                            self.kill_callback()
                        self.stop.set()
                        break

                else:
                    logger.debug("recv: %s", command)

                    message = (
                        "Command `%s' is not implemented - stopping user process"
                        % command
                    )
                    logger.error(message)
                    self.send_error(message)
                    self.system_error = message
                    if self.kill_callback is not None:
                        self.kill_callback()
                    self.stop.set()
                    break

        logger.debug("0MQ server thread stopped")

    def _acknowledge(self):

        logger.debug("send: ack")
        self.socket.send_string("ack")
        logger.debug("setting stop condition for 0MQ server thread")
        self.stop.set()

    def done(self, statistics=None):
        """Syntax: don"""

        logger.debug("recv: don %s", statistics)

        if statistics is not None:
            self.statistics = simplejson.loads(statistics)

        self._acknowledge()

    def error(self, t, msg):
        """Syntax: err type message"""

        t = t.decode("utf-8")
        msg = msg.decode("utf-8")

        logger.debug("recv: err %s <msg> (size=%d)", t, len(msg))

        if t == "usr":
            self.user_error = msg
        else:
            self.system_error = msg

        self.statistics = dict(network=dict(wait_time=0.0))
        self._acknowledge()

    def infos(self, name):
        """Syntax: ifo name"""

        name = name.decode("utf-8")
        logger.debug("recv: ifo %s", name)

        if self.data_sources is None:
            message = "Unexpected message received: ifo %s" % name
            raise RemoteException("sys", message)

        try:
            data_source = self.data_sources[name]
        except Exception:
            raise RemoteException("sys", "Unknown input: %s" % name)

        logger.debug("send: %d infos", len(data_source))

        self.socket.send_string("%d" % len(data_source), zmq.SNDMORE)

        for start, end in data_source.data_indices():
            self.socket.send_string("%d" % start, zmq.SNDMORE)

            if end < data_source.last_data_index():
                self.socket.send_string("%d" % end, zmq.SNDMORE)
            else:
                self.socket.send_string("%d" % end)

    def get_data(self, name, index):
        """Syntax: get name index"""

        name = name.decode("utf-8")
        index = index.decode("utf-8")

        logger.debug("recv: get %s %s", name, index)

        if self.data_sources is None:
            message = "Unexpected message received: get %s %s" % (name, index)
            raise RemoteException("sys", message)

        try:
            data_source = self.data_sources[name]
        except Exception:
            raise RemoteException("sys", "Unknown input: %s" % name)

        try:
            index = int(index)
        except Exception:
            raise RemoteException("sys", "Invalid index: %s" % index)

        (data, start_index, end_index) = data_source[index]

        if data is None:
            raise RemoteException("sys", "Invalid index: %s" % index)

        if isinstance(data, baseformat.baseformat):
            packed = data.pack()
        else:
            packed = data

        logger.debug(
            "send: <bin> (size=%d), indexes=(%d, %d)",
            len(packed),
            start_index,
            end_index,
        )

        self.socket.send_string("%d" % start_index, zmq.SNDMORE)
        self.socket.send_string("%d" % end_index, zmq.SNDMORE)
        self.socket.send(packed)

    def kill(self):
        self.must_kill.set()

    def send_error(self, message, kind="usr"):
        """Sends a user (usr) or system (sys) error message to the infrastructure"""

        logger.debug("send: (err) error")
        self.socket.send_string("err", zmq.SNDMORE)
        self.socket.send_string(kind, zmq.SNDMORE)
        logger.debug('send: """%s"""' % message.rstrip())
        self.socket.send_string(message)

        this_try = 1
        max_tries = 5
        timeout = 1000  # ms
        while this_try <= max_tries:
            socks = dict(
                self.poller.poll(timeout)
            )  # blocks here, for 5 seconds at most
            if self.socket in socks and socks[self.socket] == zmq.POLLIN:
                answer = self.socket.recv()  # ack
                logger.debug("recv: %s", answer)
                break
            logger.warn(
                '(try %d) waited %d ms for "ack" from server', this_try, timeout
            )
            this_try += 1
            if this_try > max_tries:
                logger.error("could not send error message to server")
                logger.error("stopping 0MQ client anyway")


class LoopMessageHandler(MessageHandler):
    """ Custom message handler that will handle validation request from loop
    using algorithm
    """

    def __init__(
        self, host_address, data_sources=None, kill_callback=None, context=None
    ):
        """Reimplementation"""

        super(LoopMessageHandler, self).__init__(
            host_address, data_sources, kill_callback, context
        )

        self.callbacks.update({"val": self.validate})
        self.callbacks.update({"wrt": self.write})
        self.callbacks.update({"rdi": self.read})

        self.executor = None

    def setup(self, algorithm, prefix):
        """ Setup the loop internals

        Parameters:
            algorithm (:py:class:`.algorithm.Algorithm`) : algorithm for which
              the communication channel is setup.

            prefix (str) : Folder were the prefix is located.
        """

        request_format_name = algorithm.loop_map["request"]
        self.request_data_format = DataFormat(prefix, request_format_name)

        answer_format_name = algorithm.loop_map["answer"]
        self.answer_data_format = DataFormat(prefix, answer_format_name)

    def set_executor(self, executor):
        """ Set the executor for validation

        Parameters:
            executor (:py:class:`.loop.LoopExecutor`) : Loop executor
        """
        self.executor = executor

    def validate(self, result):
        """ Validate the result received and send back a boolean answer about
        the validity of it as well as additional data for the loop using
        algorithm to process

        Syntax: val

        Parameters:
            result (:py:class:`beat.backend.python.dataformat.DataFormat`) :
              Result to be validated.
        """

        data = self.request_data_format.type()
        data.unpack(result)

        logger.debug("recv: val %s", data)

        is_valid, answer = self.executor.validate(data)

        data = make_data_format(answer, self.answer_data_format)

        self.socket.send_string("True" if is_valid else "False", zmq.SNDMORE)
        self.socket.send(data.pack())

    def write(self, processor_output_name, end_data_index):
        """ Trigger a write on the output"""

        processor_output_name = processor_output_name.decode("utf-8")
        end_data_index = end_data_index.decode("utf-8")

        if end_data_index != "None":
            try:
                end_data_index = int(end_data_index)
            except ValueError:
                logger.warning("recv: wrt invalid value {}".format(end_data_index))
                end_data_index = None
        else:
            end_data_index = None

        logger.debug("recv: wrt {} {}".format(processor_output_name, end_data_index))

        try:
            self.executor.write(processor_output_name, end_data_index)
        except Exception as e:
            logger.warning("recv: wrt write failed: {}".format(e))
            raise
        finally:
            self.socket.send_string("ack")

    def read(self):
        """Read next data"""

        try:
            self.executor.read()
        except Exception:
            raise
        finally:
            self.socket.send_string("ack")
