class RetrievalBase:
    def build_index(self, *args, **kwargs):
        # 建立初始索引
        raise NotImplementedError("Retireval plugin must have build_index function")
    
    def search(self, qinfo, rinfo):
        # 搜索与当前值最相近的top_k的索引值
        raise NotImplementedError("Retrieval plugin must have search function")
