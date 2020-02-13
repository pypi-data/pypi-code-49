#  
#      setup_headers - Sets a standard header in all source files
#  
#      Copyright (C) 2019 Jorge M. Faleiro Jr.
#  
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU Affero General Public License as published
#      by the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#  
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU Affero General Public License for more details.
#  
#      You should have received a copy of the GNU Affero General Public License
#      along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  
import unittest

from setup_headers import process_lines


def readlines(file_name):
    with open('test/data/' + file_name) as f:
        return [l.strip('\n') for l in f.readlines()]


class Test(unittest.TestCase):
    def testSimpleSubstituitionCommentWhitespace(self):
        comment_whitespace = '# '
        self.assertEqual(readlines('01_expected.txt'),
                          process_lines(readlines('01_header.txt'),
                                        readlines('01_file.txt'), comment_whitespace))

    def testSimpleSubstituitionComment(self):
        comment = '#'
        self.assertEqual(readlines('01_expected_1_comment.txt'),
                          process_lines(readlines('01_header.txt'),
                                        readlines('01_file.txt'), comment))

    def testSimpleSubstitutionGivesSameResult(self):
        self.assertEqual(readlines('01_expected.txt'),
                          process_lines(readlines('01_header.txt'),
                                        readlines('01_expected.txt'), '# '))

    def testSubstituitionNoEmptyLines(self):
        comment = '#'
        self.assertEqual(readlines('02_expected.txt'),
                          process_lines(readlines('02_header.txt'),
                                        readlines('02_file.txt'), comment))

    def testSubstitutionNoEmptyLinesGivesSameResult(self):
        self.assertEqual(readlines('02_expected.txt'),
                          process_lines(readlines('02_header.txt'),
                                        readlines('02_expected.txt'), '#'))
