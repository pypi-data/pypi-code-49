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
import socket
import logging

import unittest
import json
import multiprocessing
import tempfile
import shutil
import zmq

from ddt import ddt
from ddt import idata

from contextlib import closing

from ..scripts import databases_provider
from ..database import Database
from ..data import RemoteDataSource
from ..data import RemoteException

from .test_database import INTEGERS_DBS

from . import prefix


logger = logging.getLogger(__name__)


# ----------------------------------------------------------


CONFIGURATION = {
    "queue": "queue",
    "inputs": {
        "in_data": {
            "set": "double",
            "protocol": "double",
            "database": "integers_db/1",
            "output": "a",
            "path": "ec/89/e5/6e161d2cb012ef6ac8acf59bf453a6328766f90dc9baba9eb14ea23c55",
            "endpoint": "a",
            "hash": "ec89e56e161d2cb012ef6ac8acf59bf453a6328766f90dc9baba9eb14ea23c55",
            "channel": "integers",
        }
    },
    "algorithm": "user/integers_echo/1",
    "parameters": {},
    "environment": {"name": "Python 2.7", "version": "1.2.0"},
    "outputs": {
        "out_data": {
            "path": "20/61/b6/2df3c3bedd5366f4a625c5d87ffbf5a26007c46c456e9abf21b46c6681",
            "endpoint": "out_data",
            "hash": "2061b62df3c3bedd5366f4a625c5d87ffbf5a26007c46c456e9abf21b46c6681",
            "channel": "integers",
        }
    },
    "nb_slots": 1,
    "channel": "integers",
}


# ----------------------------------------------------------


CONFIGURATION_ERROR = {
    "queue": "queue",
    "inputs": {
        "in_data": {
            "set": "get_crashes",
            "protocol": "protocol",
            "database": "crash/1",
            "output": "out",
            "path": "ec/89/e5/6e161d2cb012ef6ac8acf59bf453a6328766f90dc9baba9eb14ea23c55",
            "endpoint": "in",
            "hash": "ec89e56e161d2cb012ef6ac8acf59bf453a6328766f90dc9baba9eb14ea23c55",
            "channel": "set",
        }
    },
    "algorithm": "user/integers_echo/1",
    "parameters": {},
    "environment": {"name": "Python 2.7", "version": "1.2.0"},
    "outputs": {
        "out_data": {
            "path": "20/61/b6/2df3c3bedd5366f4a625c5d87ffbf5a26007c46c456e9abf21b46c6681",
            "endpoint": "out_data",
            "hash": "2061b62df3c3bedd5366f4a625c5d87ffbf5a26007c46c456e9abf21b46c6681",
            "channel": "set",
        }
    },
    "nb_slots": 1,
    "channel": "set",
}


# ----------------------------------------------------------


class DatabasesProviderProcess(multiprocessing.Process):
    def __init__(self, queue, arguments):
        super(DatabasesProviderProcess, self).__init__()

        self.queue = queue
        self.arguments = arguments

    def run(self):
        self.queue.put("STARTED")
        databases_provider.main(self.arguments)


# ----------------------------------------------------------


@ddt
class TestDatabasesProvider(unittest.TestCase):
    def __init__(self, methodName="runTest"):
        super(TestDatabasesProvider, self).__init__(methodName)
        self.databases_provider_process = None
        self.working_dir = None
        self.cache_root = None
        self.data_source = None
        self.client_context = None
        self.client_socket = None

    def setUp(self):
        self.shutdown_everything()  # In case another test failed badly during its setUp()
        self.working_dir = tempfile.mkdtemp(prefix=__name__)
        self.cache_root = tempfile.mkdtemp(prefix=__name__)

    def tearDown(self):
        self.shutdown_everything()

        shutil.rmtree(self.working_dir)
        shutil.rmtree(self.cache_root)

        self.working_dir = None
        self.cache_root = None
        self.data_source = None

        if self.client_socket is not None:
            self.client_socket.setsockopt(zmq.LINGER, 0)
            self.client_socket.close()
            self.client_context.destroy()

    def shutdown_everything(self):
        self.stop_databases_provider()

    def start_databases_provider(self, configuration):
        with open(os.path.join(self.working_dir, "configuration.json"), "wb") as f:
            data = json.dumps(configuration, indent=4)
            f.write(data.encode("utf-8"))

        working_prefix = os.path.join(self.working_dir, "prefix")
        if not os.path.exists(working_prefix):
            os.makedirs(working_prefix)

        input_name, input_cfg = list(configuration["inputs"].items())[0]

        database = Database(prefix, input_cfg["database"])
        database.export(working_prefix)

        view = database.view(input_cfg["protocol"], input_cfg["set"])
        view.index(os.path.join(self.cache_root, input_cfg["path"]))

        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            s.bind(("", 0))
            port = s.getsockname()[1]

        address = "127.0.0.1:%i" % port
        args = [address, self.working_dir, self.cache_root]

        self.databases_provider_process = DatabasesProviderProcess(
            multiprocessing.Queue(), args
        )
        self.databases_provider_process.start()

        self.databases_provider_process.queue.get()

        self.client_context = zmq.Context()
        self.client_socket = self.client_context.socket(zmq.PAIR)
        self.client_socket.connect("tcp://%s" % address)

        dataformat_name = database.set(input_cfg["protocol"], input_cfg["set"])[
            "outputs"
        ][input_cfg["output"]]

        self.data_source = RemoteDataSource()
        self.data_source.setup(self.client_socket, input_name, dataformat_name, prefix)

    def stop_databases_provider(self):
        if self.databases_provider_process is not None:
            self.databases_provider_process.terminate()
            self.databases_provider_process.join()
            del self.databases_provider_process
            self.databases_provider_process = None

    @idata(INTEGERS_DBS)
    def test_success(self, db_name):
        CONFIGURATION["inputs"]["in_data"]["database"] = db_name
        self.start_databases_provider(CONFIGURATION)

        self.assertEqual(len(self.data_source), 9)

        for i in range(0, 9):
            (data, start_index, end_index) = self.data_source[i]
            self.assertEqual(start_index, i)
            self.assertEqual(end_index, i)
            self.assertEqual(data.value, i + 1)

    def test_error(self):
        self.start_databases_provider(CONFIGURATION_ERROR)

        self.assertEqual(len(self.data_source), 1)

        with self.assertRaises(RemoteException):
            (data, start_index, end_index) = self.data_source[0]
