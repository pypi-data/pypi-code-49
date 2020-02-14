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


def test_single_object():

    df = DataFormat(prefix, "user/single_object/1")
    nose.tools.assert_true(df.valid, df.errors)
    ftype = df.type

    # checks object creation
    obj = ftype(obj=dict(value1=numpy.int32(32), value2=True))
    nose.tools.assert_true(isinstance(obj, ftype))
    nose.tools.assert_true(isinstance(obj.obj.value1, numpy.int32))
    nose.tools.eq_(obj.obj.value1, 32)
    nose.tools.assert_true(isinstance(obj.obj.value2, numpy.bool_))
    nose.tools.eq_(obj.obj.value2, True)

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


def test_two_objects():

    df = DataFormat(prefix, "user/two_objects/1")
    nose.tools.assert_true(df.valid, df.errors)
    ftype = df.type

    # checks object creation
    obj = ftype(
        obj1=dict(value1=numpy.int32(32), value2=True),
        obj2=dict(value1=numpy.float32(3.14), value2="123"),
    )
    nose.tools.assert_true(isinstance(obj, ftype))
    nose.tools.assert_true(isinstance(obj.obj1.value1, numpy.int32))
    nose.tools.eq_(obj.obj1.value1, 32)
    nose.tools.assert_true(isinstance(obj.obj1.value2, numpy.bool_))
    nose.tools.eq_(obj.obj1.value2, True)
    nose.tools.assert_true(isinstance(obj.obj2.value1, numpy.float32))
    nose.tools.assert_true(numpy.isclose(obj.obj2.value1, 3.14))
    nose.tools.assert_true(isinstance(obj.obj2.value2, str))
    nose.tools.eq_(obj.obj2.value2, "123")

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


def test_hierarchy_of_objects():

    df = DataFormat(prefix, "user/hierarchy_of_objects/1")
    nose.tools.assert_true(df.valid, df.errors)
    ftype = df.type

    # checks object creation
    obj = ftype(obj1=dict(obj2=dict(obj3=dict(value=numpy.int32(32)))))

    nose.tools.assert_true(isinstance(obj, ftype))
    nose.tools.assert_true(isinstance(obj.obj1.obj2.obj3.value, numpy.int32))
    nose.tools.eq_(obj.obj1.obj2.obj3.value, 32)

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


def test_array_of_dict_objects():

    df = DataFormat(prefix, "user/1d_array_of_objects3/1")
    nose.tools.assert_true(df.valid, df.errors)
    ftype = df.type

    # checks object creation
    obj = ftype(
        value=[
            dict(
                id=numpy.int32(17),
                coordinates=dict(x=numpy.int32(15), y=numpy.int32(21)),
            ),
            dict(
                id=numpy.int32(4), coordinates=dict(x=numpy.int32(3), y=numpy.int32(-5))
            ),
        ]
    )

    nose.tools.assert_true(isinstance(obj, ftype))
    nose.tools.assert_true(isinstance(obj.value[0].id, numpy.int32))
    nose.tools.eq_(obj.value[0].id, 17)
    nose.tools.assert_true(isinstance(obj.value[0].coordinates.x, numpy.int32))
    nose.tools.eq_(obj.value[0].coordinates.x, 15)
    nose.tools.assert_true(isinstance(obj.value[0].coordinates.y, numpy.int32))
    nose.tools.eq_(obj.value[0].coordinates.y, 21)
    nose.tools.eq_(obj.value[1].id, 4)
    nose.tools.assert_true(isinstance(obj.value[1].coordinates.x, numpy.int32))
    nose.tools.eq_(obj.value[1].coordinates.x, 3)
    nose.tools.assert_true(isinstance(obj.value[1].coordinates.y, numpy.int32))
    nose.tools.eq_(obj.value[1].coordinates.y, -5)

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


def test_array_of_dict_complex_objects():

    df = DataFormat(prefix, "user/1d_array_of_objects4/1")
    nose.tools.assert_true(df.valid, df.errors)
    ftype = df.type

    # checks object creation
    obj = ftype(
        value=[
            dict(id=numpy.int32(17), name="abc", value=complex(1.2, -3.5)),
            dict(id=numpy.int32(42), name="123", value=complex(-0.2, 47.4)),
        ]
    )

    nose.tools.assert_true(isinstance(obj, ftype))
    nose.tools.assert_true(isinstance(obj.value[0].id, numpy.int32))
    nose.tools.eq_(obj.value[0].id, 17)
    nose.tools.assert_true(isinstance(obj.value[0].name, str))
    nose.tools.eq_(obj.value[0].name, "abc")
    nose.tools.assert_true(isinstance(obj.value[0].value, numpy.complex128))
    nose.tools.assert_true(numpy.isclose(obj.value[0].value, complex(1.2, -3.5)))
    nose.tools.assert_true(isinstance(obj.value[1].id, numpy.int32))
    nose.tools.eq_(obj.value[1].id, 42)
    nose.tools.assert_true(isinstance(obj.value[1].name, str))
    nose.tools.eq_(obj.value[1].name, "123")
    nose.tools.assert_true(isinstance(obj.value[1].value, numpy.complex128))
    nose.tools.assert_true(numpy.isclose(obj.value[1].value, complex(-0.2, 47.4)))

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


def test_differs():

    df = DataFormat(prefix, "user/1d_array_of_objects4/1")
    nose.tools.assert_true(df.valid, df.errors)
    ftype = df.type

    # checks object creation
    obj1 = ftype(
        value=[
            dict(id=numpy.int32(17), name="abc", value=complex(1.2, -3.5)),
            dict(id=numpy.int32(42), name="123", value=complex(-0.2, 47.4)),
        ]
    )

    obj2 = obj1.copy()
    obj3 = obj1.copy()
    obj3.value[1].value = complex(-0.2, 47.5)

    nose.tools.assert_true(obj1.isclose(obj2), "%s != %s" % (obj1, obj2))
    nose.tools.assert_false(obj1.isclose(obj3), "%s == %s" % (obj1, obj3))
