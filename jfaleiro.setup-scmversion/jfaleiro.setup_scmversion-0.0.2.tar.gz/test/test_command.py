#
#  setup_scmversion - Builds a pythonic version number sbased on scm tags and branches.
#
#  Copyright (C) 2019 Jorge M. Faleiro Jr.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import sys
import unittest
from io import StringIO
from os.path import exists

from setuptools import setup

from setup_scmversion import (PARSERS, ScmParser, Tags, main, execute_command,
                              version)
from setup_scmversion.command import TagVersionCommand, tag_version


class TestCommand(unittest.TestCase):

    def setUp(self):
        self.file_name = 'setup_scmversion/_version.py'
        self.assertTrue(os.path.isfile(self.file_name))
        self.original_creation_time = os.path.getmtime(self.file_name)

    def tearDown(self):
        self.last_creation_time = os.path.getmtime(self.file_name)
        self.assertGreaterEqual(self.last_creation_time,
                                self.original_creation_time)

    def testTagsVersion(self):
        pass  # best way to test setuptools commands?
