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


# Tests for experiment execution

import os
import unittest
import multiprocessing
import queue
import zmq

import simplejson as json

from flaky import flaky

from ..bcpapi import BCP
from ..bcpapi.client import BeatComputationClient
from ..bcpapi.execution import ExecutionProcess
from ..bcpapi.processor import BeatComputationProcessor

from ..bcp import worker
from ..bcp import broker

from ..database import Database
from ..utils import find_free_port
from ..dock import Host

from . import prefix, tmp_prefix
from . import VERBOSE_BCP_LOGGING

# ----------------------------------------------------------


CONFIGURATION1 = {
    "queue": "queue",
    "inputs": {
        "in": {
            "set": "double",
            "protocol": "double",
            "database": "integers_db/1",
            "output": "a",
            "path": "ec/89/e5/6e161d2cb012ef6ac8acf59bf453a6328766f90dc9baba9eb14ea23c55.db",
            "endpoint": "a",
            "hash": "ec89e56e161d2cb012ef6ac8acf59bf453a6328766f90dc9baba9eb14ea23c55",
            "channel": "integers",
        }
    },
    "algorithm": "legacy/echo/1",
    "parameters": {},
    "environment": {"name": "Python 2.7", "version": "1.3.0"},
    "outputs": {
        "out": {
            "path": "20/61/b6/2df3c3bedd5366f4a625c5d87ffbf5a26007c46c456e9abf21b46c6681",
            "endpoint": "out",
            "hash": "2061b62df3c3bedd5366f4a625c5d87ffbf5a26007c46c456e9abf21b46c6681",
            "channel": "integers",
        }
    },
    "nb_slots": 1,
    "channel": "integers",
}


# ----------------------------------------------------------


CONFIGURATION2 = {
    "queue": "queue",
    "inputs": {
        "in": {
            "set": "double",
            "protocol": "double",
            "database": "integers_db/1",
            "output": "a",
            "path": "ec/89/e5/6e161d2cb012ef6ac8acf59bf453a6328766f90dc9baba9eb14ea23c55.db",
            "endpoint": "a",
            "hash": "ec89e56e161d2cb012ef6ac8acf59bf453a6328766f90dc9baba9eb14ea23c55",
            "channel": "integers",
        }
    },
    "algorithm": "legacy/echo/1",
    "parameters": {},
    "environment": {"name": "Python 2.7", "version": "1.3.0"},
    "outputs": {
        "out": {
            "path": "40/61/b6/2df3c3bedd5366f4a625c5d87ffbf5a26007c46c456e9abf21b46c6681",
            "endpoint": "out",
            "hash": "4061b62df3c3bedd5366f4a625c5d87ffbf5a26007c46c456e9abf21b46c6681",
            "channel": "integers",
        }
    },
    "nb_slots": 1,
    "channel": "integers",
}


# ----------------------------------------------------------


DEFAULT_MAX_ITERATION_COUNT = 30


# ----------------------------------------------------------


class ZMQBrokerProcess(multiprocessing.Process):
    def __init__(self, port, verbose, callbacks=None):
        super(ZMQBrokerProcess, self).__init__()
        self.port = port
        self.verbose = verbose
        self.callbacks = callbacks

    def run(self):
        return broker.run(self.port, verbose=self.verbose, callbacks=self.callbacks)


class ZMQWorkerProcess(multiprocessing.Process):
    def __init__(
        self, address, name, verbose, use_docker=False, docker_images_cache=None
    ):
        super(ZMQWorkerProcess, self).__init__()
        self.broker_address = address
        self.service_name = name
        self.verbose = verbose
        self.use_docker = use_docker
        self.docker_images_cache = None

    def run(self):
        return worker.run(
            self.broker_address,
            service_name=self.service_name,
            verbose=self.verbose,
            prefix=prefix,
            cache=tmp_prefix,
            use_docker=self.use_docker,
            docker_images_cache=self.docker_images_cache,
        )


# ----------------------------------------------------------


