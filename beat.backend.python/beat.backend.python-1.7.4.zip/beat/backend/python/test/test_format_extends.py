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
    nose.tools.assert_true(df.valid, "\n  * %s" % "\n  * ".join(df.errors))
    ftype = df.type

    obj = ftype()

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

    return obj


# ----------------------------------------------------------


def test_valid():
    obj = doit("user/extended/1")

    nose.tools.assert_true(hasattr(obj, "value"))
    nose.tools.assert_true(isinstance(obj.value, numpy.int32))
    nose.tools.assert_true(hasattr(obj, "value2"))
    nose.tools.assert_true(isinstance(obj.value2, numpy.bool_))


# ----------------------------------------------------------


def test_extension_of_extended():
    obj = doit("user/extended2/1")

    nose.tools.assert_true(hasattr(obj, "value"))
    nose.tools.assert_true(isinstance(obj.value, numpy.int32))
    nose.tools.assert_true(hasattr(obj, "value2"))
    nose.tools.assert_true(isinstance(obj.value2, numpy.bool_))
    nose.tools.assert_true(hasattr(obj, "value3"))
    nose.tools.assert_true(isinstance(obj.value3, numpy.float32))


# ----------------------------------------------------------


def test_issubclass():
    first = DataFormat(prefix, "user/single_integer/1")
    nose.tools.assert_true(first.valid, "\n  * %s" % "\n  * ".join(first.errors))

    middle = DataFormat(prefix, "user/extended/1")
    nose.tools.assert_true(middle.valid, "\n  * %s" % "\n  * ".join(middle.errors))

    last = DataFormat(prefix, "user/extended2/1")
    nose.tools.assert_true(last.valid, "\n  * %s" % "\n  * ".join(last.errors))

    nose.tools.assert_true(first.isparent(middle))
    nose.tools.assert_true(middle.isparent(last))
    nose.tools.assert_true(first.isparent(last))  # two hops
