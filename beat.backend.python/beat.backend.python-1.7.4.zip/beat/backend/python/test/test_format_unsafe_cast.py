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
import nose.tools

from ..dataformat import DataFormat

from . import prefix


number42L = long(42) if six.PY2 else int(42)  # noqa


# ----------------------------------------------------------


def doit(format, key, value):

    df = DataFormat(prefix, format)
    nose.tools.assert_true(df.valid, df.errors)
    obj = df.type()
    setattr(obj, key, value)


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_single_integer():
    doit("user/single_integer/1", "value", number42L)


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_single_unsigned_integer():
    doit("user/single_unsigned_integer/1", "value", -number42L)


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_single_unsigned_integer64():
    doit("user/single_unsigned_integer64/1", "value", -number42L)


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_single_float():
    doit("user/single_float/1", "value", complex(4, 6))


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_single_boolean():
    doit("user/single_boolean/1", "value", 42)


# ----------------------------------------------------------


@nose.tools.nottest  # string conversion is always possible
@nose.tools.raises(TypeError)
def test_single_string():
    doit("user/single_string/1", "value", False)


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_single_object_fields():
    doit("user/single_object/1", "obj", dict(value1="abc", value2=False))


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_hierarchy_of_objects():
    doit("user/hierarchy_of_objects/1", "obj1", dict(obj2=dict(obj3={"value": 3.4})))


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_hierarchy_of_objects_fields():
    doit(
        "user/hierarchy_of_objects/1",
        "obj1",
        dict(obj2=dict(obj3=dict(value=number42L))),
    )


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_empty_1d_array_of_integers():
    doit("user/empty_1d_array_of_integers/1", "value", number42L)


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_empty_2d_array_of_integers():
    doit("user/empty_2d_array_of_integers/1", "value", number42L)


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_empty_3d_array_of_integers():
    doit("user/empty_3d_array_of_integers/1", "value", number42L)


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_1d_array_of_integers():
    doit("user/1d_array_of_integers/1", "value", number42L)


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_2d_array_of_integers():
    doit("user/2d_array_of_integers/1", "value", number42L)


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_3d_array_of_integers():
    doit("user/3d_array_of_integers/1", "value", number42L)


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_empty_1d_array_of_objects():
    doit("user/empty_1d_array_of_objects/1", "value", number42L)


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_empty_1d_array_of_objects4():
    doit("user/empty_1d_array_of_objects4/1", "value", number42L)


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_empty_2d_array_of_objects():
    doit("user/empty_2d_array_of_objects/1", "value", number42L)


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_empty_3d_array_of_objects():
    doit("user/empty_3d_array_of_objects/1", "value", number42L)


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_1d_array_of_objects():
    doit("user/1d_array_of_objects/1", "value", number42L)


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_2d_array_of_objects():
    doit("user/2d_array_of_objects/1", "value", number42L)


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_3d_array_of_objects():
    doit("user/3d_array_of_objects/1", "value", number42L)


# ----------------------------------------------------------


def doit_array(format, key, value, index):

    df = DataFormat(prefix, format)
    nose.tools.assert_true(df.valid, df.errors)
    obj = df.type()
    array = getattr(obj, key)
    array[index] = value


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_1d_array_of_strings_content():
    doit_array("user/1d_array_of_strings/1", "value", 42, (2,))


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_1d_array_of_objects_contents():
    doit_array("user/1d_array_of_objects/1", "value", {"value": number42L}, (5,))


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_2d_array_of_objects_contents():
    doit_array("user/2d_array_of_objects/1", "value", {"value": number42L}, (5, 3))


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_3d_array_of_objects_contents():
    doit_array("user/3d_array_of_objects/1", "value", {"value": number42L}, (5, 3, 0))


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_empty_1d_array_of_dataformat():
    doit_array("user/empty_1d_array_of_dataformat/1", "value", {})


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_empty_2d_array_of_dataformat():
    doit_array("user/empty_2d_array_of_dataformat/1", "value", {})


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_empty_3d_array_of_dataformat():
    doit_array("user/empty_3d_array_of_dataformat/1", "value", {})


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_1d_array_of_dataformat():
    doit_array("user/1d_array_of_dataformat/1", "value", {"value8": number42L}, (5,))


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_2d_array_of_dataformat():
    doit_array("user/2d_array_of_dataformat/1", "value", {"value8": number42L}, (5, 3))


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_3d_array_of_dataformat():
    doit_array(
        "user/3d_array_of_dataformat/1", "value", {"value8": number42L}, (5, 3, 0)
    )


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_1d_array_of_dataformat_content():
    doit_array("user/1d_array_of_dataformat/1", "value", {"value8": number42L}, (5,))


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_2d_array_of_dataformat_content():
    doit_array("user/2d_array_of_dataformat/1", "value", {"value8": number42L}, (5, 3))


# ----------------------------------------------------------


@nose.tools.raises(TypeError)
def test_3d_array_of_dataformat_content():
    doit_array(
        "user/3d_array_of_dataformat/1", "value", {"value8": number42L}, (5, 3, 0)
    )