class ExecutionTestCase(unittest.TestCase):
    def setUp(self):
        self.MAX_ITERATION_COUNT = int(
            os.environ.get("BPC_MAX_ITERATION_COUNT", DEFAULT_MAX_ITERATION_COUNT)
        )

    def prepare_databases(self, configuration):
        for _, input_cfg in configuration["inputs"].items():
            database = Database(prefix, input_cfg["database"])
            view = database.view(input_cfg["protocol"], input_cfg["set"])
            view.index(os.path.join(tmp_prefix, input_cfg["path"]))


class TestBroker(unittest.TestCase):
    def __on_ready(self, name):
        self.queue.put("ready")

    def __on_gone(self, name):
        self.queue.put("gone")

    def setUp(self):
        self.queue = multiprocessing.Queue()

    def test_callback(self):
        worker_name = b"test_worker"

        port = find_free_port()
        broker_address = "tcp://localhost:{}".format(port)

        broker_p = ZMQBrokerProcess(
            port, VERBOSE_BCP_LOGGING, (self.__on_ready, self.__on_gone)
        )
        broker_p.start()

        worker = ZMQWorkerProcess(broker_address, worker_name, VERBOSE_BCP_LOGGING)
        worker.start()
        worker.join(2)  # Give the worker enough time to announce itself
        worker.terminate()
        worker.join()

        max_rounds = 5
        queue_messages = []
        while max_rounds > 0 and len(queue_messages) < 2:
            max_rounds -= 1
            try:
                message = self.queue.get(block=True, timeout=5)
            except queue.Empty:
                pass
            else:
                queue_messages.append(message)

        broker_p.terminate()
        broker_p.join()

        self.assertEqual(len(queue_messages), 2)
        self.assertEqual(queue_messages[0], "ready")
        self.assertEqual(queue_messages[1], "gone")


class TestBCP(ExecutionTestCase):
    use_docker = False
    docker_images_cache = None

    def setUp(self):
        super().setUp()

        self.worker_name = b"test_worker"

        port = find_free_port()
        broker_address = "tcp://localhost:{}".format(port)

        self.broker_p = ZMQBrokerProcess(port, VERBOSE_BCP_LOGGING)
        self.broker_p.start()

        self.worker = ZMQWorkerProcess(
            broker_address,
            self.worker_name,
            VERBOSE_BCP_LOGGING,
            self.use_docker,
            self.docker_images_cache,
        )
        self.worker.start()

        self.client = BeatComputationClient(broker_address, VERBOSE_BCP_LOGGING)

    def tearDown(self):
        self.worker.terminate()
        self.worker.join()
        self.broker_p.terminate()
        self.broker_p.join()
        self.client = None

    def test_cancel_unknown(self):
        request = [BCP.BCPE_CANCEL, b"1"]
        self.client.send(self.worker_name, request)

        reply = None
        iterations = 0
        while reply is None and iterations < self.MAX_ITERATION_COUNT:
            try:
                reply = self.client.recv()
            except KeyboardInterrupt:
                break
            else:
                iterations += 1

        self.assertTrue(iterations < self.MAX_ITERATION_COUNT)
        self.assertEqual(reply[1], BCP.BCPP_ERROR)
        self.assertEqual(reply[2], b"Unknown job: 1")

    def test_cancel(self):
        self.prepare_databases(CONFIGURATION1)
        job_id = b"1"

        request = [BCP.BCPE_EXECUTE, job_id, json.dumps(CONFIGURATION1).encode("utf-8")]
        self.client.send(self.worker_name, request)

        request = [BCP.BCPE_CANCEL, job_id]
        self.client.send(self.worker_name, request)

        messages = []
        iterations = 0
        while len(messages) < 3 and iterations < self.MAX_ITERATION_COUNT:
            try:
                reply = self.client.recv()
            except KeyboardInterrupt:
                break
            else:
                if reply:
                    messages.append(reply)
                iterations += 1

        self.assertTrue(iterations < self.MAX_ITERATION_COUNT)
        self.assertEqual(messages[0][1], BCP.BCPP_JOB_RECEIVED)
        self.assertEqual(messages[0][2], job_id)
        self.assertEqual(messages[1][1], BCP.BCPP_JOB_STARTED)
        self.assertEqual(messages[1][2], job_id)
        self.assertEqual(messages[2][1], BCP.BCPP_JOB_CANCELLED)
        self.assertEqual(messages[2][2], job_id)

    @flaky(max_runs=3)
    def test_execute(self):
        self.prepare_databases(CONFIGURATION1)
        job_id = b"1"

        request = [BCP.BCPE_EXECUTE, job_id, json.dumps(CONFIGURATION1).encode("utf-8")]
        self.client.send(self.worker_name, request)

        messages = []
        iterations = 0
        while len(messages) < 3 and iterations < self.MAX_ITERATION_COUNT:
            try:
                reply = self.client.recv()
            except KeyboardInterrupt:
                break
            else:
                if reply:
                    messages.append(reply)
                iterations += 1

        self.assertTrue(iterations < self.MAX_ITERATION_COUNT)
        self.assertEqual(messages[0][1], BCP.BCPP_JOB_RECEIVED)
        self.assertEqual(messages[0][2], job_id)
        self.assertEqual(messages[1][1], BCP.BCPP_JOB_STARTED)
        self.assertEqual(messages[1][2], job_id)
        self.assertEqual(messages[2][1], BCP.BCPP_JOB_DONE)
        self.assertEqual(messages[2][2], job_id)
        self.assertEqual(len(messages[2]), 4)


