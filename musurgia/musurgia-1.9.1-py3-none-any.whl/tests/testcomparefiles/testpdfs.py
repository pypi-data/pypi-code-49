import os
from unittest import TestCase

from musurgia.agunittest import AGTestCase

tfc = AGTestCase()
path = str(os.path.abspath(__file__).split('.')[0])


class Test(TestCase):
    def test_1(self):
        actual_file_path = path + '_a1.pdf'
        expected_file_path = path + '_a2.pdf'
        tfc.assertCompareFiles(actual_file_path, expected_file_path)

    def test_2(self):
        with self.assertRaises(AssertionError):
            actual_file_path = path + '_a1.pdf'
            expected_file_path = path + '_b.pdf'
            tfc.assertCompareFiles(actual_file_path, expected_file_path)
