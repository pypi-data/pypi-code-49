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

import contextlib
import os
import sys
import unittest
from io import StringIO
from os.path import exists

from setup_scmversion import PARSERS, ScmParser, Tags, main, version


class Test(unittest.TestCase):

    def testVersion(self):
        self.assertIsNotNone(version())

    def testIsValidVersionType(self):
        self.assertTrue(ScmParser.is_valid_version_type('RELEASE'))
        self.assertFalse(ScmParser.is_valid_version_type('release'))

        self.assertTrue(ScmParser.is_valid_version_type('RELEASE_BRANCH'))
        self.assertFalse(ScmParser.is_valid_version_type('release_branch'))

    def testInvalidParser(self):
        with self.assertRaises(ValueError):
            version(scm='invalid_parser')

    def testDefaultParserIsGit(self):
        self.assertEqual(version(), version(scm='git'))

    def testBuildVersion(self):
        self.assertEqual(ScmParser.build_version('release/0.0.1', '12', None),
                         (Tags.RELEASE_BRANCH.name, '0.0.1.dev12'))
        self.assertEqual(ScmParser.build_version('release/0.0.1', '12', ''),
                         (Tags.RELEASE_BRANCH.name, '0.0.1.dev12'))
        self.assertEqual(ScmParser.build_version('feature/0.0.1', '12', None),
                         (Tags.FEATURE_BRANCH.name, '0.0.1.feature12'))
        self.assertEqual(ScmParser.build_version('feature/0.0.1', '12', ''),
                         (Tags.FEATURE_BRANCH.name, '0.0.1.feature12'))
        self.assertEqual(ScmParser.build_version('master', '12', '0.0.1'),
                         (Tags.RELEASE.name, '0.0.1'))
        self.assertEqual(ScmParser.build_version('master', '12', None),
                         (Tags.OTHER.name, 'master.dev12'))
        self.assertEqual(ScmParser.build_version('master', '12', ''),
                         (Tags.OTHER.name, 'master.dev12'))

    @unittest.skip('fails on untagged master branches')
    def testParser(self):
        self.assertTrue(ScmParser.is_valid_version(version()))

    def testAssertRaises(self):
        with self.assertRaises(AssertionError):
            with self.assertRaises(ValueError):
                print('no error')

    def testMainHelp(self):
        with self.assertRaises(SystemExit) as e:
            main(['--help'])
        self.assertEqual(e.exception.code, 0)
        with self.assertRaises(SystemExit) as e1:
            main(['-h'])
        self.assertEqual(e1.exception.code, 0)

    def testMainInvalidCommandArguments(self):
        with self.assertRaises(SystemExit) as e1:
            main()
        self.assertEqual(e1.exception.code, 2)

        with self.assertRaises(SystemExit) as e2:
            main(args=[''])
        self.assertEqual(e2.exception.code, 2)

        with self.assertRaises(SystemExit) as e3:
            main(args=['--version'])
        self.assertEqual(e3.exception.code, 2)

    def testMainValidCommandArgumentsVersion(self):
        captured = StringIO()
        sys.stdout = captured

        main(['version'])
        self.assertTrue(ScmParser.is_valid_version(captured.getvalue()))

        sys.stdout = sys.__stdout__

    def testMainValidCommandArgumentsVersionType(self):
        captured = StringIO()
        sys.stdout = captured

        main(['version-type'])
        self.assertTrue(ScmParser.is_valid_version_type(
            captured.getvalue().strip()))

        sys.stdout = sys.__stdout__

    def testMainValidCommandArgumentsParsers(self):
        captured = StringIO()
        sys.stdout = captured

        main(['parsers'])
        self.assertEqual(str(list(PARSERS.keys())),
                         captured.getvalue().strip())

        sys.stdout = sys.__stdout__

    def testMainValidCommandTagVersion(self):
        file_name = 'test/_version.py'
        with contextlib.suppress(FileNotFoundError):
            os.remove(file_name)
        self.assertFalse(os.path.exists(file_name))

        main(['tag-version', 'test'])

        self.assertTrue(os.path.exists(file_name))
        os.remove(file_name)

    def testMainValidCommandTagVersionDefaultPackageDefaultFile(self):
        file_name = 'setup_scmversion/_version.py'
        self.assertTrue(os.path.exists(file_name))
        original_creation_time = os.path.getmtime(file_name)

        main(['tag-version'])

        self.assertGreaterEqual(os.path.getmtime(file_name),
                                original_creation_time)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
