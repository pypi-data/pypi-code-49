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
from ..protocoltemplate import ProtocolTemplate

from . import prefix


# ----------------------------------------------------------


def load(pt_name):

    protocol_template = ProtocolTemplate(prefix, pt_name)
    nose.tools.assert_true(
        protocol_template.valid, "\n  * %s" % "\n  * ".join(protocol_template.errors)
    )
    return protocol_template


# ----------------------------------------------------------


def test_load_valid_protocol_template():
    for name, set_size in [("double/1", 1), ("triple/1", 1), ("two_sets/1", 2)]:
        yield load_valid_protocol_template, name, set_size


def load_valid_protocol_template(name, set_size):

    protocol_template = load(name)

    nose.tools.eq_(len(protocol_template.sets()), set_size)


# ----------------------------------------------------------


def test_load_protocol_with_one_set():

    protocol_template = load("double/1")
    nose.tools.eq_(len(protocol_template.sets()), 1)

    set_ = protocol_template.set("double")

    nose.tools.eq_(set_["name"], "double")
    nose.tools.eq_(len(set_["outputs"]), 3)

    nose.tools.assert_is_not_none(set_["outputs"]["a"])
    nose.tools.assert_is_not_none(set_["outputs"]["b"])
    nose.tools.assert_is_not_none(set_["outputs"]["sum"])


# ----------------------------------------------------------


def test_load_protocol_with_two_sets():

    protocol_template = load("two_sets/1")
    nose.tools.eq_(len(protocol_template.sets()), 2)

    set_ = protocol_template.set("double")

    nose.tools.eq_(set_["name"], "double")
    nose.tools.eq_(len(set_["outputs"]), 3)

    nose.tools.assert_is_not_none(set_["outputs"]["a"])
    nose.tools.assert_is_not_none(set_["outputs"]["b"])
    nose.tools.assert_is_not_none(set_["outputs"]["sum"])

    set_ = protocol_template.set("triple")

    nose.tools.eq_(set_["name"], "triple")
    nose.tools.eq_(len(set_["outputs"]), 4)

    nose.tools.assert_is_not_none(set_["outputs"]["a"])
    nose.tools.assert_is_not_none(set_["outputs"]["b"])
    nose.tools.assert_is_not_none(set_["outputs"]["c"])
    nose.tools.assert_is_not_none(set_["outputs"]["sum"])


# ----------------------------------------------------------


def test_duplicate_key_error():
    protocoltemplate = ProtocolTemplate(prefix, "duplicate_key_error/1")
    nose.tools.assert_false(protocoltemplate.valid)
    nose.tools.assert_true(
        "Protocol template declaration file invalid" in protocoltemplate.errors[0]
    )
