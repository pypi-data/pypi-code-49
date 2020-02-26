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


def test_valid():

    df = DataFormat(prefix, "user/composed/1")
    nose.tools.assert_true(df.valid)

    ftype = df.type

    nose.tools.assert_true(numpy.issubdtype(ftype.integers.value8, numpy.int8))
    nose.tools.assert_true(numpy.issubdtype(ftype.integers.value16, numpy.int16))
    nose.tools.assert_true(numpy.issubdtype(ftype.integers.value32, numpy.int32))
    nose.tools.assert_true(numpy.issubdtype(ftype.integers.value64, numpy.int64))
    nose.tools.assert_true(numpy.issubdtype(ftype.floats.value32, numpy.float32))
    nose.tools.assert_true(numpy.issubdtype(ftype.floats.value64, numpy.float64))

    obj = ftype(
        integers=dict(
            value8=numpy.int8(2 ** 6),
            value16=numpy.int16(2 ** 14),
            value32=numpy.int32(2 ** 30),
            value64=numpy.int64(2 ** 62),
        ),
        floats=dict(value32=numpy.float32(3.14), value64=numpy.float64(2.78)),
    )

    nose.tools.eq_(obj.integers.value8.dtype, numpy.int8)
    nose.tools.eq_(obj.integers.value8, 2 ** 6)

    nose.tools.eq_(obj.integers.value16.dtype, numpy.int16)
    nose.tools.eq_(obj.integers.value16, 2 ** 14)

    nose.tools.eq_(obj.integers.value32.dtype, numpy.int32)
    nose.tools.eq_(obj.integers.value32, 2 ** 30)

    nose.tools.eq_(obj.integers.value64.dtype, numpy.int64)
    nose.tools.eq_(obj.integers.value64, 2 ** 62)

    nose.tools.eq_(obj.floats.value32.dtype, numpy.float32)
    nose.tools.assert_true(numpy.isclose(obj.floats.value32, 3.14))

    nose.tools.eq_(obj.floats.value64.dtype, numpy.float64)
    nose.tools.assert_true(numpy.isclose(obj.floats.value64, 2.78))

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


def test_invalid():

    df = DataFormat(prefix, "user/composed_unknown/1")
    nose.tools.assert_false(df.valid)
    nose.tools.assert_not_equal(df.errors[0].find("referred dataformat"), -1)
    nose.tools.assert_not_equal(df.errors[0].find("invalid"), -1)
