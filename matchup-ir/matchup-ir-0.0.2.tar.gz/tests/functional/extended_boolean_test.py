import unittest
import os

from matchup.structure.Solution import Result
from matchup.structure.Vocabulary import Vocabulary
from matchup.structure.Query import Query
from matchup.models.Model import ModelType
from matchup.structure.weighting.Tf import TermFrequency
from matchup.structure.weighting.Idf import InverseFrequency


class ExtendedBooleanTest(unittest.TestCase):
    def setUp(self):
        self._vocabulary = Vocabulary(settings_path=os.path.abspath("tests/static"),
                                      processed_path=os.path.abspath("tests/static/files"))
        self._vocabulary.import_vocabulary()
        self._query = Query(vocabulary=self._vocabulary)

    def test_search_known_response(self):
        self._query.ask(answer="artilheiro brasil 1994 gols")
        response = self._query.search(model=ModelType.ExtendedBoolean, idf=InverseFrequency(), tf=TermFrequency(),
                                      P=3.0)

        some_expected_results = [Result(os.path.abspath("tests/static/files/d1.txt"), 0.564),
                                 Result(os.path.abspath("tests/static/files/d3.txt"), 0.180),
                                 Result(os.path.abspath("tests/static/files/d15.txt"), 0.308),
                                 Result(os.path.abspath("tests/static/files/d11.txt"), 0.179)]

        for expected in some_expected_results:
            self.assertTrue(expected in response)
