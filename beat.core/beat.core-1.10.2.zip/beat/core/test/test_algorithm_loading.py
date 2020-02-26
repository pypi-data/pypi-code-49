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

from ..algorithm import Algorithm

from . import prefix, tmp_prefix
from .utils import cleanup


# ----------------------------------------------------------


def test_load_default_algorithm():

    algorithm = Algorithm(prefix, data=None)
    nose.tools.assert_true(
        algorithm.valid, "\n  * %s" % "\n  * ".join(algorithm.errors)
    )


# ----------------------------------------------------------


def test_missing_inputs():

    algorithm = Algorithm(prefix, "errors/no_inputs_declarations/1")
    nose.tools.assert_false(algorithm.valid)
    nose.tools.assert_not_equal(
        algorithm.errors[0].find("'inputs' is a required property"), -1
    )


# ----------------------------------------------------------


def test_missing_outputs():

    algorithm = Algorithm(prefix, "errors/no_outputs_declarations/1")
    nose.tools.assert_false(algorithm.valid)
    nose.tools.assert_not_equal(
        algorithm.errors[0].find("'outputs' is a required property"), -1
    )


# ----------------------------------------------------------


def test_invalid_loop_channel():

    algorithm = Algorithm(prefix, "schema/invalid_loop_channel/1")
    nose.tools.assert_false(algorithm.valid)
    nose.tools.assert_not_equal(
        algorithm.errors[0].find("'request' is a required property"), -1
    )


# ----------------------------------------------------------


def test_duplicate_key():

    algorithm = Algorithm(prefix, "schema/invalid_duplicate_key/1")
    nose.tools.assert_false(algorithm.valid)
    nose.tools.assert_not_equal(algorithm.errors[0].find("Invalid file content"), -1)


# ----------------------------------------------------------


def test_v2():

    algorithm = Algorithm(prefix, "user/integers_add_v2/1")
    nose.tools.assert_true(
        algorithm.valid, "\n  * %s" % "\n  * ".join(algorithm.errors)
    )


def test_analyzer_v2():

    algorithm = Algorithm(prefix, "user/integers_echo_analyzer_v2/1")
    nose.tools.assert_true(
        algorithm.valid, "\n  * %s" % "\n  * ".join(algorithm.errors)
    )


def test_analyzer_v2_invalid_parameters():

    algorithm = Algorithm(prefix, "schema/invalid_analyzer_parameters/1")
    nose.tools.assert_false(algorithm.valid)


def test_v3():

    algorithm = Algorithm(prefix, "autonomous/loop_evaluator/1")
    nose.tools.assert_true(
        algorithm.valid, "\n  * %s" % "\n  * ".join(algorithm.errors)
    )

    algorithm = Algorithm(prefix, "autonomous/loop_processor/1")
    nose.tools.assert_true(
        algorithm.valid, "\n  * %s" % "\n  * ".join(algorithm.errors)
    )


def test_invalid_v3():
    algorithm = Algorithm(prefix, "schema/invalid_loop_output/1")
    nose.tools.assert_false(algorithm.valid)

    algorithm = Algorithm(prefix, "schema/invalid_loop_type/1")
    nose.tools.assert_false(algorithm.valid)

    algorithm = Algorithm(prefix, "schema/invalid_loop_user_type/1")
    nose.tools.assert_false(algorithm.valid)


# ----------------------------------------------------------


@nose.tools.with_setup(teardown=cleanup)
def test_export():

    name = "v1/for_dep/1"
    obj = Algorithm(prefix, name)
    nose.tools.assert_true(obj.valid, "\n  * %s" % "\n  * ".join(obj.errors))

    obj.export(tmp_prefix)

    # load from tmp_prefix and validates
    exported = Algorithm(tmp_prefix, name)
    nose.tools.assert_true(exported.valid, "\n  * %s" % "\n  * ".join(exported.errors))
