from src.matching.matching_base import MatchingBase
from rank_bm25 import BM25Okapi

class BM25Matcher(MatchingBase):

    def compute_simlarity(self, query_info, retrived_indices):
        #TODO should find a better bm25 package
        '''query and samples should be cleaned and tokenized'''
        query = query_info.terminfo
        samples = [self.dict_map['corpus'][2][idx] for idx in retrived_indices]
        self.bm25 = BM25Okapi(samples)
        scores = self.bm25.get_scores(query)
        return scores


