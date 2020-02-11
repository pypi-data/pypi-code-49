import unittest
import os

from matchup.presentation.Sanitizer import Sanitizer
from matchup.presentation.Text import Line, Term


class SanitizerTest(unittest.TestCase):
    def setUp(self):
        self._sanitizer = Sanitizer(stopwords_path=os.path.abspath("tests/static/pt-br.txt"))

    def test_import_stopwords(self):
        response = self._sanitizer.import_stopwords()

        self.assertTrue(response)
        self.assertTrue('quando' in response)

    def test_remove_special_chars(self):
        test_case = '^`}!@#!@#!$%$$a%&%¨*&(*&*¨¨%$$)_^{`:?|/'
        test_response = 'a'

        self.assertEqual(self._sanitizer._remove_special_chars_lower(test_case), test_response)

    def test_remove_accents(self):
        test_case = 'áéíóúàèìòùâêîôûÃ'
        test_response = 'aeiouaeiouaeiouA'

        self.assertEqual(self._sanitizer.strip_accents(test_case), test_response)

    def test_index_line(self):
        line = Line("eu sou o marcos e existem stopwords em tudo", 1)
        line_list = ['marcos', 'existem', 'stopwords', 'tudo']
        response_terms = [Term('marcos', '1-9'), Term('existem', '1-18'),
                          Term('stopwords', '1-26'), Term('tudo', '1-39')]

        self.assertEqual(self._sanitizer.index_line(line_list, line), response_terms)

    def test_sanitize_line(self):
        line = "eu sòu o mãrcos e existem stôpwords em túdo"
        response_terms = [Term('marcos', '1-9'), Term('existem', '1-18'),
                          Term('stopwords', '1-26'), Term('tudo', '1-39')]
        self.assertEqual(self._sanitizer.sanitize_line(line, 1), response_terms)





