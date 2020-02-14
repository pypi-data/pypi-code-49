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
import shutil

from ..data import mixDataIndices
from ..data import CachedDataSource
from ..data import CachedDataSink
from ..data import getAllFilenames
from ..data import foundSplitRanges
from ..hash import hashFileContents
from ..dataformat import DataFormat
from ..database import Database

from . import prefix


#----------------------------------------------------------


class TestMixDataIndices(unittest.TestCase):

    def test_one_list(self):
        list_of_data_indices = [
            [(0, 2), (3, 4), (5, 6)]
        ]

        result = mixDataIndices(list_of_data_indices)

        self.assertEqual([(0, 2), (3, 4), (5, 6)], result)


    def test_two_identical_lists(self):
        list_of_data_indices = [
            [(0, 2), (3, 4), (5, 6)],
            [(0, 2), (3, 4), (5, 6)],
        ]

        result = mixDataIndices(list_of_data_indices)

        self.assertEqual([(0, 2), (3, 4), (5, 6)], result)


    def test_two_synchronized_lists(self):
        list_of_data_indices = [
            [(0, 2), (3, 4), (5, 6)],
            [(0, 4), (5, 6)],
        ]

        result = mixDataIndices(list_of_data_indices)

        self.assertEqual([(0, 2), (3, 4), (5, 6)], result)


    def test_two_desynchronized_lists(self):
        list_of_data_indices = [
            [(0, 2), (3, 4), (5, 6)],
            [(0, 1), (2, 4), (5, 6)],
        ]

        result = mixDataIndices(list_of_data_indices)

        self.assertEqual([(0, 1), (2, 2), (3, 4), (5, 6)], result)


#----------------------------------------------------------


class TestCachedDataBase(unittest.TestCase):

    def setUp(self):
        testfile = tempfile.NamedTemporaryFile(prefix=__name__, suffix='.data')
        testfile.close() # preserve only the name
        self.filename = testfile.name


    def tearDown(self):
        basename, ext = os.path.splitext(self.filename)
        filenames = [self.filename]
        filenames += glob.glob(basename + '*')
        for filename in filenames:
            if os.path.exists(filename):
                os.unlink(filename)


    def writeData(self, dataformat_name, start_index=0, end_index=10):
        dataformat = DataFormat(prefix, dataformat_name)
        self.assertTrue(dataformat.valid)

        data_sink = CachedDataSink()
        self.assertTrue(data_sink.setup(self.filename, dataformat, start_index, end_index))

        all_data = []
        for i in range(start_index, end_index + 1):
            data = dataformat.type()
            data_sink.write(data, i, i)
            all_data.append(data)

        (nb_bytes, duration) = data_sink.statistics()
        self.assertTrue(nb_bytes > 0)
        self.assertTrue(duration > 0)

        data_sink.close()
        del data_sink

        return all_data


#----------------------------------------------------------


