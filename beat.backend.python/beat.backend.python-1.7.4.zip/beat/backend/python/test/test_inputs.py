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

from .mocks import MockDataSource

from ..outputs import SynchronizationListener
from ..inputs import Input
from ..inputs import InputGroup
from ..inputs import InputList
from ..dataformat import DataFormat
from ..data import CachedDataSink

from . import prefix


#----------------------------------------------------------


class InputTest(unittest.TestCase):

    def test_creation(self):
        data_source = MockDataSource([])

        input = Input('test', 'mock', data_source)

        self.assertTrue(input.data is None)
        self.assertTrue(input.group is None)
        self.assertEqual(input.data_format, 'mock')
        self.assertEqual(input.data_index, -1)
        self.assertEqual(input.data_index_end, -1)
        self.assertTrue(input.data_same_as_previous)
        self.assertEqual(input.data_source, data_source)
        self.assertEqual(input.name, 'test')
        self.assertEqual(input.nb_data_blocks_read, 0)


    def test_no_more_data(self):
        data_source = MockDataSource([])

        input = Input('test', 'mock', data_source)

        self.assertFalse(input.hasMoreData())


    def test_has_more_data(self):
        dataformat = DataFormat(prefix, 'user/single_integer/1')

        data_source = MockDataSource([ (dataformat.type(value=10), 0, 0) ])

        input = Input('test', 'mock', data_source)

        self.assertTrue(input.hasMoreData())


    def test_retrieve_one_data_unit(self):
        group = InputGroup('channel1', restricted_access=False)

        dataformat = DataFormat(prefix, 'user/single_integer/1')

        data_source = MockDataSource([ (dataformat.type(value=10), 0, 0),
                                       (dataformat.type(value=20), 1, 1) ])

        input = Input('test', 'mock', data_source)

        group.add(input)

        self.assertTrue(input.hasMoreData())
        self.assertFalse(input.hasDataChanged())
        self.assertTrue(input.isDataUnitDone())

        input.next()

        self.assertTrue(input.data is not None)
        self.assertEqual(input.data.value, 10)
        self.assertEqual(input.data_index, 0)
        self.assertEqual(input.data_index_end, 0)
        self.assertFalse(input.data_same_as_previous)
        self.assertEqual(input.nb_data_blocks_read, 1)

        self.assertTrue(input.hasMoreData())
        self.assertTrue(input.hasDataChanged())
        self.assertTrue(input.isDataUnitDone())


    def test_retrieve_all_data_units(self):
        group = InputGroup('channel1', restricted_access=False)

        dataformat = DataFormat(prefix, 'user/single_integer/1')

        data_source = MockDataSource([ (dataformat.type(value=10), 0, 0) ])
        input = Input('test', 'mock', data_source)

        group.add(input)

        self.assertTrue(input.hasMoreData())
        self.assertFalse(input.hasDataChanged())
        self.assertTrue(input.isDataUnitDone())

        input.next()

        self.assertTrue(input.data is not None)
        self.assertEqual(input.data.value, 10)
        self.assertEqual(input.data_index, 0)
        self.assertEqual(input.data_index_end, 0)
        self.assertFalse(input.data_same_as_previous)
        self.assertEqual(input.nb_data_blocks_read, 1)

        self.assertFalse(input.hasMoreData())
        self.assertTrue(input.hasDataChanged())
        self.assertTrue(input.isDataUnitDone())


    def test_restricted_access(self):
        group = InputGroup('channel1', restricted_access=True)

        dataformat = DataFormat(prefix, 'user/single_integer/1')

        data_source = MockDataSource([ (dataformat.type(value=10), 0, 0) ])
        input = Input('test', 'mock', data_source)

        group.add(input)

        self.assertTrue(input.hasMoreData())
        self.assertFalse(input.hasDataChanged())
        self.assertTrue(input.isDataUnitDone())

        with self.assertRaises(RuntimeError):
            input.next()


#----------------------------------------------------------


