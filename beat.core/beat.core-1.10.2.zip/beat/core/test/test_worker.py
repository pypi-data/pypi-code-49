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
import logging
import unittest
import simplejson as json
import multiprocessing
import queue

from time import time
from time import sleep

from ddt import ddt
from ddt import idata

from ..scripts import worker
from ..worker import WorkerController
from ..database import Database
from ..utils import find_free_port

from . import prefix, tmp_prefix


logger = logging.getLogger(__name__)

# ----------------------------------------------------------


WORKER1 = b"worker1"
WORKER2 = b"worker2"
PORT = find_free_port()


# ----------------------------------------------------------

DATABASES = [f"integers_db/{i}" for i in range(1, 3)]


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


def prepare_database(db_name):
    CONFIGURATION1["inputs"]["in"]["database"] = db_name
    CONFIGURATION2["inputs"]["in"]["database"] = db_name

    for _, input_cfg in CONFIGURATION1["inputs"].items():
        database = Database(prefix, input_cfg["database"])
        view = database.view(input_cfg["protocol"], input_cfg["set"])
        view.index(os.path.join(tmp_prefix, input_cfg["path"]))


# ----------------------------------------------------------


class ControllerProcess(multiprocessing.Process):
    def __init__(self, queue):
        super(ControllerProcess, self).__init__()

        self.queue = queue

    def run(self):
        self.queue.put("STARTED")

        def onWorkerReady(name):
            self.queue.put("READY %s" % name.decode())

        def onWorkerGone(name):
            self.queue.put("GONE %s" % name.decode())

        self.controller = WorkerController(
            "127.0.0.1",
            port=PORT,
            callbacks=dict(onWorkerReady=onWorkerReady, onWorkerGone=onWorkerGone),
        )

        while True:
            self.controller.process(100)

            try:
                command = self.queue.get_nowait()
                if command == "STOP":
                    break
            except queue.Empty:
                pass

        self.controller.destroy()


# ----------------------------------------------------------


class WorkerProcess(multiprocessing.Process):
    def __init__(self, queue, arguments):
        super(WorkerProcess, self).__init__()

        self.queue = queue
        self.arguments = arguments

    def run(self):
        self.queue.put("STARTED")
        worker.main(self.arguments)


# ----------------------------------------------------------


class TestWorkerBase(unittest.TestCase):
    def __init__(self, methodName="runTest"):
        super(TestWorkerBase, self).__init__(methodName)
        self.controller = None
        self.connected_workers = []
        self.worker_processes = {}
        self.docker = False

    def setUp(self):
        self.shutdown_everything()  # In case another test failed badly during its setUp()

    def tearDown(self):
        self.shutdown_everything()

    def shutdown_everything(self):
        for name in list(self.worker_processes.keys()):
            self.stop_worker(name)

        self.worker_processes = {}
        self.connected_workers = []

        self.stop_controller()

    def start_controller(self, port=None):
        self.connected_workers = []

        def onWorkerReady(name):
            self.connected_workers.append(name)

        def onWorkerGone(name):
            self.connected_workers.remove(name)

        self.controller = WorkerController(
            "127.0.0.1",
            port=port,
            callbacks=dict(onWorkerReady=onWorkerReady, onWorkerGone=onWorkerGone),
        )

        self.controller.process(100)

    def stop_controller(self):
        if self.controller is not None:
            self.controller.destroy()
            self.controller = None

    def start_worker(self, name, address=None):
        args = [
            "--prefix=%s" % prefix,
            "--cache=%s" % tmp_prefix,
            "--name=%s" % name.decode(),
            # '-vv',
            self.controller.address if address is None else address,
        ]

        if self.docker:
            args.insert(3, "--docker")

        worker_process = WorkerProcess(multiprocessing.Queue(), args)
        worker_process.start()

        worker_process.queue.get()

        self.worker_processes[name] = worker_process

    def stop_worker(self, name):
        if name in self.worker_processes:
            self.worker_processes[name].terminate()
            self.worker_processes[name].join()
            del self.worker_processes[name]

    def wait_for_worker_connection(self, name, timeout=10):
        start = time()
        while name not in self.connected_workers:
            self.assertTrue(self.controller.process(100) is None)
            self.assertTrue(time() - start < timeout)  # Exit after 'timeout' seconds

        self.assertTrue(name in self.controller.workers)

    def wait_for_worker_disconnection(self, name):
        start = time()
        while name in self.connected_workers:
            self.assertTrue(self.controller.process(100) is None)
            self.assertTrue(time() - start < 10)  # Exit after 10 seconds

        self.assertTrue(name not in self.controller.workers)


