from src.common.utils import load_func

class RetrievalStrategy:
    def __init__(self, dict_map, retireval_config):
        self.dict_map = dict_map
        # 读取配置文件
        self.retireval_config = retireval_config
        # 用于存放所有的方法实例
        self.method_dict = {}
        if len(self.retireval_config) < 1:
            raise ValueError("len(Retrieval plugin)==0")
        for name, method_config in self.retireval_config.items():
            if method_config['use']:
                func, other_params = load_func(method_config)
                retrieval_tool = func(other_params)
                self.method_dict[name] = retrieval_tool

    def buildIndex(self, corpus):
        for name in self.method_dict:
            self.method_dict[name]._build_index(corpus)

    def add_index(self, extra_corpus):
        for name in self.method_dict:
            if name.lower() == 'faiss':
                self.method_dict[name].add_indenx(extra_corpus)

    def merge(self, resultinfo):
        pass

    def retrieve(self, queryinfo, resultinfo):
        '''
        返回的是召回的id集合， matching 部分需要通过id集合从全局字典中取值。
        '''
        # 各分支分别召回, 返回idx的列表
        for name, retireval_tool in self.method_dict.items():
                retireval_tool.search(queryinfo, resultinfo)
        if len(self.method_dict) > 1:
            self.merge(resultinfo)
