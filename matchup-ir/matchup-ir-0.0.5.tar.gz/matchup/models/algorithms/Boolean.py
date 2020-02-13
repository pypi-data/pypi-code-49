"""
    Classic IR model. Boolean model are implemented here, based in Interface Model
"""

from collections import defaultdict
from typing import DefaultDict

from matchup.models.Model import Model, List, Term, Vocabulary
from matchup.structure.Solution import Result


class Boolean(Model):

    @staticmethod
    def run(query: List[Term], vocabulary: Vocabulary) -> List[Result]:
        """
            Principal method that represents IR boolean model.
        :param query: list of all query terms
        :param vocabulary: data structure that represents the vocabulary
        :return: list of solution -> (document, score)
        """
        # dicionário {documento : [array de presença dos termos da consulta]}
        scores = Boolean.__map_keywords_in_documents(query, vocabulary)

        maximum_pontuation = len(query)

        rank = defaultdict(float)

        for key in scores.keys():
            rank[key] = sum(scores[key]) / maximum_pontuation   # Ponderando os 'acertos' de forma simples

        # ordena pelos valores
        rank = sorted(rank.items(), key=lambda v: v[1], reverse=True)

        return Model.cast_solution(rank)

    @staticmethod
    def __map_keywords_in_documents(query: List[Term], vocabulary: Vocabulary) -> DefaultDict[str, list]:
        """
            Given the query and the vocabulary, this function calculates the scores of all words in vocabulary.
        :param query: list of all query terms
        :param vocabulary: data structure that represents the vocabulary
        :return: scores based in document
        """
        scores = defaultdict(list)

        for doc in vocabulary.file_names:
            scores[doc] = []

        for term in query:
            if term.word in vocabulary:
                matched_docs = [occurrence.doc() for occurrence in vocabulary[term.word]]
                for one_doc in matched_docs:
                    scores[one_doc].append(1)
        return scores

