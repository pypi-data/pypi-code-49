import unittest
from morphling.input import Reader
from morphling.copy import Copy


class TestImportData(unittest.TestCase):
    def test_be_able_to_import_data_from_file(self):
        obj = Reader()
        actual = obj.read('test/input_file/basic_line')
        with open('test/input_file/basic_line', 'r') as reader:
            expect = reader.read()
        self.assertEqual(actual, expect)