class TestGetAllFilenames(TestCachedDataBase):

    def test_one_complete_data_file(self):
        self.writeData('user/single_integer/1', 0, 9)

        (data_filenames, indices_filenames, data_checksum_filenames, indices_checksum_filenames) = \
            getAllFilenames(self.filename)

        self.assertEqual(1, len(data_filenames))
        self.assertEqual(1, len(indices_filenames))
        self.assertEqual(1, len(data_checksum_filenames))
        self.assertEqual(1, len(indices_checksum_filenames))


    def test_three_complete_data_files(self):
        self.writeData('user/single_integer/1', 0, 9)
        self.writeData('user/single_integer/1', 10, 19)
        self.writeData('user/single_integer/1', 20, 29)

        (data_filenames, indices_filenames, data_checksum_filenames, indices_checksum_filenames) = \
            getAllFilenames(self.filename)

        self.assertEqual(3, len(data_filenames))
        self.assertEqual(3, len(indices_filenames))
        self.assertEqual(3, len(data_checksum_filenames))
        self.assertEqual(3, len(indices_checksum_filenames))


    def test_one_partial_data_file(self):
        self.writeData('user/single_integer/1', 0, 9)

        (data_filenames, indices_filenames, data_checksum_filenames, indices_checksum_filenames) = \
            getAllFilenames(self.filename, 2, 6)

        self.assertEqual(1, len(data_filenames))
        self.assertEqual(1, len(indices_filenames))
        self.assertEqual(1, len(data_checksum_filenames))
        self.assertEqual(1, len(indices_checksum_filenames))


    def test_three_partial_data_files_1(self):
        self.writeData('user/single_integer/1', 0, 9)
        self.writeData('user/single_integer/1', 10, 19)
        self.writeData('user/single_integer/1', 20, 29)

        (data_filenames, indices_filenames, data_checksum_filenames, indices_checksum_filenames) = \
            getAllFilenames(self.filename, 14, 18)

        self.assertEqual(1, len(data_filenames))
        self.assertEqual(1, len(indices_filenames))
        self.assertEqual(1, len(data_checksum_filenames))
        self.assertEqual(1, len(indices_checksum_filenames))


    def test_three_partial_data_files_2(self):
        self.writeData('user/single_integer/1', 0, 9)
        self.writeData('user/single_integer/1', 10, 19)
        self.writeData('user/single_integer/1', 20, 29)

        (data_filenames, indices_filenames, data_checksum_filenames, indices_checksum_filenames) = \
            getAllFilenames(self.filename, 4, 18)

        self.assertEqual(2, len(data_filenames))
        self.assertEqual(2, len(indices_filenames))
        self.assertEqual(2, len(data_checksum_filenames))
        self.assertEqual(2, len(indices_checksum_filenames))


    def test_three_partial_data_files_3(self):
        self.writeData('user/single_integer/1', 0, 9)
        self.writeData('user/single_integer/1', 10, 19)
        self.writeData('user/single_integer/1', 20, 29)

        (data_filenames, indices_filenames, data_checksum_filenames, indices_checksum_filenames) = \
            getAllFilenames(self.filename, 4, 28)

        self.assertEqual(3, len(data_filenames))
        self.assertEqual(3, len(indices_filenames))
        self.assertEqual(3, len(data_checksum_filenames))
        self.assertEqual(3, len(indices_checksum_filenames))


#----------------------------------------------------------


class TestCachedDataSource(TestCachedDataBase):

    def check_valid_indices(self, cached_file):
        for i in range(0, len(cached_file)):
            (data, start_index, end_index) = cached_file[i]
            self.assertTrue(data is not None)
            self.assertEqual(i + cached_file.first_data_index(), start_index)
            self.assertEqual(i + cached_file.first_data_index(), end_index)


    def check_valid_data_indices(self, cached_file):
        for i in range(0, len(cached_file)):
            (data, start_index, end_index) = cached_file.getAtDataIndex(i + cached_file.first_data_index())
            self.assertTrue(data is not None)
            self.assertEqual(i + cached_file.first_data_index(), start_index)
            self.assertEqual(i + cached_file.first_data_index(), end_index)


    def check_invalid_indices(self, cached_file):
        # Invalid indices
        (data, start_index, end_index) = cached_file[-1]
        self.assertTrue(data is None)

        (data, start_index, end_index) = cached_file[len(cached_file)]
        self.assertTrue(data is None)

        # Invalid data indices
        (data, start_index, end_index) = cached_file.getAtDataIndex(cached_file.first_data_index() - 1)
        self.assertTrue(data is None)

        (data, start_index, end_index) = cached_file.getAtDataIndex(cached_file.last_data_index() + 1)
        self.assertTrue(data is None)


    def test_one_complete_data_file(self):
        self.writeData('user/single_integer/1', 0, 9)

        cached_file = CachedDataSource()
        cached_file.setup(self.filename, prefix)

        self.assertEqual(10, len(cached_file))

        self.check_valid_indices(cached_file)
        self.check_valid_data_indices(cached_file)
        self.check_invalid_indices(cached_file)


    def test_three_complete_data_files(self):
        self.writeData('user/single_integer/1', 0, 9)
        self.writeData('user/single_integer/1', 10, 19)
        self.writeData('user/single_integer/1', 20, 29)

        cached_file = CachedDataSource()
        cached_file.setup(self.filename, prefix)

        self.assertEqual(30, len(cached_file))

        self.check_valid_indices(cached_file)
        self.check_valid_data_indices(cached_file)
        self.check_invalid_indices(cached_file)


    def test_one_partial_data_file(self):
        self.writeData('user/single_integer/1', 0, 9)

        cached_file = CachedDataSource()
        cached_file.setup(self.filename, prefix, 2, 6)

        self.assertEqual(5, len(cached_file))

        self.check_valid_indices(cached_file)
        self.check_valid_data_indices(cached_file)
        self.check_invalid_indices(cached_file)


    def test_three_partial_data_files_1(self):
        self.writeData('user/single_integer/1', 0, 9)
        self.writeData('user/single_integer/1', 10, 19)
        self.writeData('user/single_integer/1', 20, 29)

        cached_file = CachedDataSource()
        cached_file.setup(self.filename, prefix, 14, 18)

        self.assertEqual(5, len(cached_file))

        self.check_valid_indices(cached_file)
        self.check_valid_data_indices(cached_file)
        self.check_invalid_indices(cached_file)


    def test_three_partial_data_files_2(self):
        self.writeData('user/single_integer/1', 0, 9)
        self.writeData('user/single_integer/1', 10, 19)
        self.writeData('user/single_integer/1', 20, 29)

        cached_file = CachedDataSource()
        cached_file.setup(self.filename, prefix, 4, 18)

        self.assertEqual(15, len(cached_file))

        self.check_valid_indices(cached_file)
        self.check_valid_data_indices(cached_file)
        self.check_invalid_indices(cached_file)


    def test_three_partial_data_files_3(self):
        self.writeData('user/single_integer/1', 0, 9)
        self.writeData('user/single_integer/1', 10, 19)
        self.writeData('user/single_integer/1', 20, 29)

        cached_file = CachedDataSource()
        cached_file.setup(self.filename, prefix, 4, 28)

        self.assertEqual(25, len(cached_file))

        self.check_valid_indices(cached_file)
        self.check_valid_data_indices(cached_file)
        self.check_invalid_indices(cached_file)


