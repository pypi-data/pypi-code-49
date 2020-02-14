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


# Tests for experiment execution

import os

import unittest
import multiprocessing
import tempfile
import shutil

from ddt import ddt
from ddt import idata

from ..scripts import index
from ..hash import hashDataset
from ..hash import toPath

from .test_database import INTEGERS_DBS

from . import prefix


# ----------------------------------------------------------


class IndexationProcess(multiprocessing.Process):
    def __init__(self, queue, arguments):
        super(IndexationProcess, self).__init__()

        self.queue = queue
        self.arguments = arguments

    def run(self):
        self.queue.put("STARTED")
        index.main(self.arguments)


# ----------------------------------------------------------


@ddt
class TestDatabaseIndexation(unittest.TestCase):
    def __init__(self, methodName="runTest"):
        super(TestDatabaseIndexation, self).__init__(methodName)
        self.databases_indexation_process = None
        self.working_dir = None
        self.cache_root = None

    def setUp(self):
        self.shutdown_everything()  # In case another test failed badly during its setUp()
        self.working_dir = tempfile.mkdtemp(prefix=__name__)
        self.cache_root = tempfile.mkdtemp(prefix=__name__)

    def tearDown(self):
        self.shutdown_everything()

        shutil.rmtree(self.working_dir)
        shutil.rmtree(self.cache_root)

        self.working_dir = None
        self.cache_root = None
        self.data_source = None

    def shutdown_everything(self):
        if self.databases_indexation_process is not None:
            self.databases_indexation_process.terminate()
            self.databases_indexation_process.join()
            del self.databases_indexation_process
            self.databases_indexation_process = None

    def process(self, database, protocol_name=None, set_name=None):
        args = [prefix, self.cache_root, database]

        if protocol_name is not None:
            args.append(protocol_name)

            if set_name is not None:
                args.append(set_name)

        self.databases_indexation_process = IndexationProcess(
            multiprocessing.Queue(), args
        )
        self.databases_indexation_process.start()

        self.databases_indexation_process.queue.get()

        self.databases_indexation_process.join()
        del self.databases_indexation_process
        self.databases_indexation_process = None

    @idata(INTEGERS_DBS)
    def test_one_set(self, db_name):
        self.process(db_name, "double", "double")

        expected_files = [hashDataset(db_name, "double", "double")]
        print(expected_files)
        for filename in expected_files:
            self.assertTrue(
                os.path.exists(
                    os.path.join(self.cache_root, toPath(filename, suffix=".db"))
                )
            )

    @idata(INTEGERS_DBS)
    def test_one_protocol(self, db_name):
        self.process(db_name, "two_sets")

        expected_files = [
            hashDataset(db_name, "two_sets", "double"),
            hashDataset(db_name, "two_sets", "triple"),
        ]

        for filename in expected_files:
            self.assertTrue(
                os.path.exists(
                    os.path.join(self.cache_root, toPath(filename, suffix=".db"))
                )
            )

    @idata(INTEGERS_DBS)
    def test_whole_database(self, db_name):
        self.process(db_name)

        expected_files = [
            hashDataset(db_name, "double", "double"),
            hashDataset(db_name, "triple", "triple"),
            hashDataset(db_name, "two_sets", "double"),
            hashDataset(db_name, "two_sets", "triple"),
            hashDataset(db_name, "labelled", "labelled"),
            hashDataset(db_name, "different_frequencies", "double"),
        ]

        for filename in expected_files:
            self.assertTrue(
                os.path.exists(
                    os.path.join(self.cache_root, toPath(filename, suffix=".db"))
                )
            )

    def test_error(self):
        self.process("crash/1", "protocol", "index_crashes")

        unexpected_files = [hashDataset("crash/1", "protocol", "index_crashes")]

        for filename in unexpected_files:
            self.assertFalse(
                os.path.exists(
                    os.path.join(self.cache_root, toPath(filename, suffix=".db"))
                )
            )
