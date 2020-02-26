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


import sys
import types

import nose.tools

from . import prefix, tmp_prefix
from .utils import cleanup
from ..library import Library, Storage


def test_valid():

    lib = Library(prefix, "user/valid/1")
    nose.tools.assert_true(lib.valid, "\n  * %s" % "\n  * ".join(lib.errors))
    nose.tools.eq_(len(lib.uses), 0)
    nose.tools.eq_(len(lib.libraries), 0)

    # tries to call the function `f()' on that library
    module = lib.load()
    nose.tools.assert_true(isinstance(module, types.ModuleType))
    nose.tools.eq_(module.f(), "OK")
    nose.tools.eq_(module.pyver(), "%d.%d" % sys.version_info[:2])


def test_nested_1():

    lib = Library(prefix, "user/nest1/1")
    nose.tools.assert_true(lib.valid, "\n  * %s" % "\n  * ".join(lib.errors))
    nose.tools.eq_(len(lib.uses), 1)
    nose.tools.eq_(len(lib.libraries), 1)

    # tries to call the function `f()' on that library
    module = lib.load()
    nose.tools.assert_true(isinstance(module, types.ModuleType))
    nose.tools.eq_(module.f("-extra"), "OK-extra")
    nose.tools.eq_(module.pyver("-extra"), "%d.%d-extra" % sys.version_info[:2])


def test_nested_2():

    lib = Library(prefix, "user/nest2/1")
    nose.tools.assert_true(lib.valid, "\n  * %s" % "\n  * ".join(lib.errors))
    nose.tools.eq_(len(lib.uses), 1)
    nose.tools.eq_(len(lib.libraries), 1)

    # tries to call the function `f()' on that library
    module = lib.load()
    nose.tools.assert_true(isinstance(module, types.ModuleType))
    nose.tools.eq_(module.f("-x"), "OK-x-x")
    nose.tools.eq_(module.pyver("-x"), "%d.%d-x-x" % sys.version_info[:2])


def test_direct_recursion():

    lib = Library(prefix, "user/direct_recursion/1")
    nose.tools.assert_false(lib.valid)

    nose.tools.eq_(len(lib.errors), 1)
    nose.tools.assert_not_equal(lib.errors[0].find("recursion for library"), -1)
    nose.tools.assert_not_equal(lib.errors[0].find(lib.name), -1)


def test_indirect_recursion():

    lib = Library(prefix, "user/indirect_recursion/1")
    nose.tools.assert_false(lib.valid)
    nose.tools.eq_(len(lib.errors), 1)
    nose.tools.assert_not_equal(lib.errors[0].find("referred library"), -1)
    nose.tools.assert_not_equal(
        lib.errors[0].find("user/indirect_recursion_next/1"), -1
    )


def test_invalid_mix():

    lib = Library(prefix, "errors/invalid_mix/1")
    nose.tools.assert_false(lib.valid)
    nose.tools.eq_(len(lib.errors), 1)
    nose.tools.assert_not_equal(lib.errors[0].find("differs from current language"), -1)


def test_duplicate_key():

    lib = Library(prefix, "errors/duplicate_key/1")
    nose.tools.assert_false(lib.valid)
    nose.tools.eq_(len(lib.errors), 1)
    nose.tools.assert_not_equal(lib.errors[0].find("found several times"), -1)


