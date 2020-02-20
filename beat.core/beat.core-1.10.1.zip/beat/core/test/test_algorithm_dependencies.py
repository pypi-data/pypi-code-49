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

from ..algorithm import Algorithm, Storage
from ..library import Library, Storage as LibraryStorage
from ..dataformat import Storage as DataFormatStorage

from . import prefix, tmp_prefix
from .utils import cleanup


def copy_objects(algorithm, library):

    alg = Algorithm(prefix, algorithm)
    storage = Storage(tmp_prefix, alg.name)
    alg.write(storage)

    for dataformat in alg.dataformats:
        storage = DataFormatStorage(tmp_prefix, dataformat)
        alg.dataformats[dataformat].write(storage)

    lib = Library(prefix, library)
    storage = LibraryStorage(tmp_prefix, lib.name)
    lib.write(storage)


@nose.tools.with_setup(teardown=cleanup)
def test_dependencies():
    name = "v1/for_dep/1"
    dep_name = "user/dep/1"

    copy_objects(name, dep_name)

    alg = Algorithm(tmp_prefix, name)
    nose.tools.assert_true(alg.valid, "\n  * %s" % "\n  * ".join(alg.errors))
    nose.tools.assert_is_none(alg.uses)
    nose.tools.eq_(len(alg.libraries), 0)

    l_dep = Library(tmp_prefix, dep_name)
    nose.tools.assert_true(l_dep.valid, "\n  * %s" % "\n  * ".join(l_dep.errors))

    # check modification
    alg.uses = {"dep1": dep_name}
    alg.write()
    alg = Algorithm(tmp_prefix, name)
    nose.tools.assert_true(alg.valid, "\n  * %s" % "\n  * ".join(alg.errors))

    nose.tools.eq_(len(alg.uses), 1)
    nose.tools.eq_(len(alg.libraries), 1)
    nose.tools.eq_(list(alg.uses.keys())[0], "dep1")
    nose.tools.eq_(list(alg.uses.values())[0], "user/dep/1")

    alg.uses = {}
    alg.uses["mod1"] = dep_name
    alg.write()
    alg = Algorithm(tmp_prefix, name)
    nose.tools.assert_true(alg.valid, "\n  * %s" % "\n  * ".join(alg.errors))

    nose.tools.eq_(len(alg.uses), 1)
    nose.tools.eq_(len(alg.libraries), 1)
    nose.tools.eq_(list(alg.uses.keys())[0], "mod1")
    nose.tools.eq_(list(alg.uses.values())[0], "user/dep/1")

    alg.uses = {}
    alg.write()
    alg = Algorithm(tmp_prefix, name)
    nose.tools.assert_true(alg.valid, "\n  * %s" % "\n  * ".join(alg.errors))

    nose.tools.eq_(len(alg.uses), 0)
    nose.tools.eq_(len(alg.libraries), 0)


@nose.tools.with_setup(teardown=cleanup)
def test_invalid_dependencies():

    name = "v1/for_dep/1"
    dep_name = "errors/invalid_dep/1"

    copy_objects(name, dep_name)

    alg = Algorithm(tmp_prefix, name)
    nose.tools.assert_true(alg.valid, "\n  * %s" % "\n  * ".join(alg.errors))
    nose.tools.assert_is_none(alg.uses)
    nose.tools.eq_(len(alg.libraries), 0)

    l_dep = Library(tmp_prefix, "errors/invalid_dep/1")
    nose.tools.assert_true(l_dep.valid, "\n  * %s" % "\n  * ".join(l_dep.errors))

    alg.uses = {"dep": dep_name}
    alg.write()
    alg = Algorithm(tmp_prefix, name)
    nose.tools.assert_false(alg.valid)
    nose.tools.assert_not_equal(alg.errors[0].find("differs from current language"), -1)


@nose.tools.with_setup(teardown=cleanup)
def test_invalid_dependency_setup():
    name = "v1/for_dep/1"
    dep_name = "user/dep/1"

    copy_objects(name, dep_name)

    alg = Algorithm(tmp_prefix, name)
    nose.tools.assert_true(alg.valid, "\n  * %s" % "\n  * ".join(alg.errors))
    nose.tools.assert_is_none(alg.uses)
    with nose.tools.assert_raises(RuntimeError):
        alg.uses = "dummy"
