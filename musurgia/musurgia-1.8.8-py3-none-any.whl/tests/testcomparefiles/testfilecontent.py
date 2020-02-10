import os
from unittest import TestCase

from musurgia.agunittest import AGTestCase

tfc = AGTestCase()

path = str(os.path.abspath(__file__).split('.')[0])


class Test(TestCase):
    def test_1_1(self):
        with self.assertRaises(ValueError):
            wrong_path = path + '_test_1'
            tfc.assertCompareFiles(wrong_path)

    def test_1_2(self):
        actual_file_path = path + '_test_1.txt'
        tfc.assertCompareFiles(actual_file_path)

    def test_2_1(self):
        actual_file_path = path + '_test_2.txt'
        with self.assertRaises(AssertionError):
            tfc.assertCompareFiles(actual_file_path)

    def test_2_2(self):
        actual_file_path = path + '_test_2.txt'
        expected_file_path= path + '_test_1_expected.txt'
        tfc.assertCompareFiles(actual_file_path=actual_file_path, expected_file_path=expected_file_path)
