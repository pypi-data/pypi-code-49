import unittest

from morphling.output import Writer


class TestWriter(unittest.TestCase):
    def test_be_able_to_write_file(self):
        actual = 'test data'
        output_path = 'test/output_file/basic_write'
        obj = Writer()
        obj.write(actual, output_path)
        obj.write(actual, output_path)
        with open(output_path, 'r') as reader:
            expect = reader.read()
        self.assertEqual(actual, expect)

    def test_be_able_to_append_data_into_existing_file(self):
        actual = 'test data'
        output_path = 'test/output_file/basic_write'
        obj = Writer()
        obj.write(actual, output_path)
        obj.append(actual, output_path)
        with open(output_path, 'r') as reader:
            expect = reader.read()
        self.assertEqual(actual + actual, expect)

    def test_be_able_to_write_csv_file(self):
        data = [['name', 'age', 'color'], ['John hopskin', 15, 'Blue sky']]
        output_path = 'test/output_file/test_write_csv.csv'
        obj = Writer()
        obj.to_csv(data, output_path)
        with open(output_path, 'r') as reader:
            expect = reader.read()
        self.assertEqual('name,age,color\nJohn hopskin,15,Blue sky\n', expect)

    def test_be_able_to_write_csv_when_there_is_new_line_beween_data(self):
        data = [['name', 'age', 'color'], ['John\nhopskin', 15, 'Blue sky']]
        output_path = 'test/output_file/test_write_csv_new_line.csv'
        obj = Writer()
        obj.to_csv(data, output_path)
        with open(output_path, 'r') as reader:
            expect = reader.read()
        self.assertEqual('name,age,color\n"John\nhopskin",15,Blue sky\n', expect)

    def test_be_able_to_write_csv_when_there_is_comma_between_data(self):
        data = [['name', 'age', 'color'], ['John, hopskin', 15, 'Blue, sky']]
        output_path = 'test/output_file/test_write_csv_comma.csv'
        obj = Writer()
        obj.to_csv(data, output_path)
        with open(output_path, 'r') as reader:
            expect = reader.read()
        self.assertEqual('name,age,color\n"John, hopskin",15,"Blue, sky"\n', expect)
