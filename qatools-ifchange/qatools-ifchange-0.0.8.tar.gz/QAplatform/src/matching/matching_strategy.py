import sys
import types
from src.matching.semantic.bert_matcher import BertMatcher
from src.matching.semantic.embedding_matcher import EmbeddingCosineMatcher
from src.matching.lexical.bm25_matcher import BM25Matcher
from src.matching.lexical.jaccard_matcher import CharJaccardMatcher, WordJaccardMatcher
from src.matching.lexical.tfidf_matcher import TfidfCosineMatcher
def str_to_class(classname):
    try:
        return getattr(sys.modules[__name__], classname)
    except:
        raise NotImplementedError


class MatchingStrategy:
    def __init__(self, dict_map, matching_config):
        self.dict_map = dict_map
        self.matching_config = matching_config
        models = list(self.matching_config.keys())
        self.methods = {}
        for model in models:
            class_nm = self.matching_config[model]['type']
            if self.matching_config[model]['use']:
                self.methods[model] = str_to_class(class_nm)(self.dict_map, self.matching_config[model])

    def match(self, queryinfo, resultinfo):
        ids = resultinfo.retrieval['allids']
        for method in self.methods:
            resultinfo.matching[method] = self.methods[method].compute_similarity(queryinfo, ids)
        return resultinfo
        

