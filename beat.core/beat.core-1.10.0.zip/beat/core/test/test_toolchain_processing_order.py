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


def test_integers_addition_1():

    toolchain = Toolchain(prefix, "user/integers_addition/1")
    nose.tools.assert_true(toolchain.valid)

    order = toolchain.execution_order()
    nose.tools.eq_(list(order.keys()), ["addition", "analysis"])
    nose.tools.eq_(order["addition"], set())
    nose.tools.eq_(order["analysis"], set(["addition"]))


def test_integers_addition_2():

    toolchain = Toolchain(prefix, "user/integers_addition/2")
    nose.tools.assert_true(toolchain.valid)

    order = toolchain.execution_order()
    nose.tools.eq_(list(order.keys()), ["addition1", "addition2", "analysis"])
    nose.tools.eq_(order["addition1"], set())
    nose.tools.eq_(order["addition2"], set(["addition1"]))
    nose.tools.eq_(order["analysis"], set(["addition2"]))


def test_integers_addition_3():

    toolchain = Toolchain(prefix, "user/integers_addition/3")
    nose.tools.assert_true(toolchain.valid)

    order = toolchain.execution_order()
    nose.tools.eq_(
        list(order.keys()), ["addition1", "addition2", "addition3", "analysis"]
    )
    nose.tools.eq_(order["addition1"], set())
    nose.tools.eq_(order["addition2"], set())
    nose.tools.eq_(order["addition3"], set(["addition1", "addition2"]))
    nose.tools.eq_(order["analysis"], set(["addition3"]))
