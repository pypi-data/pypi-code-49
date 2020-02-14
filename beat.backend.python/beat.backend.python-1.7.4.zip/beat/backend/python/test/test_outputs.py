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


import six
import numpy
import nose.tools

from .mocks import MockDataSink

from ..outputs import Output, OutputList, SynchronizationListener
from ..dataformat import DataFormat
from beat.backend.python.baseformat import baseformat

from . import prefix


# ----------------------------------------------------------


def test_creation_without_synchronization_listener():

    dataformat = DataFormat(prefix, "user/single_integer/1")
    nose.tools.assert_true(dataformat.valid, dataformat.errors)
    data_sink = MockDataSink(dataformat)

    output = Output("test", data_sink)

    nose.tools.eq_(output.name, "test")
    nose.tools.eq_(output.last_written_data_index, -1)
    nose.tools.eq_(output.nb_data_blocks_written, 0)
    nose.tools.assert_is_none(output._synchronization_listener)


# ----------------------------------------------------------


def test_creation_with_synchronization_listener():

    dataformat = DataFormat(prefix, "user/single_integer/1")
    nose.tools.assert_true(dataformat.valid, dataformat.errors)
    data_sink = MockDataSink(dataformat)

    synchronization_listener = SynchronizationListener()

    output = Output("test", data_sink, synchronization_listener)

    nose.tools.eq_(output.name, "test")
    nose.tools.eq_(output.last_written_data_index, -1)
    nose.tools.eq_(output.nb_data_blocks_written, 0)
    nose.tools.assert_is_not_none(output._synchronization_listener)
    nose.tools.eq_(output._synchronization_listener, synchronization_listener)


# ----------------------------------------------------------


def test_data_creation():

    dataformat = DataFormat(prefix, "user/single_integer/1")
    nose.tools.assert_true(dataformat.valid, dataformat.errors)
    data_sink = MockDataSink(dataformat)

    output = Output("test", data_sink)

    data = output._createData()
    nose.tools.assert_is_not_none(data)
    nose.tools.assert_true(isinstance(data, baseformat))
    nose.tools.eq_(data.value, 0)


# ----------------------------------------------------------


def test_data_writting():

    dataformat = DataFormat(prefix, "user/single_integer/1")
    nose.tools.assert_true(dataformat.valid, dataformat.errors)
    data_sink = MockDataSink(dataformat)

    synchronization_listener = SynchronizationListener()

    output = Output("test", data_sink, synchronization_listener)

    for i in six.moves.range(0, 5):
        synchronization_listener.onIntervalChanged(i, i)

        output.write({"value": numpy.int32(i * i)})
        nose.tools.eq_(output.last_written_data_index, i)
        nose.tools.eq_(output.nb_data_blocks_written, i + 1)
        nose.tools.assert_false(output.isDataMissing())

    nose.tools.eq_(len(data_sink.written), 5)

    for i in six.moves.range(0, 5):
        nose.tools.eq_(data_sink.written[i].data.value, i * i)
        nose.tools.eq_(data_sink.written[i].start, i)
        nose.tools.eq_(data_sink.written[i].end, i)


# ----------------------------------------------------------


@nose.tools.raises(IOError)
def test_data_writting_failure():

    dataformat = DataFormat(prefix, "user/single_integer/1")
    nose.tools.assert_true(dataformat.valid, dataformat.errors)
    data_sink = MockDataSink(dataformat)

    synchronization_listener = SynchronizationListener()

    output = Output("test", data_sink, synchronization_listener)

    synchronization_listener.onIntervalChanged(0, 0)

    output.write({"value": numpy.int32(42)})
    nose.tools.eq_(output.last_written_data_index, 0)
    nose.tools.eq_(output.nb_data_blocks_written, 1)
    nose.tools.assert_false(output.isDataMissing())

    data_sink.can_write = False

    synchronization_listener.onIntervalChanged(1, 1)

    output.write({"value": numpy.int32(42)})  # this should raise


# ----------------------------------------------------------


