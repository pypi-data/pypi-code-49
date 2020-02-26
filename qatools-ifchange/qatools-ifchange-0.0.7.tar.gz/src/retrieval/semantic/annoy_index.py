from annoy import AnnoyIndex
from src.retrieval.retireval_base import RetrievalBase

class AnnoyIndex(RetrievalBase):
    def __init__(self, config):
        if 'vec_size' not in config:
            raise KeyError("RetrievalAnnoy plugin not have vec_size attribute")
        self.vec_size = config['vec_size']
        self.top_k = 50
        if 'top_k' in config:
            self.top_k = config['top_k']
        self.n_trees = 15
        if 'n_trees' in config:
            self.n_trees = config['n_trees']
        self.annoyindex = AnnoyIndex(self.vec_size)

    def _build_index(self, corpus):
        pass

    def search(self, queryinfo, resultinfo):
        pass
