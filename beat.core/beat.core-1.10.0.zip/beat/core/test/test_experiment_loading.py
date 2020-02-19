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
import nose.tools
from ..experiment import Experiment

from . import prefix, tmp_prefix
from .utils import cleanup


# ----------------------------------------------------------


@nose.tools.raises(RuntimeError)
def test_load_default_experiment_fails():
    Experiment(prefix, data=None)


# ----------------------------------------------------------


def test_load_valid_experiment():

    experiment = Experiment(prefix, "user/integers_addition/1/integers_addition")

    nose.tools.assert_true(
        experiment.valid, "\n  * %s" % "\n  * ".join(experiment.errors)
    )
    nose.tools.eq_(experiment.label, "user/user/integers_addition/1/integers_addition")

    nose.tools.assert_true(
        experiment.toolchain.valid,
        "\n  * %s" % "\n  * ".join(experiment.toolchain.errors),
    )
    nose.tools.eq_(experiment.toolchain.name, "user/integers_addition/1")

    nose.tools.eq_(len(experiment.datasets), 1)
    nose.tools.assert_true("integers" in experiment.datasets)
    nose.tools.eq_(len(experiment.databases), 1)
    nose.tools.eq_(len(experiment.blocks), 1)
    nose.tools.eq_(len(experiment.analyzers), 1)

    nose.tools.eq_(len(experiment.algorithms), 2)
    nose.tools.assert_true("v1/sum/1" in experiment.algorithms)
    nose.tools.assert_true(experiment.algorithms["v1/sum/1"].valid)
    nose.tools.assert_true("v1/integers_analysis/1" in experiment.algorithms)
    nose.tools.assert_true(experiment.algorithms["v1/integers_analysis/1"].valid)


def test_load_one_dataset_two_blocks_toolchain():

    experiment = Experiment(prefix, "user/integers_addition/2/integers_addition")
    nose.tools.assert_true(
        experiment.valid, "\n  * %s" % "\n  * ".join(experiment.errors)
    )
    nose.tools.eq_(experiment.label, "user/user/integers_addition/2/integers_addition")

    nose.tools.assert_true(
        experiment.toolchain.valid,
        "\n  * %s" % "\n  * ".join(experiment.toolchain.errors),
    )
    nose.tools.eq_(experiment.toolchain.name, "user/integers_addition/2")

    nose.tools.eq_(len(experiment.datasets), 1)
    nose.tools.assert_true("integers" in experiment.datasets)
    nose.tools.eq_(len(experiment.databases), 1)
    nose.tools.eq_(len(experiment.blocks), 2)
    nose.tools.eq_(len(experiment.analyzers), 1)

    nose.tools.eq_(len(experiment.algorithms), 2)
    nose.tools.assert_true("v1/sum/1" in experiment.algorithms)
    nose.tools.assert_true(experiment.algorithms["v1/sum/1"].valid)
    nose.tools.assert_true("v1/integers_analysis/1" in experiment.algorithms)
    nose.tools.assert_true(experiment.algorithms["v1/integers_analysis/1"].valid)


def test_load_two_datasets_three_blocks_toolchain():

    experiment = Experiment(prefix, "user/integers_addition/3/integers_addition")
    nose.tools.assert_false(experiment.valid)
    nose.tools.eq_(experiment.label, "user/user/integers_addition/3/integers_addition")
    nose.tools.assert_not_equal(
        experiment.errors[0].find("mismatch in input/output"), -1
    )

    nose.tools.assert_true(experiment.toolchain.valid)
    nose.tools.eq_(experiment.toolchain.name, "user/integers_addition/3")

    nose.tools.eq_(len(experiment.datasets), 2)
    nose.tools.assert_true("integers1" in experiment.datasets)
    nose.tools.assert_true("integers2" in experiment.datasets)
    nose.tools.eq_(len(experiment.databases), 1)
    nose.tools.eq_(len(experiment.blocks), 3)
    nose.tools.eq_(len(experiment.analyzers), 1)

    nose.tools.eq_(len(experiment.algorithms), 2)
    nose.tools.assert_true("v1/sum/1" in experiment.algorithms)
    nose.tools.assert_true(experiment.algorithms["v1/sum/1"].valid)
    nose.tools.assert_true("v1/integers_analysis/1" in experiment.algorithms)
    nose.tools.assert_true(experiment.algorithms["v1/integers_analysis/1"].valid)


def test_no_description():

    experiment = Experiment(prefix, "errors/user/single/1/single_error")
    nose.tools.assert_true(
        experiment.valid, "\n  * %s" % "\n  * ".join(experiment.errors)
    )
    nose.tools.assert_is_none(experiment.description)
    nose.tools.assert_is_none(experiment.documentation)

    description = "This is my descriptor"
    experiment.description = description
    nose.tools.assert_true(isinstance(experiment.description, six.string_types))
    nose.tools.eq_(experiment.description, description)


def test_load_experiment_with_loop():

    experiment = Experiment(prefix, "user/two_loops/1/two_loops")

    nose.tools.assert_true(
        experiment.valid, "\n  * %s" % "\n  * ".join(experiment.errors)
    )
    nose.tools.eq_(experiment.label, "user/user/two_loops/1/two_loops")

    nose.tools.assert_true(
        experiment.toolchain.valid,
        "\n  * %s" % "\n  * ".join(experiment.toolchain.errors),
    )
    nose.tools.eq_(experiment.toolchain.name, "user/two_loops/1")

    nose.tools.eq_(len(experiment.datasets), 2)
    nose.tools.eq_(len(experiment.databases), 2)
    nose.tools.eq_(len(experiment.blocks), 2)
    nose.tools.eq_(len(experiment.loops), 2)
    nose.tools.eq_(len(experiment.analyzers), 2)
    nose.tools.eq_(len(experiment.algorithms), 6)


@nose.tools.with_setup(teardown=cleanup)
def test_export():

    name = "user/integers_addition/1/integers_addition"
    obj = Experiment(prefix, name)
    nose.tools.assert_true(obj.valid, "\n  * %s" % "\n  * ".join(obj.errors))

    obj.export(tmp_prefix)

    # load from tmp_prefix and validates
    exported = Experiment(tmp_prefix, name)
    nose.tools.assert_true(exported.valid, "\n  * %s" % "\n  * ".join(exported.errors))