#----------------------------------------------------------


class TestDatabaseOutputDataSource(unittest.TestCase):

    def setUp(self):
        self.cache_root = tempfile.mkdtemp(prefix=__name__)


    def tearDown(self):
        shutil.rmtree(self.cache_root)


    def check_valid_indices(self, data_source):
        for i in range(0, len(data_source)):
            (data, start_index, end_index) = data_source[i]
            self.assertTrue(data is not None)
            self.assertEqual(i + data_source.first_data_index(), start_index)
            self.assertEqual(i + data_source.first_data_index(), end_index)


    def check_valid_data_indices(self, data_source):
        for i in range(0, len(data_source)):
            (data, start_index, end_index) = data_source.getAtDataIndex(i + data_source.first_data_index())
            self.assertTrue(data is not None)
            self.assertEqual(i + data_source.first_data_index(), start_index)
            self.assertEqual(i + data_source.first_data_index(), end_index)


    def check_invalid_indices(self, data_source):
        # Invalid indices
        (data, start_index, end_index) = data_source[-1]
        self.assertTrue(data is None)

        (data, start_index, end_index) = data_source[len(data_source)]
        self.assertTrue(data is None)

        # Invalid data indices
        (data, start_index, end_index) = data_source.getAtDataIndex(data_source.first_data_index() - 1)
        self.assertTrue(data is None)

        (data, start_index, end_index) = data_source.getAtDataIndex(data_source.last_data_index() + 1)
        self.assertTrue(data is None)


    def test(self):
        db = Database(prefix, 'integers_db/1')
        self.assertTrue(db.valid)

        view = db.view('double', 'double')
        view.index(os.path.join(self.cache_root, 'data.db'))
        view.setup(os.path.join(self.cache_root, 'data.db'), pack=False)

        self.assertTrue(view.data_sources is not None)
        self.assertEqual(len(view.data_sources), 3)

        for output_name, data_source in view.data_sources.items():
            self.assertEqual(9, len(data_source))

            self.check_valid_indices(data_source)
            self.check_valid_data_indices(data_source)
            self.check_invalid_indices(data_source)


#----------------------------------------------------------


class TestDataSink(TestCachedDataBase):

    def test_creation(self):
        dataformat = DataFormat(prefix, 'user/single_integer/1')
        self.assertTrue(dataformat.valid)

        data_sink = CachedDataSink()
        self.assertTrue(data_sink.setup(self.filename, dataformat, 0, 10))


#----------------------------------------------------------


class TestFoundSplitRanges(unittest.TestCase):

    def test_2_splits(self):
        l = [[0,2,4,6,8,10,12], [0,3,6,9,12]]
        n_split = 2
        ref = [(0, 5), (6, 11)]
        res = foundSplitRanges(l, n_split)
        self.assertEqual(res, ref)


    def test_5_splits(self):
        l = [[0,2,4,6,8,10,12,15], [0,3,6,9,12,15]]
        n_split = 5
        ref = [(0, 5), (6, 11), (12, 14)]
        res = foundSplitRanges(l, n_split)
        self.assertEqual(res, ref)
