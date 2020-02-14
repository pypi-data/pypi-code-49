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
import six

from .. import hash


# ----------------------------------------------------------


def test_path_from_username():
    path = hash.toUserPath("johndoe")

    nose.tools.assert_is_not_none(path)
    nose.tools.assert_true(isinstance(path, str))
    nose.tools.assert_true(len(path) > 0)

    parts = path.split("/")

    nose.tools.eq_(len(parts), 3)

    for folder in parts[:-1]:
        nose.tools.eq_(len(folder), 2)

    nose.tools.eq_(parts[-1], "johndoe")


# ----------------------------------------------------------


def test_basic_hash():
    nose.tools.eq_(
        hash._sha256("123456"),
        "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",
    )


# ----------------------------------------------------------


def test_accented_hash():
    if six.PY2:
        ref = "4cb6985f5b4ec0ad4ce46904364f374194386426996a56683dc1c8d2944272ce"
    else:
        ref = "477993339861be6552873127471f9da6ae443991d5aced735f51140c34cd7599"

    nose.tools.eq_(hash._sha256("áéçü"), ref)


# ----------------------------------------------------------


def test_unicode_hash():
    nose.tools.eq_(
        hash._sha256(u"áéçü"),
        "477993339861be6552873127471f9da6ae443991d5aced735f51140c34cd7599",
    )


# ----------------------------------------------------------


def test_dataset_hash():

    h = hash.hashDataset("some_database/1", "some_protocol", " some_set")
    nose.tools.assert_is_not_none(h)
    nose.tools.assert_true(isinstance(h, str))
    nose.tools.assert_true(len(h) > 0)


# ----------------------------------------------------------


def test_dataset_hash_repeatability():

    h1 = hash.hashDataset("some_database/1", "some_protocol", " some_set")
    h2 = hash.hashDataset("some_database/1", "some_protocol", " some_set")
    nose.tools.eq_(h1, h2)


# ----------------------------------------------------------


def test_different_dataset_hashes():

    h1 = hash.hashDataset("some_database/1", "some_protocol", " some_set1")
    h2 = hash.hashDataset("some_database/1", "some_protocol", " some_set2")
    nose.tools.assert_not_equal(h1, h2, "%r != %r" % (h1, h2))
