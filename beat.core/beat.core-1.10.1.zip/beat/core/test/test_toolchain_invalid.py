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
from ..toolchain import Toolchain

from . import prefix


def count_errors(l, e):
    """Makes sure a given string is present in one of the errors"""
    return sum([int(k.find(e) != -1) for k in l])


def test_load_default():

    toolchain = Toolchain(prefix, data=None)
    nose.tools.assert_true(
        toolchain.valid, "\n  * %s" % "\n  * ".join(toolchain.errors)
    )


def test_load_unknown_toolchain():

    toolchain = Toolchain(prefix, "errors/unknown/1")
    nose.tools.assert_false(toolchain.valid)
    nose.tools.eq_(count_errors(toolchain.errors, "file not found"), 1)


def test_load_invalid_toolchain():

    toolchain = Toolchain(prefix, "errors/invalid/1")
    nose.tools.assert_false(toolchain.valid)
    nose.tools.eq_(count_errors(toolchain.errors, "invalid JSON"), 1)


def test_load_toolchain_without_blocks_list():

    toolchain = Toolchain(prefix, "errors/missing_blocks/1")
    nose.tools.assert_false(toolchain.valid)
    nose.tools.eq_(count_errors(toolchain.errors, "'blocks' is a required property"), 1)


def test_load_toolchain_with_missing_block_name():

    toolchain = Toolchain(prefix, "errors/missing_block_name/1")
    nose.tools.assert_false(toolchain.valid)
    nose.tools.eq_(count_errors(toolchain.errors, "'name' is a required property"), 1)


def test_load_toolchain_with_missing_block_inputs():

    toolchain = Toolchain(prefix, "errors/missing_block_inputs/1")
    nose.tools.assert_false(toolchain.valid)
    nose.tools.eq_(count_errors(toolchain.errors, "'inputs' is a required property"), 1)


def test_load_toolchain_with_missing_block_outputs():

    toolchain = Toolchain(prefix, "errors/missing_block_outputs/1")
    nose.tools.assert_false(toolchain.valid)
    nose.tools.eq_(
        count_errors(toolchain.errors, "'outputs' is a required property"), 1
    )


def test_load_toolchain_without_datasets_list():

    toolchain = Toolchain(prefix, "errors/missing_datasets/1")
    nose.tools.assert_false(toolchain.valid)
    nose.tools.eq_(
        count_errors(toolchain.errors, "'datasets' is a required property"), 1
    )


def test_load_toolchain_with_missing_dataset_name():

    toolchain = Toolchain(prefix, "errors/missing_dataset_name/1")
    nose.tools.assert_false(toolchain.valid)
    nose.tools.eq_(count_errors(toolchain.errors, "'name' is a required property"), 1)


def test_load_toolchain_with_missing_dataset_outputs():

    toolchain = Toolchain(prefix, "errors/missing_dataset_outputs/1")
    nose.tools.assert_false(toolchain.valid)
    nose.tools.eq_(
        count_errors(toolchain.errors, "'outputs' is a required property"), 1
    )


def test_load_toolchain_with_missing_connection_from():

    toolchain = Toolchain(prefix, "errors/missing_connection_from/1")
    nose.tools.assert_false(toolchain.valid)
    nose.tools.eq_(count_errors(toolchain.errors, "'from' is a required property"), 1)


def test_load_toolchain_with_missing_connection_to():

    toolchain = Toolchain(prefix, "errors/missing_connection_to/1")
    nose.tools.assert_false(toolchain.valid)
    nose.tools.eq_(count_errors(toolchain.errors, "'to' is a required property"), 1)


def test_load_toolchain_referencing_unknown_block_input():

    toolchain = Toolchain(prefix, "errors/unknown_block_input/1")
    nose.tools.assert_false(toolchain.valid)
    nose.tools.eq_(
        count_errors(toolchain.errors, "invalid input endpoint 'addition.c'"), 1
    )


def test_load_toolchain_referencing_unknown_dataset_output():

    toolchain = Toolchain(prefix, "errors/unknown_dataset_output/1")
    nose.tools.assert_false(toolchain.valid)
    nose.tools.eq_(
        count_errors(toolchain.errors, "invalid output endpoint 'integers.timestamps'"),
        1,
    )


def test_load_toolchain_referencing_unknown_block_output():

    toolchain = Toolchain(prefix, "errors/unknown_block_output/1")
    nose.tools.assert_false(toolchain.valid)
    nose.tools.eq_(
        count_errors(toolchain.errors, "invalid output endpoint 'addition.unknown'"), 1
    )


def test_load_toolchain_referencing_unknown_analyzer_input():

    toolchain = Toolchain(prefix, "errors/unknown_analyzer_input/1")
    nose.tools.assert_false(toolchain.valid)
    nose.tools.eq_(
        count_errors(toolchain.errors, "invalid input endpoint 'analysis.unknown'"), 1
    )


def test_load_toolchain_unconnected_input():

    toolchain = Toolchain(prefix, "errors/unconnected_input/1")
    nose.tools.assert_false(toolchain.valid)
    nose.tools.eq_(
        count_errors(toolchain.errors, "input(s) `addition.b' remain unconnected"), 1
    )


def test_load_toolchain_double_connected_input():

    toolchain = Toolchain(prefix, "errors/double_connected_input/1")
    nose.tools.assert_false(toolchain.valid)
    nose.tools.eq_(count_errors(toolchain.errors, "ending on the same input as"), 1)
