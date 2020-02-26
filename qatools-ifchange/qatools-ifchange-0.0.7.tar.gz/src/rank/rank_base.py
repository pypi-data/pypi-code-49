#
class RankBase(object):
    def predict(self, scores, ids, num):
        raise NotImplementedError("Rank plugin must have predict function")
