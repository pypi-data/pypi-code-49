"""
    Classic IR model. Probabilistic model are implemented here, based in Interface Model
"""
from collections import defaultdict
from typing import List, DefaultDict
from math import log

from matchup.models.Model import IterModel, Term, Vocabulary
from matchup.structure.Solution import Result


class Probabilistic(IterModel):

    # V : Conjunto solução
    _V = defaultdict(float)
    
    @staticmethod
    def run(query: List[Term], vocabulary: Vocabulary):
        """
            Principal method that represents IR probabilistic model.
        :param query: list of all query terms
        :param vocabulary: data structure that represents the vocabulary
        :return:
        """
        IterModel.initialize_occurrences(query, vocabulary)

        IterModel.initialize_pointers()

        # one iteration of probabilistic method
        rank = Probabilistic.__iter_rank(vocabulary)

        n_rank = Probabilistic.__take(rank, 5)

        if n_rank == Probabilistic._V:
            return rank
        else:
            Probabilistic._V = n_rank
            return Probabilistic.run(query, vocabulary)

    @staticmethod
    def __generate_term_scores(vocabulary: Vocabulary) -> DefaultDict[str, float]:
        """
            Generate scores of all terms in term occurrences based in Probabilistic model
        :param vocabulary: data structure representing vocabulary
        :return: scores based in keyword
        """
        score = defaultdict(float)

        for key in IterModel._term_occurrences.keys():
            pir = Probabilistic.catch_pir(vocabulary, key)
            qir = Probabilistic.catch_qir(vocabulary, key)

            score[key] = log(pir/(1-pir), 10) + log((1 - qir)/qir, 10)

            # print("\t\tKey {0} => pir : {1} , qir {2} , score : {3}".format(key, pir, qir, score[key]))

        return score

    @staticmethod
    def __stop() -> bool:
        """
            Stop condition of model
        :return: boolean flag indicates if the model needs to stop
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
    def __atualize(doc: str, term_scores: DefaultDict[str, float]) -> float:
        """
            Atualize a lowest document score based in term scores
        :param doc: document to atualize
        :param term_scores: defaultdict of term scores
        :return: score of this document
        """
        score = 0.0
        for key in IterModel._term_occurrences.keys():
            try:
                occ = IterModel._term_occurrences[key][IterModel._pointers[key]]
                if occ.doc() == doc:
                    score += term_scores[key]
                    IterModel._pointers[key] += 1
            except ValueError:
                continue
            except IndexError:
                continue
        return score

    @staticmethod
    def __iter_rank(vocabulary: Vocabulary) -> List[Result]:
        """
            One iteration of Probabilistic model execute. Instable in first versions.
        :param vocabulary: vocabulary structure
        :return: ranked list of documents, scores
        """
        term_scores = Probabilistic.__generate_term_scores(vocabulary)

        scores = defaultdict(float)
        while not Probabilistic.__stop():
            doc = IterModel.lowest_doc()

            # print("lwst : {0}".format(doc))

            scores[doc] = Probabilistic.__atualize(doc, term_scores)

        scores = sorted(scores.items(), key=lambda v: v[1], reverse=True)

        return IterModel.cast_solution(scores)

    @staticmethod
    def __take(rank: List[Result], n: int) -> List[Result]:
        """
            Take the first n elements of this list copying to another structure
        :param rank: list of document, score
        :param n: number of elements to take
        :return: sliced list
        """
        cont = 0
        copy = list()
        for i in rank:
            if cont == n:
                return copy
            cont += 1
            copy.append(i)
        return copy

    @staticmethod
    def catch_pir(vocabulary: Vocabulary, key: str) -> float:
        """
            Catch pir statistic based in key of vocabulary
        :param vocabulary: data structure that represents vocabulary
        :param key: keyword to catch pir
        :return: float pir
        """
        n_value = len(vocabulary.file_names)
        ni = len(Probabilistic._term_occurrences[key])

        if Probabilistic._V:
            vi_value = Probabilistic.docs_with_key(vocabulary[key])
            v_value = len(Probabilistic._V)
            # print("Key {0} => V {1} Vi {2}".format(key, v_value, vi_value))
            return (vi_value + (ni / n_value)) / (v_value + 1)
        else:
            return 0.5

    @staticmethod
    def catch_qir(vocabulary: Vocabulary, key: str) -> float:
        """
            Catch qir statistic based in key of vocabulary
        :param vocabulary: data structure that represents vocabulary
        :param key: keyword to catch pir
        :return: float pir
        """
        n_value = len(vocabulary.file_names)
        ni = len(Probabilistic._term_occurrences[key])

        if Probabilistic._V:
            vi_value = Probabilistic.docs_with_key(vocabulary[key])
            v_value = len(Probabilistic._V)
            return (ni - vi_value + (ni / v_value)) / (n_value - v_value + 1)
        else:
            return ni / n_value

    @staticmethod
    def docs_with_key(occ) -> int:
        """
            Return the vi_value : number of documents with key
        :param occ: Occurrences
        :return:
        """
        doc = 0
        # print("Occurrences : {0}".format(occ))
        for oc in occ:
            if oc.doc() in [t.document for t in Probabilistic._V]:
                doc += 1
        return doc