# ----------------------------------------------------------


class TestConnection(TestWorkerBase):
    def test_worker_connection(self):
        self.start_controller()

        self.assertEqual(len(self.connected_workers), 0)
        self.assertEqual(len(self.controller.workers), 0)

        self.start_worker(WORKER1)

        self.wait_for_worker_connection(WORKER1)

        self.assertEqual(len(self.connected_workers), 1)
        self.assertEqual(len(self.controller.workers), 1)

    def test_worker_disconnection(self):
        self.start_controller()
        self.start_worker(WORKER1)

        self.wait_for_worker_connection(WORKER1)

        sleep(1)

        self.stop_worker(WORKER1)

        self.wait_for_worker_disconnection(WORKER1)

    def test_two_workers_connection(self):
        self.start_controller()

        self.assertEqual(len(self.connected_workers), 0)
        self.assertEqual(len(self.controller.workers), 0)

        self.start_worker(WORKER1)
        self.start_worker(WORKER2)

        self.wait_for_worker_connection(WORKER1)
        self.wait_for_worker_connection(WORKER2)

        self.assertEqual(len(self.connected_workers), 2)
        self.assertEqual(len(self.controller.workers), 2)

    def test_scheduler_last(self):
        self.start_worker(WORKER1, address="tcp://127.0.0.1:%i" % PORT)
        sleep(1)

        self.start_controller(port=PORT)

        self.wait_for_worker_connection(WORKER1)

    def test_scheduler_shutdown(self):
        controller = ControllerProcess(multiprocessing.Queue())
        controller.start()

        message = controller.queue.get()
        self.assertEqual(message, "STARTED")

        self.start_worker(WORKER1, "tcp://127.0.0.1:%i" % PORT)

        message = controller.queue.get()
        self.assertEqual(message, "READY " + WORKER1.decode())

        controller.queue.put("STOP")

        sleep(1)

        controller = ControllerProcess(multiprocessing.Queue())
        controller.start()

        message = controller.queue.get()
        self.assertEqual(message, "STARTED")

        message = controller.queue.get()
        self.assertEqual(message, "READY " + WORKER1.decode())

        controller.queue.put("STOP")


# ----------------------------------------------------------


