import unittest
import os

from matchup.presentation.Text import Term
from matchup.structure.Query import Query
from matchup.structure.Vocabulary import Vocabulary


class QueryTest(unittest.TestCase):
    def setUp(self):
        vocabulary = Vocabulary(settings_path=os.path.abspath("tests/static"),
                                processed_path=os.path.abspath("tests/static/files"))
        vocabulary.import_vocabulary()

        self._query = Query(vocabulary=vocabulary)

    def test_ask(self):
        answer = 'eu sou o marcos\ntop de linha'
        processed = [Term("marcos", "1-9"), Term("top", "2-0"), Term("linha", "2-7")]

        self._query.ask(answer=answer)
        self.assertEqual(self._query.search_input, processed)
