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


import numpy
import nose.tools

from ..dataformat import DataFormat

from . import prefix


# ----------------------------------------------------------


def doit(format, key, value):

    df = DataFormat(prefix, format)
    nose.tools.assert_true(df.valid, df.errors)
    obj = df.type()
    setattr(obj, key, value)
    return obj


# ----------------------------------------------------------


def test_single_integer():
    value = 42
    np_types = [numpy.uint16, numpy.uint8, numpy.int32, numpy.int16, numpy.int8]
    dataformat = "user/single_integer/1"
    return_type = numpy.int32

    for np_type in np_types:
        obj = doit(dataformat, "value", np_type(value))
        nose.tools.assert_true(numpy.equal(obj.value, value))
        nose.tools.assert_true(isinstance(obj.value, return_type))


# ----------------------------------------------------------


def test_single_integer64():
    value = 42
    np_types = [
        numpy.uint32,
        numpy.uint16,
        numpy.uint8,
        numpy.int64,
        numpy.int32,
        numpy.int16,
        numpy.int8,
    ]
    dataformat = "user/single_integer64/1"
    return_type = numpy.int64

    for np_type in np_types:
        obj = doit(dataformat, "value", np_type(value))
        nose.tools.assert_true(numpy.equal(obj.value, value))
        nose.tools.assert_true(isinstance(obj.value, return_type))


# ----------------------------------------------------------


def test_single_unsigned_integer():
    value = 42
    np_types = [numpy.uint32, numpy.uint16, numpy.uint8]
    dataformat = "user/single_unsigned_integer/1"
    return_type = numpy.uint32

    for np_type in np_types:
        obj = doit(dataformat, "value", np_type(value))
        nose.tools.assert_true(numpy.equal(obj.value, value))
        nose.tools.assert_true(isinstance(obj.value, return_type))


# ----------------------------------------------------------


def test_single_unsigned_integer64():
    value = 42
    np_types = [numpy.uint64, numpy.uint32, numpy.uint16, numpy.uint8]
    dataformat = "user/single_unsigned_integer64/1"
    return_type = numpy.uint64

    for np_type in np_types:
        obj = doit(dataformat, "value", np_type(value))
        nose.tools.assert_true(numpy.equal(obj.value, value))
        nose.tools.assert_true(isinstance(obj.value, return_type))


# ----------------------------------------------------------


def test_zero():
    value = 0
    np_types = [
        numpy.uint64,
        numpy.uint32,
        numpy.uint16,
        numpy.uint8,
        numpy.int64,
        numpy.int32,
        numpy.int16,
        numpy.int8,
    ]
    dataformats = [
        ("user/single_integer/1", numpy.int32),
        ("user/single_unsigned_integer/1", numpy.uint32),
        ("user/single_integer64/1", numpy.int64),
        ("user/single_unsigned_integer64/1", numpy.uint64),
    ]

    for dataformat, return_type in dataformats:
        for np_type in np_types:
            obj = doit(dataformat, "value", np_type(value))
            nose.tools.assert_true(numpy.equal(obj.value, value))
            nose.tools.assert_true(isinstance(obj.value, return_type))


# ----------------------------------------------------------


def test_single_float():
    obj = doit("user/single_float/1", "value", numpy.float32(42))
    nose.tools.assert_true(numpy.isclose(obj.value, 42))
    nose.tools.assert_true(isinstance(obj.value, numpy.float32))


# ----------------------------------------------------------


def test_single_boolean():
    obj = doit("user/single_boolean/1", "value", True)
    nose.tools.assert_true(obj.value)
    nose.tools.assert_true(isinstance(obj.value, numpy.bool_))


# ----------------------------------------------------------


def test_single_string():
    obj = doit("user/single_string/1", "value", "test")
    nose.tools.eq_(obj.value, "test")


# ----------------------------------------------------------


def test_single_object():
    obj = doit("user/single_object/1", "obj", dict(value1=numpy.int16(42), value2=True))
    nose.tools.assert_true(numpy.equal(obj.obj.value1, 42))
    nose.tools.assert_true(isinstance(obj.obj.value1, numpy.int32))
    nose.tools.assert_true(obj.obj.value2)
    nose.tools.assert_true(isinstance(obj.obj.value2, numpy.bool_))


# ----------------------------------------------------------


def test_hierarchy_of_objects():
    obj = doit(
        "user/hierarchy_of_objects/1",
        "obj1",
        dict(obj2=dict(obj3=dict(value=numpy.int16(42)))),
    )
    nose.tools.assert_true(isinstance(obj.obj1.obj2.obj3.value, numpy.int32))
    nose.tools.assert_true(numpy.equal(obj.obj1.obj2.obj3.value, 42))