class TestBCPDocker(TestBCP):
    use_docker = True

    @classmethod
    def setUpClass(cls):
        cls.docker_images_cache = os.path.join(tmp_prefix, "docker_images_cache.json")
        cls.host = Host(images_cache=cls.docker_images_cache, raise_on_errors=False)


class TestExecutionProcess(ExecutionTestCase):
    REMOTE_ADDRESS = "ipc://execution_feed"

    def tearDown(self):
        os.remove(self.REMOTE_ADDRESS.split("//")[1])

    def setup_process(self):
        self.prepare_databases(CONFIGURATION1)
        process = ExecutionProcess(
            self.REMOTE_ADDRESS,
            b"1",
            prefix,
            CONFIGURATION1,
            tmp_prefix,
            VERBOSE_BCP_LOGGING,
        )
        process.start()
        return process

    def test_execution_process(self):
        ctx = zmq.Context()
        socket = ctx.socket(zmq.ROUTER)
        socket.linger = 0
        socket.bind(self.REMOTE_ADDRESS)

        poller = zmq.Poller()
        poller.register(socket, zmq.POLLIN)

        process = self.setup_process()

        done = False
        iterations = 0
        messages = []

        while True and iterations < self.MAX_ITERATION_COUNT:
            try:
                items = poller.poll(1000)
            except KeyboardInterrupt:
                break

            if items:
                msg = socket.recv_multipart()
                messages.append(msg)

                result = msg[1]
                if result == BCP.BCPP_JOB_DONE:
                    done = True
                    break
                elif result in [BCP.BCPP_JOB_ERROR, BCP.BCPP_ERROR]:
                    break
            iterations += 1

        process.terminate()
        process.join()
        ctx.destroy()

        self.assertTrue(iterations < self.MAX_ITERATION_COUNT)
        self.assertTrue(done)
        self.assertEqual(process.queue.get(), "started")
        self.assertEqual(messages[0][1], BCP.BCPP_JOB_DONE)

    def test_processor(self):
        poller = zmq.Poller()
        processor = BeatComputationProcessor(
            poller, self.REMOTE_ADDRESS, VERBOSE_BCP_LOGGING
        )

        process = self.setup_process()

        done = False
        iterations = 0

        messages = []

        while True and iterations < self.MAX_ITERATION_COUNT:
            try:
                items = poller.poll(1000)
            except KeyboardInterrupt:
                break

            if items:
                msg = processor.process()
                messages.append(msg)

                result = msg[1]
                if result == BCP.BCPP_JOB_DONE:
                    done = True
                    break
                elif result in [BCP.BCPP_JOB_ERROR, BCP.BCPP_ERROR]:
                    break
            iterations += 1

        process.terminate()
        process.join()

        self.assertTrue(iterations < self.MAX_ITERATION_COUNT)
        self.assertTrue(done)
        self.assertEqual(process.queue.get(), "started")
        self.assertEqual(messages[0][1], BCP.BCPP_JOB_DONE)
