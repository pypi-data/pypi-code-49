from src.matching.matching_base import MatchingBase

class WordJaccardMatcher(MatchingBase):
    def compute_simlarity(self, query_info, retrived_indices):
        seg_query = query_info.terminfo
        seg_samples = [self.dict_map['corpus'][2][sample] for sample in retrived_indices]
        return [word_jaccard(seg_query, sample) for sample in seg_samples]

class CharJaccardMatcher(MatchingBase):
    def compute_simlarity(self, query_info, retrived_indices):
        query = query_info.cleantext
        samples = [self.dict_map['corpus'][0][sample] for sample in retrived_indices]
        return [char_jaccard(query, sample) for sample in samples]

def word_jaccard(seg1, seg2):
    a = list(set(seg1).intersection(set(seg2)))
    b = list(set(seg1).union(set(seg2)))
    return float(len(a) / len(b))


def char_jaccard(sen1, sen2):
    a = list(set(list(sen1)).intersection(set(list(sen2))))
    b = list(set(list(sen1)).union(set(list(sen2))))
    return float(len(a) / len(b))

