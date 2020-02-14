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
import os
import glob
import tempfile
import numpy as np

from ..data_loaders import DataLoader
from ..data_loaders import DataLoaderList
from ..dataformat import DataFormat
from ..data import CachedDataSink
from ..data import CachedDataSource

from . import prefix


#----------------------------------------------------------


class DataLoaderBaseTest(unittest.TestCase):

    def setUp(self):
        self.filenames = {}


    def tearDown(self):
        for f in self.filenames.values():
            basename, ext = os.path.splitext(f)
            filenames = [f]
            filenames += glob.glob(basename + '*')
            for filename in filenames:
                if os.path.exists(filename):
                    os.unlink(filename)


    def writeData(self, input_name, indices, start_value):
        testfile = tempfile.NamedTemporaryFile(prefix=__name__ + input_name, suffix='.data')
        testfile.close() # preserve only the name
        self.filenames[input_name] = testfile.name

        dataformat = DataFormat(prefix, 'user/single_integer/1')
        self.assertTrue(dataformat.valid)

        data_sink = CachedDataSink()
        self.assertTrue(data_sink.setup(self.filenames[input_name], dataformat,
                                        indices[0][0], indices[-1][1]))

        for i in indices:
            data = dataformat.type()
            data.value = np.int32(start_value + i[0])
            data_sink.write(data, i[0], i[1])

        (nb_bytes, duration) = data_sink.statistics()
        self.assertTrue(nb_bytes > 0)
        self.assertTrue(duration > 0)

        data_sink.close()
        del data_sink


#----------------------------------------------------------


