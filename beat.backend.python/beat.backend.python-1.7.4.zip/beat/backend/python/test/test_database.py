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
from ..database import Database

from . import prefix


INTEGERS_DBS = ["integers_db/{}".format(i) for i in range(1, 3)]


# ----------------------------------------------------------


def load(database_name):

    database = Database(prefix, database_name)
    nose.tools.assert_true(database.valid, "\n  * %s" % "\n  * ".join(database.errors))
    return database


# ----------------------------------------------------------


def test_load_valid_database():

    for db_name in INTEGERS_DBS:
        yield load_valid_database, db_name


def load_valid_database(db_name):
    database = load(db_name)
    nose.tools.eq_(len(database.sets("double")), 1)
    nose.tools.eq_(len(database.sets("triple")), 1)
    nose.tools.eq_(len(database.sets("two_sets")), 2)


# ----------------------------------------------------------


def test_load_protocol_with_one_set():

    for db_name in INTEGERS_DBS:
        yield load_valid_database, db_name


def load_protocol_with_one_set(db_name):

    database = load(db_name)

    protocol = database.protocol("double")
    nose.tools.eq_(len(protocol["sets"]), 1)

    set_ = database.set("double", "double")

    nose.tools.eq_(set_["name"], "double")
    nose.tools.eq_(len(set_["outputs"]), 3)

    nose.tools.assert_is_not_none(set_["outputs"]["a"])
    nose.tools.assert_is_not_none(set_["outputs"]["b"])
    nose.tools.assert_is_not_none(set_["outputs"]["sum"])


# ----------------------------------------------------------


def test_load_protocol_with_two_sets():

    for db_name in INTEGERS_DBS:
        yield load_valid_database, db_name


def load_protocol_with_two_sets(db_name):

    database = load(db_name)

    protocol = database.protocol("two_sets")
    nose.tools.eq_(len(protocol["sets"]), 2)

    set_ = database.set("two_sets", "double")

    nose.tools.eq_(set["name"], "double")
    nose.tools.eq_(len(set["outputs"]), 3)

    nose.tools.assert_is_not_none(set_["outputs"]["a"])
    nose.tools.assert_is_not_none(set_["outputs"]["b"])
    nose.tools.assert_is_not_none(set_["outputs"]["sum"])

    set_ = database.set("two_sets", "triple")

    nose.tools.eq_(set_["name"], "triple")
    nose.tools.eq_(len(set_["outputs"]), 4)

    nose.tools.assert_is_not_none(set_["outputs"]["a"])
    nose.tools.assert_is_not_none(set_["outputs"]["b"])
    nose.tools.assert_is_not_none(set_["outputs"]["c"])
    nose.tools.assert_is_not_none(set_["outputs"]["sum"])


# ----------------------------------------------------------


def test_view_definitions():
    yield compare_definitions, "integers_db", "double", "double"
    yield compare_definitions, "with_parameters", "test_with_parameters", "double"
    yield compare_definitions, "with_parameters", "test_with_empty_parameters", "double"


def compare_definitions(db_name, protocol_name, view_name):

    db_1 = load("{}/1".format(db_name))
    db_1_view_definition = db_1.view_definition(protocol_name, view_name)
    db_1_view_definition.pop("template")  # Unused property

    db_2 = load("{}/2".format(db_name))
    db_2_view_definition = db_2.view_definition(protocol_name, view_name)

    db_1_sorted = sorted(db_1_view_definition)
    db_2_sorted = sorted(db_2_view_definition)
    nose.tools.eq_(db_1_sorted, db_2_sorted)


# ----------------------------------------------------------


def test_duplicate_key_error():
    database = Database(prefix, "duplicate_key_error/1")
    nose.tools.assert_false(database.valid)
    nose.tools.assert_true("Database declaration file invalid" in database.errors[0])
