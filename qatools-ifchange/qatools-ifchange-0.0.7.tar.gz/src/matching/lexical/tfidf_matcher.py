from src.matching.matching_base import MatchingBase
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TfidfCosineMatcher(MatchingBase):
    def computer_simlarity(self, query_info, retrived_indices):
        vectorizer = TfidfVectorizer()
        #TODO should fit on all corpus
        query = query_info.terminfo
        samples = [self.dict_map['corpus'][2][idx] for idx in retrived_indices]
        docs_tfidf = vectorizer.fit_transform(samples)
        query_tfidf = vectorizer.transform(query)
        return self._calc_cos(docs_tfidf, query_tfidf)

    def _calc_cos(self, docs, query):
        cosineSimilarities = cosine_similarity(query, docs).flatten()
        return cosineSimilarities

