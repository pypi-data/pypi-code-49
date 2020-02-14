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


import logging
logger = logging.getLogger(__name__)

import unittest
import zmq
import os
import glob
import tempfile
import numpy as np

from ..execution import MessageHandler
from ..dataformat import DataFormat
from ..inputs import Input
from ..inputs import InputGroup
from ..inputs import InputList
from ..data import RemoteException
from ..data import CachedDataSource
from ..data import RemoteDataSource
from ..data import CachedDataSink
from ..data_loaders import DataLoader

from .mocks import CrashingDataSource
from . import prefix


#----------------------------------------------------------


class TestMessageHandlerBase(unittest.TestCase):

    def setUp(self):
        self.filenames = []
        self.data_loader = None


    def tearDown(self):
        for filename in self.filenames:
            basename, ext = os.path.splitext(filename)
            filenames = [filename]
            filenames += glob.glob(basename + '*')
            for filename in filenames:
                if os.path.exists(filename):
                    os.unlink(filename)

        self.message_handler.kill()
        self.message_handler.join()
        self.message_handler = None

        self.client_socket.close()
        self.client_context.destroy()

        self.data_loader = None


    def create_data_loader(self, data_sources):
        self.client_context = zmq.Context()

        self.message_handler = MessageHandler('127.0.0.1', data_sources=data_sources, context=self.client_context)
        self.message_handler.start()

        self.client_socket = self.client_context.socket(zmq.PAIR)
        self.client_socket.connect(self.message_handler.address)

        self.data_loader = DataLoader('channel')

        for input_name in data_sources.keys():
            data_source = RemoteDataSource()
            data_source.setup(self.client_socket, input_name, 'user/single_integer/1', prefix)
            self.data_loader.add(input_name, data_source)


    def writeData(self, start_index=0, end_index=10, step=1, base=0):
        testfile = tempfile.NamedTemporaryFile(prefix=__name__, suffix='.data')
        testfile.close() # preserve only the name
        filename = testfile.name

        self.filenames.append(filename)

        dataformat = DataFormat(prefix, 'user/single_integer/1')
        self.assertTrue(dataformat.valid)

        data_sink = CachedDataSink()
        self.assertTrue(data_sink.setup(filename, dataformat, start_index, end_index))

        index = start_index
        while index + step - 1 <= end_index:
            data = dataformat.type()
            data.value = np.int32(index + base)
            data_sink.write(data, index, index + step - 1)
            index += step

        (nb_bytes, duration) = data_sink.statistics()
        self.assertTrue(nb_bytes > 0)
        self.assertTrue(duration > 0)

        data_sink.close()
        del data_sink

        cached_file = CachedDataSource()
        cached_file.setup(filename, prefix)

        self.assertTrue(len(cached_file.infos) > 0)

        return cached_file


#----------------------------------------------------------


class TestOneDataSource(TestMessageHandlerBase):

    def setUp(self):
        super(TestOneDataSource, self).setUp()

        data_sources = {}
        data_sources['a'] = self.writeData(start_index=0, end_index=9)

        self.create_data_loader(data_sources)


    def test_iteration(self):
        self.assertEqual(self.data_loader.count('a'), 10)

        for i in range(10):
            (result, start, end) = self.data_loader[i]
            self.assertEqual(start, i)
            self.assertEqual(end, i)
            self.assertEqual(result['a'].value, i)


#----------------------------------------------------------


class TestSameFrequencyDataSources(TestMessageHandlerBase):

    def setUp(self):
        super(TestSameFrequencyDataSources, self).setUp()

        data_sources = {}
        data_sources['a'] = self.writeData(start_index=0, end_index=9)
        data_sources['b'] = self.writeData(start_index=0, end_index=9, base=10)

        self.create_data_loader(data_sources)


    def test_iteration(self):
        self.assertEqual(self.data_loader.count('a'), 10)
        self.assertEqual(self.data_loader.count('b'), 10)

        for i in range(10):
            (result, start, end) = self.data_loader[i]
            self.assertEqual(start, i)
            self.assertEqual(end, i)
            self.assertEqual(result['a'].value, i)
            self.assertEqual(result['b'].value, 10 + i)


#----------------------------------------------------------


class TestDifferentFrequenciesDataSources(TestMessageHandlerBase):

    def setUp(self):
        super(TestDifferentFrequenciesDataSources, self).setUp()

        data_sources = {}
        data_sources['a'] = self.writeData(start_index=0, end_index=9)
        data_sources['b'] = self.writeData(start_index=0, end_index=9, base=10, step=5)

        self.create_data_loader(data_sources)


    def test_iteration(self):
        self.assertEqual(self.data_loader.count('a'), 10)
        self.assertEqual(self.data_loader.count('b'), 2)

        for i in range(10):
            (result, start, end) = self.data_loader[i]
            self.assertEqual(start, i)
            self.assertEqual(end, i)
            self.assertEqual(result['a'].value, i)

            if i < 5:
                self.assertEqual(result['b'].value, 10)
            else:
                self.assertEqual(result['b'].value, 15)


#----------------------------------------------------------


class TestCrashingDataSource(TestMessageHandlerBase):

    def setUp(self):
        super(TestCrashingDataSource, self).setUp()

        data_sources = {}
        data_sources['a'] = CrashingDataSource()

        self.create_data_loader(data_sources)


    def test_crash(self):
        with self.assertRaises(RemoteException):
            (result, start, end) = self.data_loader[0]
