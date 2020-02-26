from src.common.utils import load_func

class RankStrategy:
    def __init__(self, dict_map, rank_config):
        self.dict_map = dict_map
        self.rank_config = rank_config
        self.methods = {}
        for rank_name in self.rank_config:
            if not self.rank_config[rank_name]["use"]:
                continue
            func, _ = load_func(self.rank_config[rank_name])
            self.methods[rank_name] = func()

    def _merge(self):
        pass

    def rank(self, queryinfo, resultinfo, num):
        resultinfo.rank = {}
        for method in self.methods:
            resultinfo.rank[method] = self.methods[method].predict(resultinfo.matching[method], resultinfo.retrieval['allids'], num)
            resultinfo.rank['final'] = resultinfo.rank[method]
        if len(self.methods) > 0:
            self._merge()