@ddt
class TestOneWorker(TestWorkerBase):
    def setUp(self):
        super(TestOneWorker, self).setUp()

        self.start_controller()
        self.start_worker(WORKER1)

        self.wait_for_worker_connection(WORKER1)

    def _wait(self, max=200):
        message = None
        nb = 0

        while (message is None) and (nb < max):
            message = self.controller.process(100)
            nb += 1

        if message is None:
            print("Process failed with the allocate range: {}".format(max))

        return message

    def _check_done(self, message, expected_worker, expected_job_id):
        self.assertIsNotNone(message)

        (worker, status, job_id, data) = message

        self.assertEqual(worker, expected_worker)
        self.assertEqual(status, WorkerController.DONE)
        self.assertEqual(job_id, expected_job_id)

        result = json.loads(data[0])

        self.assertEqual(result["status"], 0)

    @idata(DATABASES)
    def test_success(self, db_name):
        prepare_database(db_name)

        self.controller.execute(WORKER1, 1, CONFIGURATION1)

        message = self._wait()

        self._check_done(message, WORKER1, 1)

    @idata(DATABASES)
    def test_processing_error(self, db_name):
        prepare_database(db_name)

        config = dict(CONFIGURATION1)
        config["algorithm"] = "legacy/process_crash/1"

        self.controller.execute(WORKER1, 1, config)

        message = self._wait()
        self.assertTrue(message is not None)
        (worker, status, job_id, data) = message

        self.assertEqual(worker, WORKER1)
        self.assertEqual(status, WorkerController.JOB_ERROR)
        self.assertEqual(job_id, 1)

        result = json.loads(data[0])

        self.assertEqual(result["status"], 1)
        self.assertTrue("a = b" in result["user_error"])

    @idata(DATABASES)
    def test_error_unknown_algorithm(self, db_name):
        prepare_database(db_name)

        config = dict(CONFIGURATION1)
        config["algorithm"] = "user/unknown/1"

        self.controller.execute(WORKER1, 1, config)

        message = self._wait()
        self.assertTrue(message is not None)
        (worker, status, job_id, data) = message

        self.assertEqual(worker, WORKER1)
        self.assertEqual(status, WorkerController.JOB_ERROR)
        self.assertEqual(job_id, 1)
        self.assertTrue(len(data) > 0)

    @idata(DATABASES)
    def test_error_syntax_error(self, db_name):
        prepare_database(db_name)

        config = dict(CONFIGURATION1)
        config["algorithm"] = "legacy/syntax_error/1"

        self.controller.execute(WORKER1, 1, config)

        message = self._wait()
        self.assertTrue(message is not None)
        (worker, status, job_id, data) = message

        self.assertEqual(worker, WORKER1)
        self.assertTrue(status in [WorkerController.ERROR, WorkerController.JOB_ERROR])
        self.assertEqual(job_id, 1)
        self.assertTrue(len(data) > 0)

    @idata(DATABASES)
    def test_multiple_jobs(self, db_name):
        prepare_database(db_name)

        config = dict(CONFIGURATION1)
        config["algorithm"] = "v1/integers_echo_slow/1"

        self.controller.execute(WORKER1, 1, CONFIGURATION1)
        self.controller.execute(WORKER1, 2, config)

        message = self._wait()
        self._check_done(message, WORKER1, 1)

        message = self._wait()
        self._check_done(message, WORKER1, 2)

    @idata(DATABASES)
    def test_reuse(self, db_name):
        prepare_database(db_name)

        self.controller.execute(WORKER1, 1, CONFIGURATION1)
        message = self._wait()
        self._check_done(message, WORKER1, 1)

        self.controller.execute(WORKER1, 2, CONFIGURATION1)
        message = self._wait()
        self._check_done(message, WORKER1, 2)

    @idata(DATABASES)
    def test_cancel(self, db_name):
        prepare_database(db_name)

        config = dict(CONFIGURATION1)
        config["algorithm"] = "v1/integers_echo_slow/1"

        self.controller.execute(WORKER1, 1, config)
        self.controller.cancel(WORKER1, 1)

        message = self._wait()
        self.assertTrue(message is not None)
        (worker, status, job_id, data) = message

        self.assertEqual(worker, WORKER1)
        self.assertEqual(status, WorkerController.CANCELLED)
        self.assertEqual(job_id, 1)
        self.assertEqual(len(data), 0)

    def test_error_cancel_unknown_job(self):
        self.controller.cancel(WORKER1, 1)

        message = self._wait()
        self.assertTrue(message is not None)
        (worker, status, job_id, data) = message

        self.assertEqual(worker, WORKER1)
        self.assertEqual(status, WorkerController.ERROR)
        self.assertTrue(job_id is None)
        self.assertEqual(data[0].decode(), "Unknown job: 1")


# ----------------------------------------------------------


@ddt
class TestTwoWorkers(TestWorkerBase):
    def setUp(self):
        self.tearDown()  # In case another test failed badly during its setUp()

        super(TestTwoWorkers, self).setUp()

        self.start_controller()
        self.start_worker(WORKER1)
        self.start_worker(WORKER2)
        self.wait_for_worker_connection(WORKER1)
        self.wait_for_worker_connection(WORKER2)

    def _test_success_one_worker(self, worker_name, db_name):
        prepare_database(db_name)

        self.controller.execute(worker_name, 1, CONFIGURATION1)

        message = None
        while message is None:
            message = self.controller.process(100)

        self.assertTrue(message is not None)
        (worker, status, job_id, data) = message

        self.assertEqual(worker, worker_name)
        self.assertEqual(status, WorkerController.DONE)
        self.assertEqual(job_id, 1)

        result = json.loads(data[0])

        self.assertEqual(result["status"], 0)

    @idata(DATABASES)
    def test_success_worker1(self, db_name):
        self._test_success_one_worker(WORKER1, db_name)

    @idata(DATABASES)
    def test_success_worker2(self, db_name):
        self._test_success_one_worker(WORKER2, db_name)

    @idata(DATABASES)
    def test_success_both_workers(self, db_name):
        def _check(worker, status, job_id, data):
            self.assertEqual(status, WorkerController.DONE)

            if worker == WORKER1:
                self.assertEqual(job_id, 1)
            else:
                self.assertEqual(worker, WORKER2)
                self.assertEqual(job_id, 2)

            result = json.loads(data[0])
            self.assertEqual(result["status"], 0)

        prepare_database(db_name)

        self.controller.execute(WORKER1, 1, CONFIGURATION1)
        self.controller.execute(WORKER2, 2, CONFIGURATION2)

        message = None
        while message is None:
            message = self.controller.process(100)

        (worker1, status, job_id, data) = message
        _check(worker1, status, job_id, data)

        message = None
        while message is None:
            message = self.controller.process(100)

        (worker2, status, job_id, data) = message
        _check(worker2, status, job_id, data)

        self.assertNotEqual(worker1, worker2)