# ----------------------------------------------------------


def test_empty_1d_array_of_integers():
    obj = doit("user/empty_1d_array_of_integers/1", "value", [numpy.int16(42)])
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.shape, (1,))
    nose.tools.eq_(obj.value.dtype, numpy.int32)
    nose.tools.assert_true(numpy.equal(obj.value[0], 42))


# ----------------------------------------------------------


def test_empty_2d_array_of_integers():
    obj = doit("user/empty_2d_array_of_integers/1", "value", [[numpy.int16(42)]])
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.shape, (1, 1))
    nose.tools.eq_(obj.value.dtype, numpy.int32)
    nose.tools.assert_true(numpy.equal(obj.value[0][0], 42))


# ----------------------------------------------------------


def test_empty_3d_array_of_integers():
    obj = doit("user/empty_3d_array_of_integers/1", "value", [[[numpy.int16(42)]]])
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.shape, (1, 1, 1))
    nose.tools.eq_(obj.value.dtype, numpy.int32)
    nose.tools.assert_true(numpy.equal(obj.value[0][0][0], 42))


# ----------------------------------------------------------


def test_1d_array_of_integers():
    v = 10 * [numpy.int16(42)]
    obj = doit("user/1d_array_of_integers/1", "value", v)
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.shape, (10,))
    nose.tools.eq_(obj.value.dtype, numpy.int32)
    nose.tools.assert_true(numpy.all(obj.value == 42))


# ----------------------------------------------------------


def test_2d_array_of_integers():
    v = numpy.array(50 * [numpy.int16(42)]).reshape(10, 5)
    obj = doit("user/2d_array_of_integers/1", "value", v)
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.shape, (10, 5))
    nose.tools.eq_(obj.value.dtype, numpy.int32)
    nose.tools.assert_true(numpy.all(obj.value == 42))


# ----------------------------------------------------------


def test_3d_array_of_integers():
    v = numpy.array(100 * [numpy.int16(42)]).reshape(10, 5, 2)
    obj = doit("user/3d_array_of_integers/1", "value", v)
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.shape, (10, 5, 2))
    nose.tools.eq_(obj.value.dtype, numpy.int32)
    nose.tools.assert_true(numpy.all(obj.value == 42))


# ----------------------------------------------------------


def test_empty_1d_array_of_objects():
    obj = doit(
        "user/empty_1d_array_of_objects/1", "value", [{"value": numpy.int16(42)}]
    )
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.shape, (1,))
    nose.tools.eq_(obj.value.dtype, numpy.object)
    nose.tools.assert_true(numpy.equal(obj.value[0].value, 42))


# ----------------------------------------------------------


def test_empty_1d_array_of_objects4():
    obj = doit(
        "user/empty_1d_array_of_objects4/1",
        "value",
        [{"id": numpy.int16(42), "name": "test", "value": 42.0}],
    )
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.shape, (1,))
    nose.tools.eq_(obj.value.dtype, numpy.object)
    nose.tools.assert_true(numpy.isclose(obj.value[0].value, 42))


# ----------------------------------------------------------


def test_empty_2d_array_of_objects():
    obj = doit(
        "user/empty_2d_array_of_objects/1", "value", [[{"value": numpy.int16(42)}]]
    )
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.shape, (1, 1))
    nose.tools.eq_(obj.value.dtype, numpy.object)
    nose.tools.assert_true(numpy.equal(obj.value[0][0].value, 42))


# ----------------------------------------------------------


def test_empty_3d_array_of_objects():
    obj = doit(
        "user/empty_3d_array_of_objects/1", "value", [[[{"value": numpy.int16(42)}]]]
    )
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.shape, (1, 1, 1))
    nose.tools.eq_(obj.value.dtype, numpy.object)
    nose.tools.assert_true(numpy.equal(obj.value[0][0][0].value, 42))


# ----------------------------------------------------------


def test_1d_array_of_objects():
    obj = doit("user/1d_array_of_objects/1", "value", 10 * [{"value": numpy.int16(42)}])
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.assert_true(obj.value.shape == (10,))
    nose.tools.assert_true(obj.value.dtype == numpy.object)
    nose.tools.assert_true(numpy.equal(obj.value[0].value, 42))


# ----------------------------------------------------------


