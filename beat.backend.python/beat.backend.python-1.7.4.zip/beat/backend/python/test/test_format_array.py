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


def doit(format):

    df = DataFormat(prefix, format)
    nose.tools.assert_true(df.valid, df.errors)
    ftype = df.type

    obj = ftype()
    nose.tools.assert_true(isinstance(obj.value, numpy.ndarray))
    nose.tools.eq_(obj.value.ndim, len(ftype.value) - 1)
    nose.tools.eq_(obj.value.shape, tuple(ftype.value[:-1]))

    if ftype.value[-1] != str:
        nose.tools.eq_(obj.value.dtype, ftype.value[-1])
    else:
        nose.tools.assert_true(
            issubclass(obj.value.dtype.type, object)
        )  # element for strings

    # checks JSON enconding
    copy = ftype(**obj.as_dict())
    nose.tools.assert_true(
        copy.isclose(obj),
        "%r is not close enough to %r" % (copy.as_dict(), obj.as_dict()),
    )

    # checks binary encoding
    copy = ftype()
    copy.unpack(obj.pack())
    nose.tools.assert_true(
        copy.isclose(obj),
        "%r is not close enough to %r" % (copy.as_dict(), obj.as_dict()),
    )


# ----------------------------------------------------------


def test_empty_1d_array_of_integers():
    doit("user/empty_1d_array_of_integers/1")


# ----------------------------------------------------------


def test_empty_2d_array_of_integers():
    doit("user/empty_2d_array_of_integers/1")


# ----------------------------------------------------------


def test_empty_3d_array_of_integers():
    doit("user/empty_3d_array_of_integers/1")


# ----------------------------------------------------------


def test_empty_fixed_2d_array_of_integers():
    doit("user/empty_2d_fixed_array_of_integers/1")


# ----------------------------------------------------------


def test_1d_array_of_integers():
    doit("user/1d_array_of_integers/1")


# ----------------------------------------------------------


def test_2d_array_of_integers():
    doit("user/2d_array_of_integers/1")


# ----------------------------------------------------------


def test_3d_array_of_integers():
    doit("user/3d_array_of_integers/1")


# ----------------------------------------------------------


def test_3d_array_of_integers_pack_unpack():

    df = DataFormat(prefix, "user/3d_array_of_integers/1")
    nose.tools.assert_true(df.valid, df.errors)
    ftype = df.type

    obj = ftype()
    limits = numpy.iinfo(obj.value.dtype)
    obj.value = numpy.random.randint(
        low=limits.min, high=limits.max, size=obj.value.shape
    ).astype(obj.value.dtype)

    # checks JSON enconding
    copy = ftype(**obj.as_dict())
    nose.tools.assert_true(
        copy.isclose(obj),
        "%r is not close enough to %r" % (copy.as_dict(), obj.as_dict()),
    )

    # checks binary encoding
    copy = ftype()
    copy.unpack(obj.pack())
    nose.tools.assert_true(
        copy.isclose(obj),
        "%r is not close enough to %r" % (copy.as_dict(), obj.as_dict()),
    )


# ----------------------------------------------------------


def test_3d_array_of_floats_pack_unpack():

    df = DataFormat(prefix, "user/3d_array_of_floats/1")
    nose.tools.assert_true(df.valid, df.errors)
    ftype = df.type

    obj = ftype()
    obj.value = numpy.random.rand(15, 72, 3).astype(float)

    # checks JSON enconding
    copy = ftype(**obj.as_dict())
    nose.tools.assert_true(
        copy.isclose(obj),
        "%r is not close enough to %r" % (copy.as_dict(), obj.as_dict()),
    )

    # checks binary encoding
    copy = ftype()
    copy.unpack(obj.pack())
    nose.tools.assert_true(
        copy.isclose(obj),
        "%r is not close enough to %r" % (copy.as_dict(), obj.as_dict()),
    )


# ----------------------------------------------------------


def test_3d_array_of_complexes_pack_unpack():

    df = DataFormat(prefix, "user/3d_array_of_complexes/1")
    nose.tools.assert_true(df.valid, df.errors)
    ftype = df.type

    obj = ftype()
    obj.value.real = numpy.random.rand(*obj.value.shape).astype(float)
    obj.value.imag = numpy.random.rand(*obj.value.shape).astype(float)

    # checks JSON enconding
    copy = ftype(**obj.as_dict())
    nose.tools.assert_true(
        copy.isclose(obj),
        "%r is not close enough to %r" % (copy.as_dict(), obj.as_dict()),
    )

    # checks binary encoding
    copy = ftype()
    copy.unpack(obj.pack())
    nose.tools.assert_true(
        copy.isclose(obj),
        "%r is not close enough to %r" % (copy.as_dict(), obj.as_dict()),
    )


# ----------------------------------------------------------


def test_empty_1d_array_of_objects():
    doit("user/empty_1d_array_of_objects/1")


# ----------------------------------------------------------


def test_empty_2d_array_of_objects():
    doit("user/empty_2d_array_of_objects/1")


# ----------------------------------------------------------


def test_empty_3d_array_of_objects():
    doit("user/empty_3d_array_of_objects/1")


# ----------------------------------------------------------


def test_empty_fixed_2d_array_of_objects():
    doit("user/empty_2d_fixed_array_of_objects/1")


# ----------------------------------------------------------


def test_1d_array_of_objects():
    doit("user/1d_array_of_objects/1")


# ----------------------------------------------------------


def test_2d_array_of_objects():
    doit("user/2d_array_of_objects/1")


# ----------------------------------------------------------


def test_3d_array_of_objects():
    doit("user/3d_array_of_objects/1")


# ----------------------------------------------------------


def test_empty_1d_array_of_external_reference():
    doit("user/empty_1d_array_of_dataformat/1")


# ----------------------------------------------------------


def test_empty_2d_array_of_external_reference():
    doit("user/empty_2d_array_of_dataformat/1")


# ----------------------------------------------------------


def test_empty_3d_array_of_external_reference():
    doit("user/empty_3d_array_of_dataformat/1")


# ----------------------------------------------------------


def test_empty_fixed_2d_array_of_external_reference():
    doit("user/empty_2d_fixed_array_of_dataformat/1")


# ----------------------------------------------------------


def test_1d_array_of_external_reference():
    doit("user/1d_array_of_dataformat/1")


# ----------------------------------------------------------


def test_2d_array_of_external_reference():
    doit("user/2d_array_of_dataformat/1")


# ----------------------------------------------------------


def test_3d_array_of_external_reference():
    doit("user/3d_array_of_dataformat/1")


# ----------------------------------------------------------


def test_empty_1d_array_of_external_reference_with_empty_array_of_objects():
    doit("user/empty_1d_array_of_dataformat_with_empty_array_of_objects/1")


# ----------------------------------------------------------


def test_empty_1d_array_of_external_reference_with_array_of_objects():
    doit("user/empty_1d_array_of_dataformat_with_array_of_objects/1")


# ----------------------------------------------------------


def test_1d_array_of_strings():
    doit("user/1d_array_of_strings/1")