class DataLoaderTest(DataLoaderBaseTest):

    def test_creation(self):
        data_loader = DataLoader('channel1')

        self.assertEqual(data_loader.channel, 'channel1')
        self.assertEqual(data_loader.nb_data_units, 0)
        self.assertEqual(data_loader.data_index_start, -1)
        self.assertEqual(data_loader.data_index_end, -1)
        self.assertEqual(data_loader.count(), 0)


    def test_empty(self):
        data_loader = DataLoader('channel1')

        self.assertEqual(data_loader.count(), 0)
        self.assertEqual(data_loader[0], (None, None, None))
        self.assertTrue(data_loader.view('unknown', 0) is None)


    def test_one_input(self):

        # Setup
        self.writeData('input1', [(0, 0), (1, 1), (2, 2)], 1000)

        data_loader = DataLoader('channel1')

        cached_file = CachedDataSource()
        cached_file.setup(self.filenames['input1'], prefix)
        data_loader.add('input1', cached_file)


        # Global checks
        self.assertEqual(data_loader.count(), 3)
        self.assertEqual(data_loader.count('input1'), 3)

        self.assertEqual(data_loader.data_index_start, 0)
        self.assertEqual(data_loader.data_index_end, 2)


        # Indexing
        (data, start, end) = data_loader[-1]
        self.assertTrue(data is None)

        (data, start, end) = data_loader[0]
        self.assertTrue(data is not None)
        self.assertEqual(start, 0)
        self.assertEqual(end, 0)
        self.assertEqual(data['input1'].value, 1000)

        (data, start, end) = data_loader[1]
        self.assertTrue(data is not None)
        self.assertEqual(start, 1)
        self.assertEqual(end, 1)
        self.assertEqual(data['input1'].value, 1001)

        (data, start, end) = data_loader[2]
        self.assertTrue(data is not None)
        self.assertEqual(start, 2)
        self.assertEqual(end, 2)
        self.assertEqual(data['input1'].value, 1002)

        (data, start, end) = data_loader[3]
        self.assertTrue(data is None)


        # View 'input1', index -1
        view = data_loader.view('input1', -1)
        self.assertTrue(view is None)


        # View 'input1', index 0
        view = data_loader.view('input1', 0)

        self.assertEqual(view.count(), 1)
        self.assertEqual(view.count('input1'), 1)

        self.assertEqual(view.data_index_start, 0)
        self.assertEqual(view.data_index_end, 0)

        (data, start, end) = view[-1]
        self.assertTrue(data is None)

        (data, start, end) = view[0]
        self.assertTrue(data is not None)
        self.assertEqual(start, 0)
        self.assertEqual(end, 0)
        self.assertEqual(data['input1'].value, 1000)

        (data, start, end) = view[1]
        self.assertTrue(data is None)


        # View 'input1', index 1
        view = data_loader.view('input1', 1)

        self.assertEqual(view.count(), 1)
        self.assertEqual(view.count('input1'), 1)

        self.assertEqual(view.data_index_start, 1)
        self.assertEqual(view.data_index_end, 1)

        (data, start, end) = view[-1]
        self.assertTrue(data is None)

        (data, start, end) = view[0]
        self.assertTrue(data is not None)
        self.assertEqual(start, 1)
        self.assertEqual(end, 1)
        self.assertEqual(data['input1'].value, 1001)

        (data, start, end) = view[1]
        self.assertTrue(data is None)


        # View 'input1', index 2
        view = data_loader.view('input1', 2)

        self.assertEqual(view.count(), 1)
        self.assertEqual(view.count('input1'), 1)

        self.assertEqual(view.data_index_start, 2)
        self.assertEqual(view.data_index_end, 2)

        (data, start, end) = view[-1]
        self.assertTrue(data is None)

        (data, start, end) = view[0]
        self.assertTrue(data is not None)
        self.assertEqual(start, 2)
        self.assertEqual(end, 2)
        self.assertEqual(data['input1'].value, 1002)

        (data, start, end) = view[1]
        self.assertTrue(data is None)


        # View 'input1', index 3
        view = data_loader.view('input1', 3)
        self.assertTrue(view is None)


    def test_two_synchronized_inputs(self):

        # Setup
        self.writeData('input1', [(0, 0), (1, 1), (2, 2), (3, 3)], 1000)
        self.writeData('input2', [(0, 1), (2, 3)], 2000)

        data_loader = DataLoader('channel1')

        cached_file = CachedDataSource()
        cached_file.setup(self.filenames['input1'], prefix)
        data_loader.add('input1', cached_file)

        cached_file = CachedDataSource()
        cached_file.setup(self.filenames['input2'], prefix)
        data_loader.add('input2', cached_file)


        # Global checks
        self.assertEqual(data_loader.count(), 4)
        self.assertEqual(data_loader.count('input1'), 4)
        self.assertEqual(data_loader.count('input2'), 2)

        self.assertEqual(data_loader.data_index_start, 0)
        self.assertEqual(data_loader.data_index_end, 3)


        # Indexing
        (data, start, end) = data_loader[-1]
        self.assertTrue(data is None)

        (data, start, end) = data_loader[0]
        self.assertTrue(data is not None)
        self.assertEqual(start, 0)
        self.assertEqual(end, 0)
        self.assertEqual(data['input1'].value, 1000)
        self.assertEqual(data['input2'].value, 2000)

        (data, start, end) = data_loader[1]
        self.assertTrue(data is not None)
        self.assertEqual(start, 1)
        self.assertEqual(end, 1)
        self.assertEqual(data['input1'].value, 1001)
        self.assertEqual(data['input2'].value, 2000)

        (data, start, end) = data_loader[2]
        self.assertTrue(data is not None)
        self.assertEqual(start, 2)
        self.assertEqual(end, 2)
        self.assertEqual(data['input1'].value, 1002)
        self.assertEqual(data['input2'].value, 2002)

        (data, start, end) = data_loader[3]
        self.assertTrue(data is not None)
        self.assertEqual(start, 3)
        self.assertEqual(end, 3)
        self.assertEqual(data['input1'].value, 1003)
        self.assertEqual(data['input2'].value, 2002)

        (data, start, end) = data_loader[4]
        self.assertTrue(data is None)


        # View 'input1', index -1
        view = data_loader.view('input1', -1)
        self.assertTrue(view is None)


        # View 'input1', index 0
        view = data_loader.view('input1', 0)

        self.assertEqual(view.count(), 1)
        self.assertEqual(view.count('input1'), 1)
        self.assertEqual(view.count('input2'), 1)

        self.assertEqual(view.data_index_start, 0)
        self.assertEqual(view.data_index_end, 0)

        (data, start, end) = view[-1]
        self.assertTrue(data is None)

        (data, start, end) = view[0]
        self.assertTrue(data is not None)
        self.assertEqual(start, 0)
        self.assertEqual(end, 0)
        self.assertEqual(data['input1'].value, 1000)
        self.assertEqual(data['input2'].value, 2000)

        (data, start, end) = view[1]
        self.assertTrue(data is None)


        # View 'input1', index 1
        view = data_loader.view('input1', 1)

        self.assertEqual(view.count(), 1)
        self.assertEqual(view.count('input1'), 1)
        self.assertEqual(view.count('input2'), 1)

        self.assertEqual(view.data_index_start, 1)
        self.assertEqual(view.data_index_end, 1)

        (data, start, end) = view[-1]
        self.assertTrue(data is None)

        (data, start, end) = view[0]
        self.assertTrue(data is not None)
        self.assertEqual(start, 1)
        self.assertEqual(end, 1)
        self.assertEqual(data['input1'].value, 1001)
        self.assertEqual(data['input2'].value, 2000)

        (data, start, end) = view[1]
        self.assertTrue(data is None)


        # View 'input1', index 2
        view = data_loader.view('input1', 2)

        self.assertEqual(view.count(), 1)
        self.assertEqual(view.count('input1'), 1)
        self.assertEqual(view.count('input2'), 1)

        self.assertEqual(view.data_index_start, 2)
        self.assertEqual(view.data_index_end, 2)

        (data, start, end) = view[-1]
        self.assertTrue(data is None)

        (data, start, end) = view[0]
        self.assertTrue(data is not None)
        self.assertEqual(start, 2)
        self.assertEqual(end, 2)
        self.assertEqual(data['input1'].value, 1002)
        self.assertEqual(data['input2'].value, 2002)

        (data, start, end) = view[1]
        self.assertTrue(data is None)


        # View 'input1', index 3
        view = data_loader.view('input1', 3)

        self.assertEqual(view.count(), 1)
        self.assertEqual(view.count('input1'), 1)
        self.assertEqual(view.count('input2'), 1)

        self.assertEqual(view.data_index_start, 3)
        self.assertEqual(view.data_index_end, 3)

        (data, start, end) = view[-1]
        self.assertTrue(data is None)

        (data, start, end) = view[0]
        self.assertTrue(data is not None)
        self.assertEqual(start, 3)
        self.assertEqual(end, 3)
        self.assertEqual(data['input1'].value, 1003)
        self.assertEqual(data['input2'].value, 2002)

        (data, start, end) = view[1]
        self.assertTrue(data is None)


        # View 'input1', index 4
        view = data_loader.view('input1', 4)
        self.assertTrue(view is None)


        # View 'input2', index -1
        view = data_loader.view('input2', -1)
        self.assertTrue(view is None)


        # View 'input2', index 0
        view = data_loader.view('input2', 0)

        self.assertEqual(view.count(), 2)
        self.assertEqual(view.count('input1'), 2)
        self.assertEqual(view.count('input2'), 1)

        self.assertEqual(view.data_index_start, 0)
        self.assertEqual(view.data_index_end, 1)

        (data, start, end) = view[-1]
        self.assertTrue(data is None)

        (data, start, end) = view[0]
        self.assertTrue(data is not None)
        self.assertEqual(start, 0)
        self.assertEqual(end, 0)
        self.assertEqual(data['input1'].value, 1000)
        self.assertEqual(data['input2'].value, 2000)

        (data, start, end) = view[1]
        self.assertTrue(data is not None)
        self.assertEqual(start, 1)
        self.assertEqual(end, 1)
        self.assertEqual(data['input1'].value, 1001)
        self.assertEqual(data['input2'].value, 2000)

        (data, start, end) = view[2]
        self.assertTrue(data is None)


        # View 'input2', index 1
        view = data_loader.view('input2', 1)

        self.assertEqual(view.count(), 2)
        self.assertEqual(view.count('input1'), 2)
        self.assertEqual(view.count('input2'), 1)

        self.assertEqual(view.data_index_start, 2)
        self.assertEqual(view.data_index_end, 3)

        (data, start, end) = view[-1]
        self.assertTrue(data is None)

        (data, start, end) = view[0]
        self.assertTrue(data is not None)
        self.assertEqual(start, 2)
        self.assertEqual(end, 2)
        self.assertEqual(data['input1'].value, 1002)
        self.assertEqual(data['input2'].value, 2002)

        (data, start, end) = view[1]
        self.assertTrue(data is not None)
        self.assertEqual(start, 3)
        self.assertEqual(end, 3)
        self.assertEqual(data['input1'].value, 1003)
        self.assertEqual(data['input2'].value, 2002)

        (data, start, end) = view[2]
        self.assertTrue(data is None)


        # View 'input2', index 2
        view = data_loader.view('input2', 2)
        self.assertTrue(view is None)


    def test_two_desynchronized_inputs(self):

        # Setup
        self.writeData('input1', [(0, 2), (3, 3)], 1000)
        self.writeData('input2', [(0, 1), (2, 3)], 2000)

        data_loader = DataLoader('channel1')

        cached_file = CachedDataSource()
        cached_file.setup(self.filenames['input1'], prefix)
        data_loader.add('input1', cached_file)

        cached_file = CachedDataSource()
        cached_file.setup(self.filenames['input2'], prefix)
        data_loader.add('input2', cached_file)


        # Global checks
        self.assertEqual(data_loader.count(), 3)
        self.assertEqual(data_loader.count('input1'), 2)
        self.assertEqual(data_loader.count('input2'), 2)

        self.assertEqual(data_loader.data_index_start, 0)
        self.assertEqual(data_loader.data_index_end, 3)


        # Indexing
        (data, start, end) = data_loader[-1]
        self.assertTrue(data is None)

        (data, start, end) = data_loader[0]
        self.assertTrue(data is not None)
        self.assertEqual(start, 0)
        self.assertEqual(end, 1)
        self.assertEqual(data['input1'].value, 1000)
        self.assertEqual(data['input2'].value, 2000)

        (data, start, end) = data_loader[1]
        self.assertTrue(data is not None)
        self.assertEqual(start, 2)
        self.assertEqual(end, 2)
        self.assertEqual(data['input1'].value, 1000)
        self.assertEqual(data['input2'].value, 2002)

        (data, start, end) = data_loader[2]
        self.assertTrue(data is not None)
        self.assertEqual(start, 3)
        self.assertEqual(end, 3)
        self.assertEqual(data['input1'].value, 1003)
        self.assertEqual(data['input2'].value, 2002)

        (data, start, end) = data_loader[3]
        self.assertTrue(data is None)


        # View 'input1', index -1
        view = data_loader.view('input1', -1)
        self.assertTrue(view is None)


        # View 'input1', index 0
        view = data_loader.view('input1', 0)

        self.assertEqual(view.count(), 2)
        self.assertEqual(view.count('input1'), 1)
        self.assertEqual(view.count('input2'), 2)

        self.assertEqual(view.data_index_start, 0)
        self.assertEqual(view.data_index_end, 2)

        (data, start, end) = view[-1]
        self.assertTrue(data is None)

        (data, start, end) = view[0]
        self.assertTrue(data is not None)
        self.assertEqual(start, 0)
        self.assertEqual(end, 1)
        self.assertEqual(data['input1'].value, 1000)
        self.assertEqual(data['input2'].value, 2000)

        (data, start, end) = view[1]
        self.assertTrue(data is not None)
        self.assertEqual(start, 2)
        self.assertEqual(end, 2)
        self.assertEqual(data['input1'].value, 1000)
        self.assertEqual(data['input2'].value, 2002)

        (data, start, end) = view[2]
        self.assertTrue(data is None)


        # View 'input1', index 1
        view = data_loader.view('input1', 1)

        self.assertEqual(view.count(), 1)
        self.assertEqual(view.count('input1'), 1)
        self.assertEqual(view.count('input2'), 1)

        self.assertEqual(view.data_index_start, 3)
        self.assertEqual(view.data_index_end, 3)

        (data, start, end) = view[-1]
        self.assertTrue(data is None)

        (data, start, end) = view[0]
        self.assertTrue(data is not None)
        self.assertEqual(start, 3)
        self.assertEqual(end, 3)
        self.assertEqual(data['input1'].value, 1003)
        self.assertEqual(data['input2'].value, 2002)

        (data, start, end) = view[1]
        self.assertTrue(data is None)


        # View 'input1', index 2
        view = data_loader.view('input1', 2)
        self.assertTrue(view is None)


        # View 'input2', index -1
        view = data_loader.view('input2', -1)
        self.assertTrue(view is None)


        # View 'input2', index 0
        view = data_loader.view('input2', 0)

        self.assertEqual(view.count(), 1)
        self.assertEqual(view.count('input1'), 1)
        self.assertEqual(view.count('input2'), 1)

        self.assertEqual(view.data_index_start, 0)
        self.assertEqual(view.data_index_end, 1)

        (data, start, end) = view[-1]
        self.assertTrue(data is None)

        (data, start, end) = view[0]
        self.assertTrue(data is not None)
        self.assertEqual(start, 0)
        self.assertEqual(end, 1)
        self.assertEqual(data['input1'].value, 1000)
        self.assertEqual(data['input2'].value, 2000)

        (data, start, end) = view[1]
        self.assertTrue(data is None)


        # View 'input2', index 1
        view = data_loader.view('input2', 1)

        self.assertEqual(view.count(), 2)
        self.assertEqual(view.count('input1'), 2)
        self.assertEqual(view.count('input2'), 1)

        self.assertEqual(view.data_index_start, 2)
        self.assertEqual(view.data_index_end, 3)

        (data, start, end) = view[-1]
        self.assertTrue(data is None)

        (data, start, end) = view[0]
        self.assertTrue(data is not None)
        self.assertEqual(start, 2)
        self.assertEqual(end, 2)
        self.assertEqual(data['input1'].value, 1000)
        self.assertEqual(data['input2'].value, 2002)

        (data, start, end) = view[1]
        self.assertTrue(data is not None)
        self.assertEqual(start, 3)
        self.assertEqual(end, 3)
        self.assertEqual(data['input1'].value, 1003)
        self.assertEqual(data['input2'].value, 2002)

        (data, start, end) = view[2]
        self.assertTrue(data is None)


        # View 'input2', index 2
        view = data_loader.view('input2', 2)
        self.assertTrue(view is None)


