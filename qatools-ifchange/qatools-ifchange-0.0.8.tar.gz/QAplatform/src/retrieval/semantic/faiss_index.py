import faiss
import numpy as np
from src.retrieval.retrieval_base import RetrievalBase

class FaissIndex(RetrievalBase):
    def __init__(self, config):
        if 'vec_size' not in config:
            raise KeyError("RetrievalFaiss plugin not have vec_size attribute")
        self.vec_size = config['vec_size']
        self.top_k = 50
        if 'top_k' in config:
            self.top_k = int(config['top_k'])
        index = faiss.IndexFlatL2(self.vec_size)
        self.indexidmap = faiss.IndexIDMap(index)

    def _build_index(self, corpus):
        kvdict = {idx: items[0] for idx, items in corpus[3].items()}
        for idx, vec in  kvdict.items():
            self.indexidmap.add_with_ids(vec.reshape(1, -1), np.array([idx]))
        print(f"Faiss_Index: count ntotal:{self.indexidmap.ntotal}")

    def add_index(self, corpus):
        ntotal = self.indexidmap.ntotal
        kvdict = {idx+ntotal: items[0] for idx, items in corpus[3].items()}
        for idx, vec in kvdict.items():
            self.indexidmap.add_with_ids(vec.reshape(1, -1), np.array([idx]))
        print("add {} new data, current faiss total {}".format(len(corpus), self.indexidmap.ntotal))

    def search(self, queryinfo, resultinfo):
        # 搜索与当前向量最相近的k个向量的索引
        _ , ids = self.indexidmap.search(queryinfo.embinfo[0].reshape(1, -1), self.top_k)
        resultinfo.retrieval['faiss'] = ids[0]
        resultinfo.retrieval['allids'] = ids[0]
