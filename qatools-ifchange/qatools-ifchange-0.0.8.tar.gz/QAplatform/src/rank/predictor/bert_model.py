#
from src.rank.rank_base import RankBase
import numpy as np

class BertRank(RankBase):
    def predict(self, scores, ids, num):
        if num == 1:
            scores = np.array(scores)
            max_id = np.argmax(scores)
            return [(scores[max_id], ids[max_id])]
        else:
            zipres = sorted([x for x in zip(scores, ids)],key=lambda x : x[0], reverse=True)[:num]
            return zipres

