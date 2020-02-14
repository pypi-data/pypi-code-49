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


import nose.tools

from ..dataformat import DataFormat

from . import prefix


# ----------------------------------------------------------


def doit(format, data):

    df = DataFormat(prefix, format)
    nose.tools.assert_true(df.valid, df.errors)
    obj = df.type()
    obj.from_dict(data, casting="unsafe", add_defaults=False)


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_single_integer():
    doit("user/single_integer/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_single_float():
    doit("user/single_float/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_single_boolean():
    doit("user/single_boolean/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_single_string():
    doit("user/single_string/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_single_object():
    doit("user/single_object/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_single_object_field():
    doit("user/single_object/1", dict(obj={}))


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_hierarchy_of_objects():
    doit("user/hierarchy_of_objects/1", dict(obj1=dict(obj2={})))


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_hierarchy_of_objects_field():
    doit("user/hierarchy_of_objects/1", dict(obj1=dict(obj2=dict(obj3={}))))


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_empty_1d_array_of_integers():
    doit("user/empty_1d_array_of_integers/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_empty_2d_array_of_integers():
    doit("user/empty_2d_array_of_integers/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_empty_3d_array_of_integers():
    doit("user/empty_3d_array_of_integers/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_1d_array_of_integers():
    doit("user/1d_array_of_integers/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_2d_array_of_integers():
    doit("user/2d_array_of_integers/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_3d_array_of_integers():
    doit("user/3d_array_of_integers/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_empty_1d_array_of_objects():
    doit("user/empty_1d_array_of_objects/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_empty_1d_array_of_objects4():
    doit("user/empty_1d_array_of_objects4/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_empty_2d_array_of_objects():
    doit("user/empty_2d_array_of_objects/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_empty_3d_array_of_objects():
    doit("user/empty_3d_array_of_objects/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_1d_array_of_objects():
    doit("user/1d_array_of_objects/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_2d_array_of_objects():
    doit("user/2d_array_of_objects/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_3d_array_of_objects():
    doit("user/3d_array_of_objects/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_empty_1d_array_of_dataformat():
    doit("user/empty_1d_array_of_dataformat/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_empty_2d_array_of_dataformat():
    doit("user/empty_2d_array_of_dataformat/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_empty_3d_array_of_dataformat():
    doit("user/empty_3d_array_of_dataformat/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_1d_array_of_dataformat():
    doit("user/1d_array_of_dataformat/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_2d_array_of_dataformat():
    doit("user/2d_array_of_dataformat/1", {})


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_3d_array_of_dataformat():
    doit("user/3d_array_of_dataformat/1", {})
