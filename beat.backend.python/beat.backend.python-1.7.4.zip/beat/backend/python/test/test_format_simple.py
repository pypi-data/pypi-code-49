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


def test_integers():

    df = DataFormat(prefix, "user/integers/1")
    nose.tools.assert_true(df.valid, df.errors)

    ftype = df.type

    nose.tools.assert_true(numpy.issubdtype(ftype.value8, numpy.int8))
    nose.tools.assert_true(numpy.issubdtype(ftype.value16, numpy.int16))
    nose.tools.assert_true(numpy.issubdtype(ftype.value32, numpy.int32))
    nose.tools.assert_true(numpy.issubdtype(ftype.value64, numpy.int64))

    obj = ftype(
        value8=numpy.int8(2 ** 6),
        value16=numpy.int16(2 ** 14),
        value32=numpy.int32(2 ** 30),
        value64=numpy.int64(2 ** 62),
    )

    nose.tools.eq_(obj.value8.dtype, numpy.int8)
    nose.tools.eq_(obj.value8, 2 ** 6)

    nose.tools.eq_(obj.value16.dtype, numpy.int16)
    nose.tools.eq_(obj.value16, 2 ** 14)

    nose.tools.eq_(obj.value32.dtype, numpy.int32)
    nose.tools.eq_(obj.value32, 2 ** 30)

    nose.tools.eq_(obj.value64.dtype, numpy.int64)
    nose.tools.eq_(obj.value64, 2 ** 62)

    # checks JSON enconding
    copy = ftype()
    copy.from_dict(obj.as_dict())
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


@nose.tools.raises(TypeError)
def test_integers_unsafe_cast():

    df = DataFormat(prefix, "user/integers/1")
    nose.tools.assert_true(df.valid, df.errors)

    ftype = df.type

    obj = ftype()
    obj.from_dict(dict(value8=2 ** 6), casting="safe", add_defaults=True)


# ----------------------------------------------------------


def test_unsigned_integers():
    df = DataFormat(prefix, "user/unsigned_integers/1")
    nose.tools.assert_true(df.valid, df.errors)

    ftype = df.type

    nose.tools.assert_true(numpy.issubdtype(ftype.value8, numpy.uint8))
    nose.tools.assert_true(numpy.issubdtype(ftype.value16, numpy.uint16))
    nose.tools.assert_true(numpy.issubdtype(ftype.value32, numpy.uint32))
    nose.tools.assert_true(numpy.issubdtype(ftype.value64, numpy.uint64))

    obj = ftype(
        value8=numpy.uint8(2 ** 6),
        value16=numpy.uint16(2 ** 14),
        value32=numpy.uint32(2 ** 30),
        value64=numpy.uint64(2 ** 62),
    )

    nose.tools.eq_(obj.value8.dtype, numpy.uint8)
    nose.tools.eq_(obj.value8, 2 ** 6)

    nose.tools.eq_(obj.value16.dtype, numpy.uint16)
    nose.tools.eq_(obj.value16, 2 ** 14)

    nose.tools.eq_(obj.value32.dtype, numpy.uint32)
    nose.tools.eq_(obj.value32, 2 ** 30)

    nose.tools.eq_(obj.value64.dtype, numpy.uint64)
    nose.tools.eq_(obj.value64, 2 ** 62)

    # checks JSON enconding
    copy = ftype()
    copy.from_dict(obj.as_dict())
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


@nose.tools.raises(TypeError)
def test_unsigned_integers_unsafe_cast():

    df = DataFormat(prefix, "user/unsigned_integers/1")
    nose.tools.assert_true(df.valid, df.errors)

    ftype = df.type

    obj = ftype()
    obj.from_dict(dict(value8=2 ** 6), casting="safe", add_defaults=True)


# ----------------------------------------------------------


