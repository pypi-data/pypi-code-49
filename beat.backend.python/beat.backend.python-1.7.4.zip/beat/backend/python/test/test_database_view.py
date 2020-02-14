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


import unittest
import tempfile
import shutil
import os

from ddt import ddt
from ddt import idata

from ..database import Database

from .test_database import INTEGERS_DBS

from . import prefix


# ----------------------------------------------------------


class MyExc(Exception):
    pass


# ----------------------------------------------------------


@ddt
class TestDatabaseViewRunner(unittest.TestCase):
    def setUp(self):
        self.cache_root = tempfile.mkdtemp(prefix=__name__)

    def tearDown(self):
        shutil.rmtree(self.cache_root)

    def test_syntax_error(self):
        db = Database(prefix, "syntax_error/1")
        self.assertTrue(db.valid)

        with self.assertRaises(SyntaxError):
            db.view("protocol", "set")

    def test_unknown_view(self):
        db = Database(prefix, "integers_db/1")
        self.assertTrue(db.valid)

        with self.assertRaises(KeyError):
            db.view("protocol", "does_not_exist")

    @idata(INTEGERS_DBS)
    def test_valid_view(self, db_name):
        db = Database(prefix, db_name)
        self.assertTrue(db.valid)

        view = db.view("double", "double")
        self.assertTrue(view is not None)

    def test_indexing_crash(self):
        db = Database(prefix, "crash/1")
        self.assertTrue(db.valid)

        view = db.view("protocol", "index_crashes", MyExc)

        with self.assertRaises(MyExc):
            view.index(os.path.join(self.cache_root, "data.db"))

    def test_get_crash(self):
        db = Database(prefix, "crash/1")
        self.assertTrue(db.valid)

        view = db.view("protocol", "get_crashes", MyExc)
        view.index(os.path.join(self.cache_root, "data.db"))
        view.setup(os.path.join(self.cache_root, "data.db"))

        with self.assertRaises(MyExc):
            view.get("a", 0)

    def test_not_setup(self):
        db = Database(prefix, "crash/1")
        self.assertTrue(db.valid)

        view = db.view("protocol", "get_crashes", MyExc)

        with self.assertRaises(MyExc):
            view.get("a", 0)

    @idata(INTEGERS_DBS)
    def test_success(self, db_name):
        db = Database(prefix, db_name)
        self.assertTrue(db.valid)

        view = db.view("double", "double", MyExc)
        view.index(os.path.join(self.cache_root, "data.db"))
        view.setup(os.path.join(self.cache_root, "data.db"))

        self.assertTrue(view.data_sources is not None)
        self.assertEqual(len(view.data_sources), 3)

        for i in range(0, 9):
            self.assertEqual(view.get("a", i)["value"], i + 1)
            self.assertEqual(view.get("b", i)["value"], (i + 1) * 10)
            self.assertEqual(view.get("sum", i)["value"], (i + 1) * 10 + i + 1)

    def test_success_using_keywords(self):
        db = Database(prefix, "python_keyword/1")
        self.assertTrue(db.valid)

        view = db.view("keyword", "keyword", MyExc)
        view.index(os.path.join(self.cache_root, "data.db"))
        view.setup(os.path.join(self.cache_root, "data.db"))

        self.assertTrue(view.data_sources is not None)
        self.assertEqual(len(view.data_sources), 3)

        for i in range(0, 9):
            self.assertEqual(view.get("class", i)["value"], i + 1)
            self.assertEqual(view.get("def", i)["value"], (i + 1) * 10)
            self.assertEqual(view.get("sum", i)["value"], (i + 1) * 10 + i + 1)