class RestrictedInputGroupTest(unittest.TestCase):

    def test_creation(self):
        group = InputGroup('channel1')

        self.assertTrue(group.restricted_access)
        self.assertTrue(group.synchronization_listener is None)
        self.assertEqual(group.channel, 'channel1')
        self.assertEqual(len(group), 0)
        self.assertEqual(group.data_index, -1)
        self.assertEqual(group.data_index_end, -1)
        self.assertEqual(group.first_data_index, -1)
        self.assertEqual(group.last_data_index, -1)


    def test_add_one_input(self):
        data_source = MockDataSource([])

        input = Input('input1', 'mock', data_source)

        group = InputGroup('channel1')

        group.add(input)

        self.assertEqual(input.group, group)
        self.assertEqual(len(group), 1)
        self.assertEqual(group['input1'], input)


    def test_add_two_inputs(self):
        data_source1 = MockDataSource([])
        input1 = Input('input1', 'mock', data_source1)

        data_source2 = MockDataSource([])
        input2 = Input('input2', 'mock', data_source2)

        group = InputGroup('channel1')

        group.add(input1)
        group.add(input2)

        self.assertEqual(input1.group, group)
        self.assertEqual(input2.group, group)
        self.assertEqual(len(group), 2)
        self.assertEqual(group['input1'], input1)
        self.assertEqual(group['input2'], input2)


    def test_no_more_data(self):
        data_source1 = MockDataSource([])
        input1 = Input('input1', 'mock', data_source1)

        data_source2 = MockDataSource([])
        input2 = Input('input2', 'mock', data_source2)

        group = InputGroup('channel1')

        group.add(input1)
        group.add(input2)

        self.assertFalse(group.hasMoreData())


    def test_has_more_data(self):
        dataformat = DataFormat(prefix, 'user/single_integer/1')

        data_source1 = MockDataSource([ (dataformat.type(value=10), 0, 0) ])
        input1 = Input('input1', 'mock', data_source1)

        data_source2 = MockDataSource([ (dataformat.type(value=10), 0, 0) ])
        input2 = Input('input2', 'mock', data_source2)

        group = InputGroup('channel1')

        group.add(input1)
        group.add(input2)

        self.assertTrue(group.hasMoreData())


    def test_restricted_access(self):
        group = InputGroup('channel1')
        with self.assertRaises(RuntimeError):
            group.next()


#----------------------------------------------------------