@nose.tools.raises(AttributeError)
def test_unsigned_integers_missing_attributes():

    df = DataFormat(prefix, "user/unsigned_integers/1")
    nose.tools.assert_true(df.valid, df.errors)

    ftype = df.type

    obj = ftype()
    obj.from_dict(dict(value8=2 ** 6), casting="safe", add_defaults=False)


# ----------------------------------------------------------


def test_floats():
    df = DataFormat(prefix, "user/floats/1")
    nose.tools.assert_true(df.valid, df.errors)

    ftype = df.type

    nose.tools.assert_true(numpy.issubdtype(ftype.value32, numpy.float32))
    nose.tools.assert_true(numpy.issubdtype(ftype.value64, numpy.float64))

    obj = ftype(value32=numpy.float32(3.0), value64=3.14)

    nose.tools.eq_(obj.value32.dtype, numpy.float32)
    nose.tools.assert_true(numpy.isclose(obj.value32, 3.0))

    nose.tools.eq_(obj.value64.dtype, numpy.float64)
    nose.tools.assert_true(numpy.isclose(obj.value64, 3.14))

    # checks JSON enconding
    copy = ftype()
    copy.from_dict(obj.as_dict())
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


@nose.tools.raises(TypeError)
def test_floats_unsafe_cast():
    df = DataFormat(prefix, "user/floats/1")
    nose.tools.assert_true(df.valid, df.errors)

    ftype = df.type

    nose.tools.assert_true(numpy.issubdtype(ftype.value32, numpy.float32))
    nose.tools.assert_true(numpy.issubdtype(ftype.value64, numpy.float64))

    obj = ftype()
    obj.from_dict(dict(value32=numpy.float64(32.0)), casting="safe", add_defaults=True)


# ----------------------------------------------------------


def test_complexes():
    df = DataFormat(prefix, "user/complexes/1")
    nose.tools.assert_true(df.valid, df.errors)

    ftype = df.type

    nose.tools.assert_true(numpy.issubdtype(ftype.value64, numpy.complex64))
    nose.tools.assert_true(numpy.issubdtype(ftype.value128, numpy.complex128))

    obj = ftype(
        value64=numpy.complex64(complex(1, 2)),
        value128=numpy.complex64(complex(1.4, 2.2)),
    )

    nose.tools.eq_(obj.value64.dtype, numpy.complex64)
    nose.tools.assert_true(numpy.isclose(obj.value64, complex(1, 2)))

    nose.tools.eq_(obj.value128.dtype, numpy.complex128)
    nose.tools.assert_true(numpy.isclose(obj.value128, complex(1.4, 2.2)))

    # checks JSON enconding
    copy = ftype()
    copy.from_dict(obj.as_dict())
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


def test_boolean():
    df = DataFormat(prefix, "user/single_boolean/1")
    nose.tools.assert_true(df.valid, df.errors)

    ftype = df.type

    nose.tools.assert_true(numpy.issubdtype(ftype.value, numpy.bool_))

    obj = ftype(value=True)

    nose.tools.eq_(obj.value.dtype, numpy.bool_)
    nose.tools.assert_true(obj.value)  # must be True

    # checks JSON enconding
    copy = ftype()
    copy.from_dict(obj.as_dict())
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


def test_string():
    df = DataFormat(prefix, "user/single_string/1")
    nose.tools.assert_true(df.valid, df.errors)

    ftype = df.type

    nose.tools.assert_true(numpy.issubdtype(ftype.value, numpy.dtype(str).type))

    obj = ftype(value="123")

    nose.tools.assert_true(isinstance(obj.value, str))
    nose.tools.eq_(obj.value, "123")

    # checks JSON enconding
    copy = ftype()
    copy.from_dict(obj.as_dict())
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


def test_duplicate_key_error():
    df = DataFormat(prefix, "errors/duplicate_key/1")
    nose.tools.assert_false(df.valid)
    nose.tools.assert_true("Dataformat declaration file invalid" in df.errors[0])
