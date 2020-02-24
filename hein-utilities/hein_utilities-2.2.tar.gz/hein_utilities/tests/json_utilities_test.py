import os
import unittest
from hein_utilities import json_utilities


def delete_json(json_file_path):
    os.remove(path=json_file_path)


class JsonUtilitiesFunctions(unittest.TestCase):

    def setUp(self):
        print('setUp json utilities functions testing')

    def test_create_json_file_with_json_type_in_path(self):
        path = json_utilities.create_json_file('test')
        file_was_created_at_path = os.path.isfile(path)

        self.assertTrue(file_was_created_at_path)

        delete_json(json_file_path=path)

    def test_create_json_file_without_json_type_in_path(self):
        path = json_utilities.create_json_file('test')
        file_was_created_at_path = os.path.isfile(path)

        self.assertTrue(file_was_created_at_path)

        delete_json(json_file_path=path)

    def test_add_new_string_value(self):
        path = json_utilities.create_json_file('test')

        actual_data = {'a': 0}
        json_utilities.update_json_file(json_file_path=path, data_to_update_with=actual_data)

        read_json_data = json_utilities.load_json_file(json_file_path=path)
        self.assertEqual(actual_data, read_json_data)

        delete_json(json_file_path=path)

    def test_add_new_dictionary_value(self):
        path = json_utilities.create_json_file('test')

        actual_data = {'a': {'b': 1}}
        json_utilities.update_json_file(json_file_path=path, data_to_update_with=actual_data)

        read_json_data = json_utilities.load_json_file(json_file_path=path)
        self.assertEqual(actual_data, read_json_data)

        delete_json(json_file_path=path)

    def test_add_additional_dictionary_value(self):
        path = json_utilities.create_json_file('test')

        initial_data = {'a': {'b': 1}}
        json_utilities.update_json_file(json_file_path=path, data_to_update_with=initial_data)

        additional_data = {'a': {'c': 2}}
        json_utilities.update_json_file(json_file_path=path, data_to_update_with=additional_data)

        true_result = {'a': {'b': 1, 'c': 2}}

        read_json_data = json_utilities.load_json_file(json_file_path=path)
        self.assertEqual(true_result, read_json_data)

        delete_json(json_file_path=path)

    def test_add_new_list_value(self):
        path = json_utilities.create_json_file('test')

        actual_data = {'a': [1]}
        json_utilities.update_json_file(json_file_path=path, data_to_update_with=actual_data)

        read_json_data = json_utilities.load_json_file(json_file_path=path)
        self.assertEqual(actual_data, read_json_data)

        delete_json(json_file_path=path)

    def test_add_additional_list_value(self):
        path = json_utilities.create_json_file('test')

        initial_data = {'a': [1]}
        json_utilities.update_json_file(json_file_path=path, data_to_update_with=initial_data)

        additional_data = {'a': [2]}
        json_utilities.update_json_file(json_file_path=path, data_to_update_with=additional_data)

        true_result = {'a': [1, 2]}

        read_json_data = json_utilities.load_json_file(json_file_path=path)
        self.assertEqual(true_result, read_json_data)

        delete_json(json_file_path=path)


if __name__ == '__main__':
    unittest.main()