class InputGroupTest(unittest.TestCase):

    def test_creation(self):
        group = InputGroup('channel1', restricted_access=False)

        self.assertFalse(group.restricted_access)
        self.assertTrue(group.synchronization_listener is None)
        self.assertEqual(group.channel, 'channel1')
        self.assertEqual(len(group), 0)
        self.assertEqual(group.data_index, -1)
        self.assertEqual(group.data_index_end, -1)
        self.assertEqual(group.first_data_index, -1)
        self.assertEqual(group.last_data_index, -1)


    def test_creation_with_listener(self):
        listener = SynchronizationListener()

        group = InputGroup('channel1', synchronization_listener=listener,
                           restricted_access=False)

        self.assertFalse(group.restricted_access)
        self.assertEqual(group.synchronization_listener, listener)
        self.assertEqual(group.channel, 'channel1')
        self.assertEqual(len(group), 0)
        self.assertEqual(group.data_index, -1)
        self.assertEqual(group.data_index_end, -1)
        self.assertEqual(group.first_data_index, -1)
        self.assertEqual(group.last_data_index, -1)

        self.assertEqual(listener.data_index_start, -1)
        self.assertEqual(listener.data_index_end, -1)


    def test_add_one_input(self):
        data_source = MockDataSource([])

        input = Input('input1', 'mock', data_source)

        group = InputGroup('channel1', restricted_access=False)

        group.add(input)

        self.assertEqual(input.group, group)
        self.assertEqual(len(group), 1)
        self.assertEqual(group['input1'], input)


    def test_add_two_inputs(self):
        data_source1 = MockDataSource([])
        input1 = Input('input1', 'mock', data_source1)

        data_source2 = MockDataSource([])
        input2 = Input('input2', 'mock', data_source2)

        group = InputGroup('channel1', restricted_access=False)

        group.add(input1)
        group.add(input2)

        self.assertEqual(input1.group, group)
        self.assertEqual(input2.group, group)
        self.assertEqual(len(group), 2)
        self.assertEqual(group['input1'], input1)
        self.assertEqual(group['input2'], input2)


    def test_no_more_data(self):
        data_source1 = MockDataSource([])
        input1 = Input('input1', 'mock', data_source1)

        data_source2 = MockDataSource([])
        input2 = Input('input2', 'mock', data_source2)

        group = InputGroup('channel1', restricted_access=False)

        group.add(input1)
        group.add(input2)

        self.assertFalse(group.hasMoreData())


    def test_has_more_data(self):
        dataformat = DataFormat(prefix, 'user/single_integer/1')

        data_source1 = MockDataSource([ (dataformat.type(value=10), 0, 0) ])
        input1 = Input('input1', 'mock', data_source1)

        data_source2 = MockDataSource([ (dataformat.type(value=10), 0, 0) ])
        input2 = Input('input2', 'mock', data_source2)

        group = InputGroup('channel1', restricted_access=False)

        group.add(input1)
        group.add(input2)

        self.assertTrue(group.hasMoreData())


    def test_retrieve_one_input_iteration(self):
        indices = [ (0, 0), (1, 1), (2, 3), (4, 4), (5, 5) ]

        expected_hasMoreData = [True, True, True, True, False]
        expected_isDataUnitDone = [True, True, True, True, True]
        expected_hasDataChanged = [True, True, True, True, True]


        dataformat = DataFormat(prefix, 'user/single_integer/1')

        data_source = MockDataSource([ (dataformat.type(value=x), indices[x][0], indices[x][1] )
                                        for x in range(0, len(indices)) ])

        input = Input('input', 'mock', data_source)

        group = InputGroup('channel1', restricted_access=False)

        group.add(input)

        self.assertTrue(group.hasMoreData())

        self.assertTrue(input.hasMoreData())
        self.assertTrue(input.isDataUnitDone())
        self.assertFalse(input.hasDataChanged())

        for i in range(0, len(indices)):
            group.next()

            self.assertEqual(group.data_index, indices[i][0])
            self.assertEqual(group.data_index_end, indices[i][1])

            self.assertEqual(group.first_data_index, indices[i][0])
            self.assertEqual(group.last_data_index, indices[i][1])

            self.assertTrue(input.data is not None)
            self.assertEqual(input.data.value, i)
            self.assertEqual(input.data_index, indices[i][0])
            self.assertEqual(input.data_index_end, indices[i][1])
            self.assertFalse(input.data_same_as_previous)
            self.assertEqual(input.nb_data_blocks_read, i + 1)

            self.assertEqual(group.hasMoreData(), expected_hasMoreData[i])
            self.assertEqual(input.hasMoreData(), expected_hasMoreData[i])
            self.assertEqual(input.isDataUnitDone(), expected_isDataUnitDone[i])
            self.assertEqual(input.hasDataChanged(), expected_hasDataChanged[i])


    def test_retrieve_three_inputs_iteration__same_frequency(self):
        indices = [ (0, 0), (1, 1), (2, 2), (3, 3), (4, 4) ]

        expected_hasMoreData = [True, True, True, True, False]
        expected_isDataUnitDone = [True, True, True, True, True]
        expected_hasDataChanged = [True, True, True, True, True]


        dataformat = DataFormat(prefix, 'user/single_integer/1')

        data_source1 = MockDataSource([ (dataformat.type(value=x), indices[x][0], indices[x][1] )
                                        for x in range(0, len(indices)) ])

        input1 = Input('input1', 'mock', data_source1)

        data_source2 = MockDataSource([ (dataformat.type(value=x + 10), indices[x][0], indices[x][1] )
                                        for x in range(0, len(indices)) ])

        input2 = Input('input2', 'mock', data_source2)

        data_source3 = MockDataSource([ (dataformat.type(value=x + 20), indices[x][0], indices[x][1] )
                                        for x in range(0, len(indices)) ])

        input3 = Input('input3', 'mock', data_source3)

        group = InputGroup('channel1', restricted_access=False)

        group.add(input1)
        group.add(input2)
        group.add(input3)

        self.assertTrue(group.hasMoreData())

        self.assertTrue(input1.hasMoreData())
        self.assertTrue(input1.isDataUnitDone())
        self.assertFalse(input1.hasDataChanged())

        self.assertTrue(input2.hasMoreData())
        self.assertTrue(input2.isDataUnitDone())
        self.assertFalse(input2.hasDataChanged())

        self.assertTrue(input3.hasMoreData())
        self.assertTrue(input3.isDataUnitDone())
        self.assertFalse(input3.hasDataChanged())

        for i in range(0, len(indices)):
            group.next()

            self.assertEqual(group.data_index, indices[i][0])
            self.assertEqual(group.data_index_end, indices[i][1])

            self.assertEqual(group.first_data_index, indices[i][0])
            self.assertEqual(group.last_data_index, indices[i][1])

            self.assertTrue(input1.data is not None)
            self.assertEqual(input1.data.value, i)
            self.assertEqual(input1.data_index, indices[i][0])
            self.assertEqual(input1.data_index_end, indices[i][1])
            self.assertFalse(input1.data_same_as_previous)
            self.assertEqual(input1.nb_data_blocks_read, i + 1)

            self.assertTrue(input2.data is not None)
            self.assertEqual(input2.data.value, i + 10)
            self.assertEqual(input2.data_index, indices[i][0])
            self.assertEqual(input2.data_index_end, indices[i][1])
            self.assertFalse(input2.data_same_as_previous)
            self.assertEqual(input2.nb_data_blocks_read, i + 1)

            self.assertTrue(input3.data is not None)
            self.assertEqual(input3.data.value, i + 20)
            self.assertEqual(input3.data_index, indices[i][0])
            self.assertEqual(input3.data_index_end, indices[i][1])
            self.assertFalse(input3.data_same_as_previous)
            self.assertEqual(input3.nb_data_blocks_read, i + 1)

            self.assertEqual(group.hasMoreData(), expected_hasMoreData[i])
            self.assertEqual(input1.hasMoreData(), expected_hasMoreData[i])
            self.assertEqual(input2.hasMoreData(), expected_hasMoreData[i])
            self.assertEqual(input3.hasMoreData(), expected_hasMoreData[i])

            self.assertEqual(input1.isDataUnitDone(), expected_isDataUnitDone[i])
            self.assertEqual(input2.isDataUnitDone(), expected_isDataUnitDone[i])
            self.assertEqual(input3.isDataUnitDone(), expected_isDataUnitDone[i])

            self.assertEqual(input1.hasDataChanged(), expected_hasDataChanged[i])
            self.assertEqual(input2.hasDataChanged(), expected_hasDataChanged[i])
            self.assertEqual(input3.hasDataChanged(), expected_hasDataChanged[i])


    def test_retrieve_three_inputs_iteration__different_frequencies(self):
        indices1 = [ (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5) ]
        indices2 = [ (0, 1), (2, 3), (4, 5) ]
        indices3 = [ (0, 5) ]

        expected_hasMoreData_1 = [True, True, True, True, True, False]
        expected_hasMoreData_2 = [True, True, True, True, False, False]
        expected_hasMoreData_3 = [False, False, False, False, False, False]

        expected_isDataUnitDone_1 = [True, True, True, True, True, True]
        expected_isDataUnitDone_2 = [False, True, False, True, False, True]
        expected_isDataUnitDone_3 = [False, False, False, False, False, True]

        expected_hasDataChanged_1 = [True, True, True, True, True, True]
        expected_hasDataChanged_2 = [True, False, True, False, True, False]
        expected_hasDataChanged_3 = [True, False, False, False, False, False]


        dataformat = DataFormat(prefix, 'user/single_integer/1')

        data_source1 = MockDataSource([ (dataformat.type(value=x), indices1[x][0], indices1[x][1] )
                                        for x in range(0, len(indices1)) ])

        input1 = Input('input1', 'mock', data_source1)

        data_source2 = MockDataSource([ (dataformat.type(value=x + 10), indices2[x][0], indices2[x][1] )
                                        for x in range(0, len(indices2)) ])

        input2 = Input('input2', 'mock', data_source2)

        data_source3 = MockDataSource([ (dataformat.type(value=x + 20), indices3[x][0], indices3[x][1] )
                                        for x in range(0, len(indices3)) ])

        input3 = Input('input3', 'mock', data_source3)

        group = InputGroup('channel1', restricted_access=False)

        group.add(input1)
        group.add(input2)
        group.add(input3)

        self.assertTrue(group.hasMoreData())

        self.assertTrue(input1.hasMoreData())
        self.assertTrue(input1.isDataUnitDone())
        self.assertFalse(input1.hasDataChanged())

        self.assertTrue(input2.hasMoreData())
        self.assertTrue(input2.isDataUnitDone())
        self.assertFalse(input2.hasDataChanged())

        self.assertTrue(input3.hasMoreData())
        self.assertTrue(input3.isDataUnitDone())
        self.assertFalse(input3.hasDataChanged())

        for i in range(0, len(indices1)):
            group.next()

            self.assertEqual(group.data_index, indices3[0][0])
            self.assertEqual(group.data_index_end, indices3[0][1])

            self.assertEqual(group.first_data_index, indices1[i][0])
            self.assertEqual(group.last_data_index, indices1[i][1])

            self.assertTrue(input1.data is not None)
            self.assertEqual(input1.data.value, i)
            self.assertEqual(input1.data_index, indices1[i][0])
            self.assertEqual(input1.data_index_end, indices1[i][1])
            self.assertFalse(input1.data_same_as_previous)
            self.assertEqual(input1.nb_data_blocks_read, i + 1)

            self.assertTrue(input2.data is not None)
            self.assertEqual(input2.data.value, (i // 2) + 10)
            self.assertEqual(input2.data_index, indices2[i // 2][0])
            self.assertEqual(input2.data_index_end, indices2[i // 2][1])
            self.assertEqual(input2.nb_data_blocks_read, (i // 2) + 1)

            self.assertTrue(input3.data is not None)
            self.assertEqual(input3.data.value, 20)
            self.assertEqual(input3.data_index, indices3[0][0])
            self.assertEqual(input3.data_index_end, indices3[0][1])
            self.assertEqual(input3.nb_data_blocks_read, 1)

            self.assertEqual(group.hasMoreData(), expected_hasMoreData_1[i])
            self.assertEqual(input1.hasMoreData(), expected_hasMoreData_1[i])
            self.assertEqual(input2.hasMoreData(), expected_hasMoreData_2[i])
            self.assertEqual(input3.hasMoreData(), expected_hasMoreData_3[i])

            self.assertEqual(input1.isDataUnitDone(), expected_isDataUnitDone_1[i])
            self.assertEqual(input2.isDataUnitDone(), expected_isDataUnitDone_2[i])
            self.assertEqual(input3.isDataUnitDone(), expected_isDataUnitDone_3[i])

            self.assertEqual(input1.hasDataChanged(), expected_hasDataChanged_1[i])
            self.assertEqual(input2.hasDataChanged(), expected_hasDataChanged_2[i])
            self.assertEqual(input3.hasDataChanged(), expected_hasDataChanged_3[i])


    def test_retrieve_two_inputs_iteration__desynchronized_frequencies(self):
        indices1 = [ (0, 2), (3, 5), (6, 8), (9, 11), (12, 14), (15, 17) ]
        indices2 = [ (0, 4), (5, 10), (11, 17) ]

        expected_values_1 = [0, 1, 1, 2, 3, 3, 4, 5]
        expected_values_2 = [0, 0, 1, 1, 1, 2, 2, 2]

        expected_group_indices1 = [(0, 4), (0, 5), (3, 10), (5, 10), (5, 11), (9, 17),  (11, 17), (11, 17)]
        expected_group_indices2 = [(0, 2), (3, 4), (5, 5),  (6, 8),  (9, 10), (11, 11), (12, 14), (15, 17)]
        expected_indices_1 = [(0, 2), (3, 5), (3, 5),  (6, 8),  (9, 11), (9, 11),  (12, 14), (15, 17)]
        expected_indices_2 = [(0, 4), (0, 4), (5, 10), (5, 10), (5, 10), (11, 17), (11, 17), (11, 17)]

        expected_hasMoreData_1 = [True, True, True, True, True,  True,  True,  False]
        expected_hasMoreData_2 = [True, True, True, True, True, False, False, False]

        expected_isDataUnitDone_1 = [True,  False, True,  True,  False, True,  True,  True]
        expected_isDataUnitDone_2 = [False, True,  False, False, True,  False, False, True]

        expected_hasDataChanged_1 = [True, True,  False, True,  True,  False, True,  True]
        expected_hasDataChanged_2 = [True, False, True,  False, False, True,  False, False]


        dataformat = DataFormat(prefix, 'user/single_integer/1')

        data_source1 = MockDataSource([ (dataformat.type(value=x), indices1[x][0], indices1[x][1] )
                                        for x in range(0, len(indices1)) ])

        input1 = Input('input1', 'mock', data_source1)

        data_source2 = MockDataSource([ (dataformat.type(value=x), indices2[x][0], indices2[x][1] )
                                        for x in range(0, len(indices2)) ])

        input2 = Input('input2', 'mock', data_source2)

        group = InputGroup('channel1', restricted_access=False)

        group.add(input1)
        group.add(input2)

        self.assertTrue(group.hasMoreData())

        self.assertTrue(input1.hasMoreData())
        self.assertTrue(input1.isDataUnitDone())
        self.assertFalse(input1.hasDataChanged())

        self.assertTrue(input2.hasMoreData())
        self.assertTrue(input2.isDataUnitDone())
        self.assertFalse(input2.hasDataChanged())

        for i in range(0, len(expected_indices_1)):
            group.next()

            self.assertEqual(group.data_index, expected_group_indices1[i][0])
            self.assertEqual(group.data_index_end, expected_group_indices1[i][1])

            self.assertEqual(group.first_data_index, expected_group_indices2[i][0])
            self.assertEqual(group.last_data_index, expected_group_indices2[i][1])

            self.assertTrue(input1.data is not None)
            self.assertEqual(input1.data.value, expected_values_1[i])
            self.assertEqual(input1.data_index, expected_indices_1[i][0])
            self.assertEqual(input1.data_index_end, expected_indices_1[i][1])

            self.assertTrue(input2.data is not None)
            self.assertEqual(input2.data.value, expected_values_2[i])
            self.assertEqual(input2.data_index, expected_indices_2[i][0])
            self.assertEqual(input2.data_index_end, expected_indices_2[i][1])

            self.assertEqual(group.hasMoreData(), expected_hasMoreData_1[i])
            self.assertEqual(input1.hasMoreData(), expected_hasMoreData_1[i])
            self.assertEqual(input2.hasMoreData(), expected_hasMoreData_2[i])

            self.assertEqual(input1.isDataUnitDone(), expected_isDataUnitDone_1[i])
            self.assertEqual(input2.isDataUnitDone(), expected_isDataUnitDone_2[i])

            self.assertEqual(input1.hasDataChanged(), expected_hasDataChanged_1[i])
            self.assertEqual(input2.hasDataChanged(), expected_hasDataChanged_2[i])


    def test_retrieve_two_inputs_iteration__different_frequencies(self):
        indices1 = [ (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7) ]
        indices2 = [ (0, 3), (4, 7) ]

        expected_values_1 = [0, 1, 2, 3, 4, 5, 6, 7]
        expected_values_2 = [0, 0, 0, 0, 1, 1, 1, 1]

        expected_hasMoreData_1 = [True, True, True, True, True,  True,  True,  False]
        expected_hasMoreData_2 = [True, True, True, True, False, False, False, False]

        expected_isDataUnitDone_1 = [True,  True,  True,  True, True,  True,  True,  True]
        expected_isDataUnitDone_2 = [False, False, False, True, False, False, False, True]

        expected_hasDataChanged_1 = [True, True,  True,   True,  True, True,   True,  True]
        expected_hasDataChanged_2 = [True, False, False,  False, True, False,  False, False]


        dataformat = DataFormat(prefix, 'user/single_integer/1')

        data_source1 = MockDataSource([ (dataformat.type(value=x), indices1[x][0], indices1[x][1] )
                                        for x in range(0, len(indices1)) ])

        input1 = Input('input1', 'mock', data_source1)

        data_source2 = MockDataSource([ (dataformat.type(value=x), indices2[x][0], indices2[x][1] )
                                        for x in range(0, len(indices2)) ])

        input2 = Input('input2', 'mock', data_source2)

        group = InputGroup('channel1', restricted_access=False)

        group.add(input1)
        group.add(input2)

        self.assertTrue(group.hasMoreData())

        self.assertTrue(input1.hasMoreData())
        self.assertTrue(input1.isDataUnitDone())
        self.assertFalse(input1.hasDataChanged())

        self.assertTrue(input2.hasMoreData())
        self.assertTrue(input2.isDataUnitDone())
        self.assertFalse(input2.hasDataChanged())

        for i in range(0, len(indices1)):
            group.next()

            self.assertEqual(group.data_index, indices2[i // 4][0])
            self.assertEqual(group.data_index_end, indices2[i // 4][1])

            self.assertEqual(group.first_data_index, indices1[i][0])
            self.assertEqual(group.last_data_index, indices1[i][1])

            self.assertTrue(input1.data is not None)
            self.assertEqual(input1.data.value, expected_values_1[i])
            self.assertEqual(input1.data_index, indices1[i][0])
            self.assertEqual(input1.data_index_end, indices1[i][1])

            self.assertTrue(input2.data is not None)
            self.assertEqual(input2.data.value, expected_values_2[i])
            self.assertEqual(input2.data_index, indices2[i // 4][0])
            self.assertEqual(input2.data_index_end, indices2[i // 4][1])

            self.assertEqual(group.hasMoreData(), expected_hasMoreData_1[i])
            self.assertEqual(input1.hasMoreData(), expected_hasMoreData_1[i])
            self.assertEqual(input2.hasMoreData(), expected_hasMoreData_2[i])

            self.assertEqual(input1.isDataUnitDone(), expected_isDataUnitDone_1[i])
            self.assertEqual(input2.isDataUnitDone(), expected_isDataUnitDone_2[i])

            self.assertEqual(input1.hasDataChanged(), expected_hasDataChanged_1[i])
            self.assertEqual(input2.hasDataChanged(), expected_hasDataChanged_2[i])


#----------------------------------------------------------


class InputListTest(unittest.TestCase):

    def test_creation(self):
        inputs = InputList()

        self.assertTrue(inputs.main_group is None)
        self.assertEqual(inputs.nbGroups(), 0)
        self.assertEqual(len(inputs), 0)
        self.assertFalse(inputs.hasMoreData())


    def test_list_unkown_input_retrieval(self):
        inputs = InputList()

        self.assertTrue(inputs['unknown'] is None)


    def test_list_group_of_unknown_input_retrieval(self):
        inputs = InputList()

        self.assertTrue(inputs.groupOf('unknown') is None)


    def test_list_one_group_one_input(self):
        inputs = InputList()

        data_source = MockDataSource([])
        input = Input('input1', 'mock', data_source)

        group = InputGroup('channel1')
        group.add(input)

        inputs.add(group)

        self.assertEqual(inputs.main_group, group)
        self.assertEqual(inputs.nbGroups(), 1)
        self.assertEqual(len(inputs), 1)

        self.assertEqual(inputs['input1'], input)
        self.assertEqual(inputs[0], input)

        self.assertEqual(inputs.groupOf('input1'), group)


    def test_list_one_group_two_inputs(self):
        inputs = InputList()

        data_source1 = MockDataSource([])
        input1 = Input('input1', 'mock', data_source1)

        data_source2 = MockDataSource([])
        input2 = Input('input2', 'mock', data_source2)

        group = InputGroup('channel1')

        group.add(input1)
        group.add(input2)

        inputs.add(group)

        self.assertEqual(inputs.main_group, group)
        self.assertEqual(inputs.nbGroups(), 1)
        self.assertEqual(len(inputs), 2)

        self.assertEqual(inputs['input1'], input1)
        self.assertEqual(inputs[0], input1)

        self.assertEqual(inputs['input2'], input2)
        self.assertEqual(inputs[1], input2)

        self.assertEqual(inputs.groupOf('input1'), group)
        self.assertEqual(inputs.groupOf('input2'), group)


    def test_list_two_groups_three_inputs(self):
        inputs = InputList()

        group1 = InputGroup('channel1')

        data_source1 = MockDataSource([])
        input1 = Input('input1', 'mock', data_source1)
        group1.add(input1)

        data_source2 = MockDataSource([])
        input2 = Input('input2', 'mock', data_source2)
        group1.add(input2)

        inputs.add(group1)

        group2 = InputGroup('channel2', restricted_access=False)

        data_source3 = MockDataSource([])
        input3 = Input('input3', 'mock', data_source3)
        group2.add(input3)

        inputs.add(group2)

        self.assertEqual(inputs.main_group, group1)
        self.assertEqual(inputs.nbGroups(), 2)
        self.assertEqual(len(inputs), 3)

        self.assertEqual(inputs['input1'], input1)
        self.assertEqual(inputs[0], input1)

        self.assertEqual(inputs['input2'], input2)
        self.assertEqual(inputs[1], input2)

        self.assertEqual(inputs['input3'], input3)
        self.assertEqual(inputs[2], input3)

        self.assertEqual(inputs.groupOf('input1'), group1)
        self.assertEqual(inputs.groupOf('input2'), group1)
        self.assertEqual(inputs.groupOf('input3'), group2)

        counter = 0
        for input in inputs:
            self.assertEqual(inputs[counter], input)
            counter += 1

        self.assertEqual(counter, 3)
