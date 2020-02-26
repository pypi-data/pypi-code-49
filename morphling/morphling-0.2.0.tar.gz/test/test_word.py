import unittest
from morphling.word import create_word_list, create_hashtag_list, create_hashtag_list
import pickle

class TestWordList(unittest.TestCase):
    def test_be_able_to_list_of_word(self):
        create_word_list('test/input_file/word_test_csv', 'test/output_file/basic_line_list')
        with open('test/output_file/basic_line_list', 'rb') as f:
            actual = pickle.load(f)
        assert type(actual) == list

class TestHashtagList(unittest.TestCase):
    def test_be_able_to_create_list_of_hash_tag(self):
        create_hashtag_list('test/input_file/word_test_csv', 'test/output_file/basic_line_list')
        with open('test/output_file/basic_line_list', 'rb') as f:
            actual = pickle.load(f)
        assert actual == ['#common', '#HappyNewYear2019', '#test', '#HappyNewYear2019']