def test_data_delaying():

    dataformat = DataFormat(prefix, "user/single_integer/1")
    nose.tools.assert_true(dataformat.valid, dataformat.errors)
    data_sink = MockDataSink(dataformat)

    synchronization_listener = SynchronizationListener()

    output = Output("test", data_sink, synchronization_listener)

    for i in six.moves.range(0, 5):
        synchronization_listener.onIntervalChanged(i * 2, i * 2 + 1)
        output.write({"value": numpy.int32(i * i)})
        nose.tools.eq_(output.last_written_data_index, i * 2 + 1)
        nose.tools.eq_(output.nb_data_blocks_written, i + 1)
        nose.tools.assert_false(output.isDataMissing())

    nose.tools.eq_(len(data_sink.written), 5)

    for i in six.moves.range(0, 5):
        nose.tools.eq_(data_sink.written[i].data.value, i * i)
        nose.tools.eq_(data_sink.written[i].start, i * 2)
        nose.tools.eq_(data_sink.written[i].end, i * 2 + 1)


# ----------------------------------------------------------


def test_data_writting_with_explicit_end_index():

    dataformat = DataFormat(prefix, "user/single_integer/1")
    nose.tools.assert_true(dataformat.valid, dataformat.errors)
    data_sink = MockDataSink(dataformat)

    synchronization_listener = SynchronizationListener()

    output = Output("test", data_sink, synchronization_listener)

    for i in six.moves.range(0, 5):
        synchronization_listener.onIntervalChanged(i * 3, i * 3 + 2)

        output.write({"value": numpy.int32(i * i)}, i * 3 + 1)
        nose.tools.eq_(output.last_written_data_index, i * 3 + 1)
        nose.tools.eq_(output.nb_data_blocks_written, i + 1)
        nose.tools.assert_true(output.isDataMissing())

    nose.tools.eq_(len(data_sink.written), 5)

    for i in six.moves.range(0, 5):
        nose.tools.eq_(data_sink.written[i].data.value, i * i)
        nose.tools.eq_(data_sink.written[i].start, max(i * 3 - 1, 0))
        nose.tools.eq_(data_sink.written[i].end, i * 3 + 1)


# ----------------------------------------------------------


@nose.tools.raises(KeyError)
def test_data_writting_failure_with_explicit_end_index_too_low():

    dataformat = DataFormat(prefix, "user/single_integer/1")
    nose.tools.assert_true(dataformat.valid, dataformat.errors)
    data_sink = MockDataSink(dataformat)

    synchronization_listener = SynchronizationListener()

    output = Output("test", data_sink, synchronization_listener)

    synchronization_listener.onIntervalChanged(0, 2)
    output.write({"value": numpy.int32(42)})

    synchronization_listener.onIntervalChanged(3, 5)

    # this must raise
    output.write({"value": numpy.int32(42)}, 1)


# ----------------------------------------------------------


@nose.tools.raises(KeyError)
def test_data_writting_failure_with_explicit_end_index_too_high():

    dataformat = DataFormat(prefix, "user/single_integer/1")
    nose.tools.assert_true(dataformat.valid, dataformat.errors)
    data_sink = MockDataSink(dataformat)

    synchronization_listener = SynchronizationListener()

    output = Output("test", data_sink, synchronization_listener)

    synchronization_listener.onIntervalChanged(0, 2)

    # this must raise
    output.write({"value": numpy.int32(42)}, 4)


# ----------------------------------------------------------


def test_list_creation():
    outputs = OutputList()
    nose.tools.eq_(len(outputs), 0)


# ----------------------------------------------------------


def test_output_list_addition():

    integer_format = DataFormat(prefix, "user/single_integer/1")
    nose.tools.assert_true(integer_format.valid, integer_format.errors)
    integer_data_sink = MockDataSink(integer_format)

    float_format = DataFormat(prefix, "user/single_float/1")
    nose.tools.assert_true(float_format.valid, float_format.errors)
    float_data_sink = MockDataSink(float_format)

    synchronization_listener = SynchronizationListener()
    outputs = OutputList()

    outputs.add(Output("output1", integer_data_sink, synchronization_listener))

    nose.tools.eq_(len(outputs), 1)
    nose.tools.assert_is_not_none(outputs[0])
    nose.tools.eq_(outputs[0].name, "output1")
    nose.tools.eq_(outputs[0]._synchronization_listener, synchronization_listener)
    nose.tools.assert_is_not_none(outputs["output1"])

    outputs.add(Output("output2", float_data_sink, synchronization_listener))

    nose.tools.eq_(len(outputs), 2)
    nose.tools.assert_is_not_none(outputs[1])
    nose.tools.eq_(outputs[1].name, "output2")
    nose.tools.eq_(outputs[1]._synchronization_listener, synchronization_listener)
    nose.tools.assert_is_not_none(outputs["output2"])
