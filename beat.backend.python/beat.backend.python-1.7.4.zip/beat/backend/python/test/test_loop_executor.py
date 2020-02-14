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
import simplejson
import numpy as np

from copy import deepcopy

from ..execution import AlgorithmExecutor
from ..execution import LoopExecutor
from ..execution import MessageHandler
from ..execution import LoopMessageHandler
from ..exceptions import RemoteException

from ..algorithm import Algorithm
from ..dataformat import DataFormat
from ..data import CachedDataSink
from ..data import CachedDataSource

from ..helpers import convert_experiment_configuration_to_container

from . import prefix


logger = logging.getLogger(__name__)


# ----------------------------------------------------------


CONFIGURATION = {
    "algorithm": "",
    "channel": "main",
    "parameters": {},
    "inputs": {"in_main": {"path": "INPUT", "channel": "main"}},
    "outputs": {"out_main": {"path": "OUTPUT_MAIN", "channel": "main"}},
    "loop": {
        "algorithm": "",
        "channel": "main",
        "parameters": {"threshold": 1},
        "inputs": {"in_loop": {"path": "INPUT_LOOP", "channel": "main"}},
        "outputs": {"out_loop": {"path": "LOOP_OUTPUT", "channel": "main"}},
    },
}


# ----------------------------------------------------------


class TestExecution(unittest.TestCase):
    def setUp(self):
        self.cache_root = tempfile.mkdtemp(prefix=__name__)
        self.working_dir = tempfile.mkdtemp(prefix=__name__)

        self.message_handler = None
        self.loop_message_handler = None
        self.executor_socket = None
        self.loop_executor = None
        self.loop_socket = None
        self.zmq_context = None

    def tearDown(self):
        shutil.rmtree(self.cache_root)
        shutil.rmtree(self.working_dir)

        self.loop_socket.send_string("don")
        if self.loop_executor:
            self.loop_socket.send_string("don")
            self.loop_executor.wait()

        for handler in [self.message_handler, self.loop_message_handler]:
            if handler is not None:
                handler.kill()
                handler.join()
                handler.destroy()
                handler = None

        for socket in [self.executor_socket, self.loop_socket]:
            if socket is not None:
                socket.setsockopt(zmq.LINGER, 0)
                socket.close()
                socket = None

        self.zmq_context.destroy()
        self.zmq_context = None

    def writeData(self, config, input_name, indices, start_value):
        filename = os.path.join(
            self.cache_root, config["inputs"][input_name]["path"] + ".data"
        )
        dataformat = DataFormat(prefix, "user/single_integer/1")
        self.assertTrue(dataformat.valid)

        data_sink = CachedDataSink()
        self.assertTrue(
            data_sink.setup(filename, dataformat, indices[0][0], indices[-1][1])
        )

        for i in indices:
            data = dataformat.type()
            data.value = np.int32(start_value + i[0])
            data_sink.write(data, i[0], i[1])

        (nb_bytes, duration) = data_sink.statistics()
        self.assertTrue(nb_bytes > 0)
        self.assertTrue(duration > 0)

        data_sink.close()
        del data_sink

    def process(self, algorithm_name, loop_algorithm_name):

        self.writeData(CONFIGURATION, "in_main", [(0, 0), (1, 1), (2, 2), (3, 3)], 1000)
        self.writeData(
            CONFIGURATION["loop"], "in_loop", [(0, 0), (1, 1), (2, 2), (3, 3)], 1000
        )

        # -------------------------------------------------------------------------

        config = deepcopy(CONFIGURATION)
        config["algorithm"] = algorithm_name
        config["loop"]["algorithm"] = loop_algorithm_name

        config = convert_experiment_configuration_to_container(config)

        with open(os.path.join(self.working_dir, "configuration.json"), "wb") as f:
            data = simplejson.dumps(config, indent=4).encode("utf-8")
            f.write(data)

        working_prefix = os.path.join(self.working_dir, "prefix")
        if not os.path.exists(working_prefix):
            os.makedirs(working_prefix)

        algorithm = Algorithm(prefix, algorithm_name)
        self.assertTrue(algorithm.valid, algorithm.errors)
        algorithm.export(working_prefix)

        # -------------------------------------------------------------------------

        loop_algorithm = Algorithm(prefix, loop_algorithm_name)
        self.assertTrue(loop_algorithm.valid, loop_algorithm.errors)
        loop_algorithm.export(working_prefix)

        # -------------------------------------------------------------------------

        self.message_handler = MessageHandler("127.0.0.1")
        self.message_handler.start()
        self.loop_message_handler = LoopMessageHandler("127.0.0.1")

        self.zmq_context = zmq.Context()
        self.executor_socket = self.zmq_context.socket(zmq.PAIR)
        self.executor_socket.connect(self.message_handler.address)
        self.loop_socket = self.zmq_context.socket(zmq.PAIR)
        self.loop_socket.connect(self.loop_message_handler.address)

        self.loop_executor = LoopExecutor(
            self.loop_message_handler, self.working_dir, cache_root=self.cache_root
        )
        self.assertTrue(self.loop_executor.setup())
        self.assertTrue(self.loop_executor.prepare())
        self.loop_executor.process()

        executor = AlgorithmExecutor(
            self.executor_socket,
            self.working_dir,
            cache_root=self.cache_root,
            loop_socket=self.loop_socket,
        )

        self.assertTrue(executor.setup())
        self.assertTrue(executor.prepare())
        self.assertTrue(executor.process())

        self.loop_executor.close()

        cached_file = CachedDataSource()
        self.assertTrue(
            cached_file.setup(
                os.path.join(
                    self.cache_root,
                    CONFIGURATION["outputs"]["out_main"]["path"] + ".data",
                ),
                prefix,
            )
        )

        for i in range(len(cached_file)):
            data, start, end = cached_file[i]
            self.assertEqual(data.value, 1000 + i)
            self.assertEqual(start, i)
            self.assertEqual(end, i)

        cached_file = CachedDataSource()
        success = cached_file.setup(
            os.path.join(
                self.cache_root,
                CONFIGURATION["loop"]["outputs"]["out_loop"]["path"] + ".data",
            ),
            prefix,
        )

        self.assertTrue(success)
        for i in range(len(cached_file)):
            data, start, end = cached_file[i]
            self.assertEqual(data.value, 1)
            self.assertEqual(start, i)
            self.assertEqual(end, i)

    def test_autonomous_loop_processor(self):
        self.process("autonomous/loop_processor/1", "autonomous/loop_evaluator/1")

    def test_sequential_loop_processor(self):
        self.process("sequential/loop_processor/1", "sequential/loop_evaluator/1")

    def test_autonomous_loop_invalid_validate_output(self):
        with self.assertRaises(RemoteException):
            self.process(
                "autonomous/loop_processor/1",
                "autonomous/invalid_loop_validate_output/1",
            )