#----------------------------------------------------------


class DataLoaderListTest(DataLoaderBaseTest):

    def test_creation(self):
        data_loaders = DataLoaderList()

        self.assertTrue(data_loaders.main_loader is None)
        self.assertEqual(len(data_loaders), 0)


    def test_list_unkown_loader_retrieval(self):
        data_loaders = DataLoaderList()
        self.assertTrue(data_loaders['unknown'] is None)


    def test_list_invalid_index_retrieval(self):
        data_loaders = DataLoaderList()
        self.assertTrue(data_loaders[10] is None)


    def test_list_loader_of_unknown_input_retrieval(self):
        data_loaders = DataLoaderList()
        self.assertTrue(data_loaders.loaderOf('unknown') is None)


    def test_list_one_loader_one_input(self):
        self.writeData('input1', [(0, 0), (1, 1), (2, 2)], 1000)

        data_loader = DataLoader('channel1')

        cached_file = CachedDataSource()
        cached_file.setup(self.filenames['input1'], prefix)
        data_loader.add('input1', cached_file)

        data_loaders = DataLoaderList()
        data_loaders.add(data_loader)

        self.assertEqual(data_loaders.main_loader, data_loader)
        self.assertEqual(len(data_loaders), 1)

        self.assertEqual(data_loaders['channel1'], data_loader)
        self.assertEqual(data_loaders[0], data_loader)

        self.assertEqual(data_loaders.loaderOf('input1'), data_loader)


    def test_list_one_loader_two_inputs(self):
        self.writeData('input1', [(0, 0), (1, 1), (2, 2)], 1000)
        self.writeData('input2', [(0, 2)], 2000)

        data_loader = DataLoader('channel1')

        cached_file = CachedDataSource()
        cached_file.setup(self.filenames['input1'], prefix)
        data_loader.add('input1', cached_file)

        cached_file = CachedDataSource()
        cached_file.setup(self.filenames['input2'], prefix)
        data_loader.add('input2', cached_file)

        data_loaders = DataLoaderList()
        data_loaders.add(data_loader)

        self.assertEqual(data_loaders.main_loader, data_loader)
        self.assertEqual(len(data_loaders), 1)

        self.assertEqual(data_loaders['channel1'], data_loader)
        self.assertEqual(data_loaders[0], data_loader)

        self.assertEqual(data_loaders.loaderOf('input1'), data_loader)
        self.assertEqual(data_loaders.loaderOf('input2'), data_loader)


    def test_list_two_loaders_three_inputs(self):
        self.writeData('input1', [(0, 0), (1, 1), (2, 2)], 1000)
        self.writeData('input2', [(0, 2)], 2000)
        self.writeData('input3', [(0, 1), (2, 2)], 3000)

        data_loader1 = DataLoader('channel1')

        cached_file = CachedDataSource()
        cached_file.setup(self.filenames['input1'], prefix)
        data_loader1.add('input1', cached_file)

        cached_file = CachedDataSource()
        cached_file.setup(self.filenames['input2'], prefix)
        data_loader1.add('input2', cached_file)

        data_loader2 = DataLoader('channel2')

        cached_file = CachedDataSource()
        cached_file.setup(self.filenames['input3'], prefix)
        data_loader2.add('input3', cached_file)

        data_loaders = DataLoaderList()
        data_loaders.add(data_loader1)
        data_loaders.add(data_loader2)

        self.assertEqual(data_loaders.main_loader, data_loader1)
        self.assertEqual(len(data_loaders), 2)

        self.assertEqual(data_loaders['channel1'], data_loader1)
        self.assertEqual(data_loaders['channel2'], data_loader2)

        self.assertEqual(data_loaders[0], data_loader1)
        self.assertEqual(data_loaders[1], data_loader2)

        self.assertEqual(data_loaders.loaderOf('input1'), data_loader1)
        self.assertEqual(data_loaders.loaderOf('input2'), data_loader1)
        self.assertEqual(data_loaders.loaderOf('input3'), data_loader2)
