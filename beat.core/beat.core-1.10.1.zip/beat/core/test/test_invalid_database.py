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

import logging

logger = logging.getLogger(__name__)


def doit(filename, error_msg):
    database = Database(prefix, filename)
    nose.tools.assert_true(database.errors)
    logger.error(error_msg)
    found = False

    for msg in database.errors:
        logger.error("%s %s", msg, error_msg)
        if msg.find(error_msg) != -1:
            found = True
            break

    nose.tools.assert_true(
        found,
        (
            "cannot find message `%s' on error list (%s) from loading database file `%s'"
            % (error_msg, database.errors, filename)
        ),
    )


def test_load_unknown_database():
    doit("unknown/1", "file not found")


def test_load_invalid_database():
    doit("invalid/1", "invalid JSON code")


def test_load_database_without_protocols_list():
    doit("missing_protocols/1", "%r is a required property" % u"protocols")


def test_load_database_with_empty_protocols_list():
    doit("empty_protocols/1", "/protocols: [] is too short")


def test_load_database_with_missing_protocol_name():
    doit("missing_protocol_name/1", "/protocols/0: %r is a required property" % u"name")


def test_load_database_with_mixed_protocol_names():
    doit("mixed_protocol_names/1", "None is not of type %r" % u"string")


def test_load_database_with_same_protocol_names():
    doit("same_protocol_names/1", "found different protocols with the same name:")


def test_load_database_with_missing_protocol_sets():
    doit("missing_protocol_sets/1", "%r is a required property" % u"sets")


def test_load_database_with_empty_protocol_sets():
    doit(
        "empty_protocol_sets/1",
        "rule: /properties/protocols/items/properties/sets/minItems",
    )


def test_load_database_with_missing_set_name():
    doit("missing_set_name/1", "%r is a required property" % u"name")


def test_load_database_with_mixed_set_names():
    doit("mixed_set_names/1", "name: None is not of type %r" % u"string")


def test_load_database_with_same_set_names():
    doit("same_set_names/1", "found different sets with the same name")


def test_load_database_with_missing_set_view():
    doit("missing_set_view/1", "%r is a required property" % u"view")


def test_load_database_with_missing_set_outputs_list():
    doit("missing_set_outputs/1", "%r is a required property" % u"outputs")


def test_load_database_with_empty_set_outputs_list():
    doit(
        "empty_set_outputs/1", "outputs: OrderedDict() does not have enough properties"
    )
