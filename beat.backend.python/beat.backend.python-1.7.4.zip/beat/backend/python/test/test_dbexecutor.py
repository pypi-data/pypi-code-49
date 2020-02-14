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
import zmq
import tempfile
import shutil

from ddt import ddt
from ddt import idata

from ..execution import DBExecutor
from ..execution import MessageHandler
from ..database import Database
from ..data_loaders import DataLoader
from ..data import RemoteDataSource
from ..hash import hashDataset
from ..hash import toPath

from .test_database import INTEGERS_DBS

from . import prefix


# ----------------------------------------------------------


logger = logging.getLogger(__name__)


CONFIGURATION = {
    "queue": "queue",
    "algorithm": "user/sum/1",
    "nb_slots": 1,
    "channel": "integers",
    "parameters": {},
    "environment": {"name": "Python 2.7", "version": "1.2.0"},
    "inputs": {
        "a": {
            "database": "integers_db/1",
            "protocol": "double",
            "set": "double",
            "output": "a",
            "endpoint": "a",
            "channel": "integers",
            "path": None,
            "hash": None,
        },
        "b": {
            "database": "integers_db/1",
            "protocol": "double",
            "set": "double",
            "output": "b",
            "endpoint": "b",
            "channel": "integers",
            "path": None,
            "hash": None,
        },
    },
    "outputs": {
        "sum": {
            "endpoint": "sum",
            "channel": "integers",
            "path": "20/61/b6/2df3c3bedd5366f4a625c5d87ffbf5a26007c46c456e9abf21b46c6681",
            "hash": "2061b62df3c3bedd5366f4a625c5d87ffbf5a26007c46c456e9abf21b46c6681",
        }
    },
}


# ----------------------------------------------------------


@ddt
class TestExecution(unittest.TestCase):
    def setUp(self):
        self.cache_root = tempfile.mkdtemp(prefix=__name__)

        for db_name in INTEGERS_DBS:
            database = Database(prefix, db_name)
            view = database.view("double", "double")
            db_view_hash = hashDataset(db_name, "double", "double")
            db_index_path = toPath(db_view_hash, suffix=".db")

            view.index(os.path.join(self.cache_root, db_index_path))

        self.db_executor = None
        self.client_context = None
        self.client_socket = None

    def tearDown(self):
        if self.client_socket is not None:
            self.client_socket.send_string("don")

        if self.db_executor is not None:
            self.db_executor.wait()

        if self.client_socket is not None:
            self.client_socket.setsockopt(zmq.LINGER, 0)
            self.client_socket.close()
            self.client_context.destroy()

        shutil.rmtree(self.cache_root)

    @idata(INTEGERS_DBS)
    def test_success(self, db_name):
        message_handler = MessageHandler("127.0.0.1")

        for input_ in ["a", "b"]:
            db_view_hash = hashDataset(db_name, "double", "double")
            db_index_path = toPath(db_view_hash, suffix=".db")

            CONFIGURATION["inputs"][input_]["database"] = db_name
            CONFIGURATION["inputs"][input_]["path"] = db_index_path
            CONFIGURATION["inputs"][input_]["hash"] = db_view_hash

        self.db_executor = DBExecutor(
            message_handler, prefix, self.cache_root, CONFIGURATION
        )

        self.assertTrue(self.db_executor.valid)

        self.db_executor.process()

        self.client_context = zmq.Context()
        self.client_socket = self.client_context.socket(zmq.PAIR)
        self.client_socket.connect(self.db_executor.address)

        data_loader = DataLoader(CONFIGURATION["channel"])

        database = Database(prefix, db_name)

        for input_name, input_conf in CONFIGURATION["inputs"].items():
            dataformat_name = database.set(input_conf["protocol"], input_conf["set"])[
                "outputs"
            ][input_conf["output"]]

            data_source = RemoteDataSource()
            data_source.setup(self.client_socket, input_name, dataformat_name, prefix)
            data_loader.add(input_name, data_source)

        self.assertEqual(data_loader.count("a"), 9)
        self.assertEqual(data_loader.count("b"), 9)
