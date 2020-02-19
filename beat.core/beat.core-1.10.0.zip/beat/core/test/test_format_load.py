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

from ..dataformat import DataFormat

from . import prefix, tmp_prefix
from .utils import cleanup


def test_load_default_format():

    df = DataFormat(prefix, data=None)
    nose.tools.assert_true(df.valid, "\n  * %s" % "\n  * ".join(df.errors))


def test_load_unknown_format():

    df = DataFormat(prefix, "user/unknown/1")
    nose.tools.assert_false(df.valid)
    nose.tools.assert_true(df.errors)
    nose.tools.eq_(len(df.errors), 1)
    nose.tools.assert_not_equal(df.errors[0].find("file not found"), -1)


def test_load_invalid_format():

    df = DataFormat(prefix, "user/invalid/1")
    nose.tools.assert_false(df.valid)
    nose.tools.assert_true(df.errors)
    nose.tools.eq_(len(df.errors), 1)
    nose.tools.assert_not_equal(df.errors[0].find("invalid JSON code"), -1)


def test_load_valid_format():

    df = DataFormat(prefix, "user/single_integer/1")
    nose.tools.assert_true(df.valid, "\n  * %s" % "\n  * ".join(df.errors))
    nose.tools.eq_(len(df.errors), 0)


@nose.tools.raises(RuntimeError)
def test_fail_to_create_data_of_unknown_format():

    df = DataFormat(prefix, "user/unknown/1")
    nose.tools.assert_false(df.valid)
    nose.tools.assert_true(df.type)


def test_fail_to_load_format_with_several_invalid_types():

    df = DataFormat(prefix, "user/errors/1")
    nose.tools.assert_false(df.valid)
    nose.tools.eq_(len(df.errors), 1)
    nose.tools.assert_not_equal(
        df.errors[0].find("is not valid under any of the given schemas"), -1
    )


def test_load_valid_format_from_JSON_declaration():

    df = DataFormat(prefix, dict(value="int32"))
    nose.tools.assert_true(df.valid, "\n  * %s" % "\n  * ".join(df.errors))
    nose.tools.eq_(df.name, "__unnamed_dataformat__")


def test_load_versioned_format():

    df1 = DataFormat(prefix, "user/versioned/1")
    nose.tools.assert_true(df1.valid, "\n  * %s" % "\n  * ".join(df1.errors))
    nose.tools.eq_(df1.name, "user/versioned/1")

    df2 = DataFormat(prefix, "user/versioned/2")
    nose.tools.assert_true(df2.valid, "\n  * %s" % "\n  * ".join(df2.errors))
    nose.tools.eq_(df2.name, "user/versioned/2")

    ftype = df2.type
    instance = ftype(value=numpy.float32(32))
    nose.tools.assert_true(isinstance(instance.value, numpy.float32))


def test_no_description():

    df = DataFormat(prefix, "user/versioned/1")
    nose.tools.assert_true(df.valid, "\n  * %s" % "\n  * ".join(df.errors))
    nose.tools.assert_is_none(df.description)
    nose.tools.assert_is_none(df.documentation)

    description = "This is my descriptor"
    df.description = description
    nose.tools.assert_true(isinstance(df.description, six.string_types))
    nose.tools.eq_(df.description, description)


def test_with_description():

    df = DataFormat(prefix, "user/versioned/2")
    nose.tools.assert_true(df.valid, "\n  * %s" % "\n  * ".join(df.errors))
    nose.tools.assert_true(isinstance(df.description, six.string_types))
    nose.tools.assert_not_equal(len(df.description), 0)
    nose.tools.assert_is_none(df.documentation)


def test_description_does_not_affect_hash():

    df2 = DataFormat(prefix, "user/versioned/2")
    nose.tools.assert_true(df2.valid, "\n  * %s" % "\n  * ".join(df2.errors))
    df3 = DataFormat(prefix, "user/versioned/3")  # the same, but no description
    nose.tools.assert_true(df3.valid, "\n  * %s" % "\n  * ".join(df3.errors))
    nose.tools.eq_(df2.hash(), df3.hash())


def test_load_direct_recursion():

    df = DataFormat(prefix, "user/direct_recursion/1")
    nose.tools.assert_false(df.valid)
    nose.tools.assert_true(df.errors)
    nose.tools.assert_not_equal(df.errors[0].find("recursion for"), -1)
    nose.tools.assert_not_equal(df.errors[0].find("user/direct_recursion/1"), -1)


def test_load_indirect_recursion():

    df = DataFormat(prefix, "user/indirect_recursion_top/1")
    nose.tools.assert_false(df.valid)
    nose.tools.assert_true(df.errors)
    nose.tools.eq_(len(df.errors), 1)
    nose.tools.assert_not_equal(df.errors[0].find("is invalid"), -1)
    nose.tools.assert_not_equal(
        df.errors[0].find("user/indirect_recursion_bottom/1"), -1
    )


@nose.tools.with_setup(teardown=cleanup)
def test_export():

    name = "user/composed/1"
    obj = DataFormat(prefix, name)
    nose.tools.assert_true(obj.valid, "\n  * %s" % "\n  * ".join(obj.errors))

    obj.export(tmp_prefix)

    # load from tmp_prefix and validates
    exported = DataFormat(tmp_prefix, name)
    nose.tools.assert_true(exported.valid, "\n  * %s" % "\n  * ".join(exported.errors))
