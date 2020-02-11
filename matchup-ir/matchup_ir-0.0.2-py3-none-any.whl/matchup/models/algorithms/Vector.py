"""
    Classic IR model. Vectorial model are implemented here, based in Interface Model
"""
from math import sqrt

from collections import defaultdict
from typing import List, DefaultDict

from matchup.models.Model import IterModel, Term, Vocabulary
from matchup.structure.Solution import Result


class Vector(IterModel):

    @staticmethod
    def run(query: List[Term], vocabulary: Vocabulary) -> List[Result]:
        """
           Principal method that represents IR vectorial model.
        :param query: list of all query terms
        :param vocabulary: data structure that represents the vocabulary
        :return: list of solution -> (document, score)
        """
        idfs = vocabulary.idf

        query_repr = Vector.process_query(query, idfs)  # processa a consulta : gera o vetor da consulta

        IterModel.initialize_occurrences(query, vocabulary)
        IterModel.initialize_pointers()

        IterModel._term_occurrences = Vector.process_documents(query, vocabulary)

        scores = defaultdict(float)

        while not Vector.stop():

            doc = IterModel.lowest_doc()
            doc_repr = Vector.process_doc(doc)

            scores[doc] = Vector.generate_scores(doc_repr, query_repr)

        scores = sorted(scores.items(), key=lambda v: v[1], reverse=True)
        return IterModel.cast_solution(scores)

    @staticmethod
    def process_query(query: List[Term], idfs) -> DefaultDict[str, float]:
        """
            Construct query representation
        :param query: list of all terms
        :param idfs: structure IDF
        :return: query representation
        """
        query_repr = defaultdict(float)
        for key in query:
            query_repr[key.word] = idfs[key.word]
        return query_repr

    @staticmethod
    def process_doc(chosen_doc: str) -> DefaultDict[str, float]:
        """
            Proccess doc generating it score
        :param chosen_doc: Str represents the lowest document
        :return: doc repr. Dictionary with all term scores by doc. That is the document vector.
        """
        doc_repr = defaultdict(float)
        for key in IterModel._term_occurrences.keys():
            try:
                occ = IterModel._term_occurrences[key][IterModel._pointers[key]]
                if occ.doc() == chosen_doc:
                    IterModel._pointers[key] += 1
                    doc_repr[key] = occ.score
            except ValueError:
                continue
            except IndexError:
                continue
        return doc_repr

    @staticmethod
    def generate_scores(doc_repr: DefaultDict[str, float], query_repr: DefaultDict[str, float]) -> float:
        """
            Calculate the similarity between one doc and one query by its representations
        :param doc_repr: doc repr
        :param query_repr: query repr
        :return: similarity
        """
        norm_query = 0
        norm_doc = 0
        intern_product = 0

        for key in query_repr.keys():
            intern_product += (doc_repr[key] * query_repr[key])
            norm_doc += doc_repr[key] ** 2
            norm_query += query_repr[key] ** 2

        norm_query = sqrt(norm_query)
        norm_doc = sqrt(norm_doc)

        if norm_doc and norm_query:
            return intern_product / (norm_doc * norm_query)
        else:
            return 0.0

    @staticmethod
    def stop() -> bool:
        """
            Given a dictionary with all pointers by keyword and another dictionary with all occurrences by keyword,
            this function calculate if the algortihm is over
        :return: boolean flag indicates if algorithm stops
        """
        for key in IterModel._pointers.keys():

            # print("key : {0}, pointer : {1}, occurrences : {2}".format(key, IterModel._pointers[key],
            #                                                            IterModel._term_occurrences[key]))
            if IterModel._pointers[key] < len(IterModel._term_occurrences[key]):
                # print("========================================================")
                return False
        # print("========================================================")
        return True

    @staticmethod
    def process_documents(query: List[Term], vocabulary: Vocabulary) -> DefaultDict[str, list]:
        """
            Generate document scores based in query
        :param query: query representation
        :param vocabulary: vocabulary structure
        :return: List of occurrences
        """
        target = defaultdict(list)

        idf = vocabulary.idf
        tf = vocabulary.tf

        for key in query:
            if key.word in vocabulary:
                occurrences = vocabulary[key.word]
                for occurrence in occurrences:
                    score = idf[key.word] * tf.calculate(key.word, occurrence, vocabulary)  # occurrence.frequency=fij
                    occurrence.score = score
                target[key.word] = occurrences
        return target
