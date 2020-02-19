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

from ..plotterparameter import Plotterparameter
from ..plotterparameter import Storage

from . import prefix


def test_default():
    # test for the "dummy" plotterparameter
    p = Plotterparameter(prefix, data=None)
    nose.tools.assert_false(p.valid)


def test_plot_config_1():
    # test for a simple plotterparameter for a simple plotter
    p = Plotterparameter(prefix, "plot/config/1")
    nose.tools.assert_true(p.valid, "\n  * %s" % "\n  * ".join(p.errors))


def test_plot_invalid_1():
    # test for invalid parameter name
    p = Plotterparameter(prefix, "plot/invalid/1")
    nose.tools.assert_false(p.valid)
    nose.tools.assert_true(
        p.errors[0] == "'not_an_option' isn't a parameter for plotter user/scatter/1"
    )


def test_plot_invalid_2():
    # test for invalid "plotter" field
    p = Plotterparameter(prefix, "plot/invalid/2")
    nose.tools.assert_false(p.valid)
    nose.tools.assert_true(
        p.errors[0] == "Plotter declaration file not found: user/not_a_plotter/1"
    )


def test_export():
    plotterparameter_name = "plot/config/1"
    target_name = "plot/generated/1"

    obj = Plotterparameter(prefix, plotterparameter_name)
    nose.tools.assert_true(obj.valid, "\n  * %s" % "\n  * ".join(obj.errors))

    pp_storage = Storage(prefix, target_name)
    obj.write(pp_storage)

    # load from tmp_prefix and validates
    exported = Plotterparameter(prefix, target_name)
    nose.tools.assert_true(exported.valid, "\n  * %s" % "\n  * ".join(exported.errors))
