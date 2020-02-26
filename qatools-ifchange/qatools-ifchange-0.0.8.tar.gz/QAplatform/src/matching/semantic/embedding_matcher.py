from src.matching.matching_base import MatchingBase
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class EmbeddingCosineMatcher(MatchingBase):
    def computer_simlarity(self, query_info, retrived_indices):
        query = query_info.embinfo[0]
        samples = [self.dict_map['corpus'][3][sample] for sample in retrived_indices]
        return self._calc_cos(samples, query)

    def _calc_cos(self, docs, query):
        cosineSimilarities = cosine_similarity(query, docs).flatten()
        return cosineSimilarities