@nose.tools.with_setup(teardown=cleanup)
def test_dependencies():

    name = "user/for_dep/1"
    dep_name = "user/dep/1"

    lib = Library(prefix, name)
    nose.tools.assert_true(lib.valid, "\n  * %s" % "\n  * ".join(lib.errors))
    nose.tools.eq_(len(lib.uses), 0)
    nose.tools.eq_(len(lib.libraries), 0)

    # Save to temporary storage, so we can test modifications on it
    new_storage = Storage(tmp_prefix, name)
    lib.write(new_storage)

    l_dep = Library(prefix, dep_name)
    nose.tools.assert_true(l_dep.valid)
    new_dep_storage = Storage(tmp_prefix, dep_name)
    l_dep.write(new_dep_storage)

    # Reload
    lib = Library(tmp_prefix, name)
    nose.tools.assert_true(lib.valid, "\n  * %s" % "\n  * ".join(lib.errors))
    l_dep = Library(tmp_prefix, dep_name)
    nose.tools.assert_true(l_dep.valid)

    lib.uses["dep1"] = l_dep.name
    lib.write()  # rewrite

    # Re-validate
    lib = Library(tmp_prefix, name)
    nose.tools.assert_true(lib.valid, "\n  * %s" % "\n  * ".join(lib.errors))

    nose.tools.eq_(len(lib.uses), 1)
    nose.tools.eq_(len(lib.libraries), 1)
    nose.tools.eq_(list(lib.uses.keys())[0], "dep1")
    nose.tools.eq_(list(lib.uses.values())[0], "user/dep/1")

    lib.uses = {}  # reset
    lib.uses["mod1"] = l_dep.name
    lib.write()  # rewrite

    # Re-validate
    lib = Library(tmp_prefix, name)
    nose.tools.assert_true(lib.valid, "\n  * %s" % "\n  * ".join(lib.errors))

    nose.tools.eq_(len(lib.uses), 1)
    nose.tools.eq_(len(lib.libraries), 1)
    nose.tools.eq_(list(lib.uses.keys())[0], "mod1")
    nose.tools.eq_(list(lib.uses.values())[0], "user/dep/1")

    lib.uses = {}  # reset
    lib.write()  # rewrite

    # Re-validate
    lib = Library(tmp_prefix, name)
    nose.tools.assert_true(lib.valid, "\n  * %s" % "\n  * ".join(lib.errors))

    nose.tools.eq_(len(lib.uses), 0)
    nose.tools.eq_(len(lib.libraries), 0)


@nose.tools.with_setup(teardown=cleanup)
def test_adding_self():
    name = "user/for_dep/1"

    lib = Library(prefix, name)
    nose.tools.assert_true(lib.valid, "\n  * %s" % "\n  * ".join(lib.errors))
    nose.tools.eq_(len(lib.uses), 0)
    nose.tools.eq_(len(lib.libraries), 0)

    lib.uses["dep"] = lib.name
    new_storage = Storage(tmp_prefix, name)
    lib.write(new_storage)  # rewrite

    # Re-validate
    lib = Library(tmp_prefix, name)
    nose.tools.assert_false(lib.valid)
    nose.tools.assert_not_equal(lib.errors[0].find("recursion"), -1)


@nose.tools.with_setup(teardown=cleanup)
def test_invalid_dependencies():

    name = "user/for_dep/1"
    dep_name = "errors/invalid_dep/1"

    lib = Library(prefix, name)
    nose.tools.assert_true(lib.valid, "\n  * %s" % "\n  * ".join(lib.errors))
    nose.tools.eq_(len(lib.uses), 0)
    nose.tools.eq_(len(lib.libraries), 0)

    # Save to temporary storage, so we can test modifications on it
    new_storage = Storage(tmp_prefix, name)
    lib.write(new_storage)

    l_dep = Library(prefix, dep_name)
    nose.tools.assert_true(l_dep.valid)
    new_dep_storage = Storage(tmp_prefix, dep_name)
    l_dep.write(new_dep_storage)

    # Reload
    lib = Library(tmp_prefix, name)
    nose.tools.assert_true(lib.valid, "\n  * %s" % "\n  * ".join(lib.errors))
    l_dep = Library(tmp_prefix, dep_name)
    nose.tools.assert_true(l_dep.valid)

    lib.uses["dep1"] = l_dep.name
    lib.write()  # rewrite

    # Re-validate
    lib = Library(tmp_prefix, name)
    nose.tools.assert_false(lib.valid)
    nose.tools.assert_not_equal(lib.errors[0].find("differs from current language"), -1)


@nose.tools.with_setup(teardown=cleanup)
def test_export():

    name = "user/nest2/1"
    obj = Library(prefix, name)
    nose.tools.assert_true(obj.valid, "\n  * %s" % "\n  * ".join(obj.errors))

    obj.export(tmp_prefix)

    # load from tmp_prefix and validates
    exported = Library(tmp_prefix, name)
    nose.tools.assert_true(exported.valid, "\n  * %s" % "\n  * ".join(exported.errors))