def test_2d_array_of_objects():
    v = numpy.array(50 * [{"value": numpy.int16(42)}]).reshape(10, 5)
    obj = doit("user/2d_array_of_objects/1", "value", v)
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.assert_true(obj.value.shape == (10, 5))
    nose.tools.assert_true(obj.value.dtype == numpy.object)
    nose.tools.assert_true(numpy.equal(obj.value[0][0].value, 42))


# ----------------------------------------------------------


def test_3d_array_of_objects():
    v = numpy.array(100 * [{"value": numpy.int16(42)}]).reshape(10, 5, 2)
    obj = doit("user/3d_array_of_objects/1", "value", v)
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.shape, (10, 5, 2))
    nose.tools.eq_(obj.value.dtype, numpy.object)
    nose.tools.assert_true(numpy.equal(obj.value[0][0][0].value, 42))


# ----------------------------------------------------------


def doit_array(format, key, value, index):

    df = DataFormat(prefix, format)
    nose.tools.assert_true(df.valid, df.errors)
    obj = df.type()
    array = getattr(obj, key)
    array[index] = value
    return obj


# ----------------------------------------------------------


def test_1d_array_of_strings_content():
    obj = doit_array("user/1d_array_of_strings/1", "value", "anjos", (2,))
    nose.tools.eq_(obj.value[2], "anjos")


# ----------------------------------------------------------


def test_1d_array_of_objects_contents():
    obj = doit_array(
        "user/1d_array_of_objects/1", "value", {"value": numpy.int16(42)}, (5,)
    )
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.shape, (10,))
    nose.tools.eq_(obj.value.dtype, numpy.object)
    nose.tools.assert_true(numpy.equal(obj.value[5].value, 42))


# ----------------------------------------------------------


def test_2d_array_of_objects_contents():
    obj = doit_array(
        "user/2d_array_of_objects/1", "value", {"value": numpy.int16(42)}, (5, 3)
    )
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.shape, (10, 5))
    nose.tools.eq_(obj.value.dtype, numpy.object)
    nose.tools.assert_true(numpy.equal(obj.value[5][3].value, 42))


# ----------------------------------------------------------


def test_3d_array_of_objects_contents():
    obj = doit_array(
        "user/3d_array_of_objects/1", "value", {"value": numpy.int16(42)}, (5, 3, 0)
    )
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.shape, (10, 5, 2))
    nose.tools.eq_(obj.value.dtype, numpy.object)
    nose.tools.assert_true(numpy.equal(obj.value[5][3][0].value, 42))


# ----------------------------------------------------------


def test_1d_array_of_dataformat_content():
    obj = doit_array(
        "user/1d_array_of_dataformat/1", "value", {"value16": numpy.int16(42)}, (5,)
    )
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.shape, (10,))
    nose.tools.eq_(obj.value.dtype, numpy.object)
    nose.tools.assert_true(numpy.equal(obj.value[5].value8, 0))
    nose.tools.assert_true(numpy.equal(obj.value[5].value16, 42))
    nose.tools.assert_true(numpy.equal(obj.value[4].value8, 0))
    nose.tools.assert_true(numpy.equal(obj.value[4].value16, 0))


# ----------------------------------------------------------


def test_2d_array_of_dataformat_content():
    obj = doit_array(
        "user/2d_array_of_dataformat/1", "value", {"value16": numpy.int16(42)}, (5, 3)
    )
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.shape, (10, 5))
    nose.tools.eq_(obj.value.dtype, numpy.object)
    nose.tools.assert_true(numpy.equal(obj.value[5][3].value8, 0))
    nose.tools.assert_true(numpy.equal(obj.value[5][3].value16, 42))
    nose.tools.assert_true(numpy.equal(obj.value[4][3].value8, 0))
    nose.tools.assert_true(numpy.equal(obj.value[4][3].value16, 0))


# ----------------------------------------------------------


def test_3d_array_of_dataformat_content():
    obj = doit_array(
        "user/3d_array_of_dataformat/1",
        "value",
        {"value16": numpy.int16(42)},
        (5, 3, 0),
    )
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.shape, (10, 5, 2))
    nose.tools.eq_(obj.value.dtype, numpy.object)
    nose.tools.assert_true(numpy.equal(obj.value[5][3][0].value8, 0))
    nose.tools.assert_true(numpy.equal(obj.value[5][3][0].value16, 42))
    nose.tools.assert_true(numpy.equal(obj.value[4][3][0].value8, 0))
    nose.tools.assert_true(numpy.equal(obj.value[4][3][0].value16, 0))
