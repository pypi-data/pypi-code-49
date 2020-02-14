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


import unittest
import logging
import tempfile
import simplejson
import os
import zmq
import shutil
import numpy as np
from copy import deepcopy

from ..execution import AlgorithmExecutor
from ..execution import MessageHandler
from ..inputs import InputList
from ..algorithm import Algorithm
from ..dataformat import DataFormat
from ..data import CachedDataSink
from ..data import CachedDataSource
from ..helpers import convert_experiment_configuration_to_container
from ..helpers import AccessMode

from . import prefix
from .mocks import MockLoggingHandler


CONFIGURATION = {
    'algorithm': '',
    'channel': 'main',
    'parameters': {
    },
    'inputs': {
        'in': {
            'path': 'INPUT',
            'channel': 'main',
        }
    },
    'outputs': {
        'out': {
            'path': 'OUTPUT',
            'channel': 'main'
        }
    },
}


#----------------------------------------------------------


class TestAlgorithmExecutor(unittest.TestCase):

    def setUp(self):
        self.cache_root = tempfile.mkdtemp(prefix=__name__)
        self.working_dir = tempfile.mkdtemp(prefix=__name__)
        self.message_handler = None
        self.executor_socket = None
        self.zmq_context = None


    def tearDown(self):
        shutil.rmtree(self.cache_root)
        shutil.rmtree(self.working_dir)

        if self.message_handler is not None:
            self.message_handler.kill()
            self.message_handler.join()
            self.message_handler.destroy()
            self.message_handler = None

        if self.executor_socket is not None:
            self.executor_socket.setsockopt(zmq.LINGER, 0)
            self.executor_socket.close()
            self.zmq_context.destroy()
            self.executor_socket = None
            self.zmq_context = None


    def writeData(self, input_name, indices, start_value):
        filename = os.path.join(self.cache_root, CONFIGURATION['inputs'][input_name]['path'] + '.data')

        dataformat = DataFormat(prefix, 'user/single_integer/1')
        self.assertTrue(dataformat.valid)

        data_sink = CachedDataSink()
        self.assertTrue(data_sink.setup(filename, dataformat, indices[0][0], indices[-1][1]))

        for i in indices:
            data = dataformat.type()
            data.value = np.int32(start_value + i[0])
            data_sink.write(data, i[0], i[1])

        (nb_bytes, duration) = data_sink.statistics()
        self.assertTrue(nb_bytes > 0)
        self.assertTrue(duration > 0)

        data_sink.close()
        del data_sink


    def process(self, algorithm_name):
        self.writeData('in', [(0, 0), (1, 1), (2, 2), (3, 3)], 1000)

        config = deepcopy(CONFIGURATION)
        config['algorithm'] = algorithm_name
        config = convert_experiment_configuration_to_container(config)

        with open(os.path.join(self.working_dir, 'configuration.json'), 'wb') as f:
            data = simplejson.dumps(config, indent=4).encode('utf-8')
            f.write(data)

        working_prefix = os.path.join(self.working_dir, 'prefix')
        if not os.path.exists(working_prefix):
            os.makedirs(working_prefix)

        algorithm = Algorithm(prefix, algorithm_name)
        algorithm.export(working_prefix)

        self.message_handler = MessageHandler('127.0.0.1')

        self.message_handler.start()

        self.zmq_context = zmq.Context()
        self.executor_socket = self.zmq_context.socket(zmq.PAIR)
        self.executor_socket.connect(self.message_handler.address)

        executor = AlgorithmExecutor(self.executor_socket, self.working_dir, cache_root=self.cache_root)

        self.assertTrue(executor.setup())
        self.assertTrue(executor.prepare())
        self.assertTrue(executor.process())

        cached_file = CachedDataSource()
        self.assertTrue(cached_file.setup(os.path.join(self.cache_root, CONFIGURATION['outputs']['out']['path'] + '.data'), prefix))

        for i in range(len(cached_file)):
            data, start, end = cached_file[i]
            self.assertEqual(data.value, 1000 + i)
            self.assertEqual(start, i)
            self.assertEqual(end, i)


    def test_legacy_echo_1(self):
        log_handler = MockLoggingHandler(level='DEBUG')
        logging.getLogger().addHandler(log_handler)
        log_messages = log_handler.messages

        self.process('legacy/echo/1')

        info_len = len(log_messages['warning'])
        self.assertEqual(info_len, 1)
        self.assertEqual(log_messages['warning'][info_len - 1], 'legacy/echo/1 is using LEGACY I/O API, please upgrade this algorithm as soon as possible')


    def test_sequential_echo_1(self):
        self.process('sequential/echo/1')


    def test_autonomous_echo_1(self):
        self.process('autonomous/echo/1')
