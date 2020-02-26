#
from src.common.utils import load_func
class AnalysisStrategy:
    def __init__(self, dict_map, analysis_config):
        self.dict_map = dict_map
        self.analysis_config = analysis_config
        self.bather = None
        self.tokenizer = None
        self.embedder = None
        if 'dataclean' in self.analysis_config and self.analysis_config['dataclean']['use']:
            dataclean_config = self.analysis_config['dataclean']
            func, other_parms = load_func(dataclean_config)
            self.bather = func(self.dict_map, other_parms)
        if 'segment' in self.analysis_config and self.analysis_config['segment']['use']:
            segment_config = self.analysis_config['segment']
            func, other_parms = load_func(segment_config) 
            self.tokenizer = func(self.dict_map, other_parms)
        if 'embedding' in self.analysis_config and self.analysis_config['embedding']['use']:
            embedding_config = self.analysis_config['embedding']
            func, other_parms = load_func(embedding_config) 
            self.embedder = func(self.dict_map, other_parms)

    def buildCorpus(self, idx2ques, idx2label):
        corpus = {}
        idx2ques_bath = idx2ques
        if self.bather:
            idx2ques_bath = self.bather.value_process(idx2ques)
        # 翻转去重,洗完澡后可能会重复
        ques2idx = {ques: idx for idx, ques in idx2ques_bath.items()}
        idx2ques = {idx: ques for ques, idx in ques2idx.items()}
        idx2label = {idx: label for idx, label in idx2label.items() if idx in idx2ques}

        idx2term = None
        idx2emb = None
        if self.tokenizer:
            idx2term = self.tokenizer.value_process(idx2ques)

        if self.tokenizer and self.embedder:
            idx2emb = self.embedder.value_process(idx2term)

        return (idx2ques, idx2label, idx2term, idx2emb)
    
    def process(self, queryinfo):
        # 对输入的query进行分析
        text = queryinfo.text
        textclean = text
        terminfo = None
        embinfo = None
        if self.bather:
            textclean = self.bather.process(text)
        if self.tokenizer:
            # (terms, tf, idf_dict)
            terminfo = self.tokenizer.process(textclean)
        if self.embedder and self.tokenizer:
            # (vec, terms_id)
            embinfo = self.embedder.process(terminfo)
        queryinfo.textclean = textclean
        queryinfo.terminfo = terminfo
        queryinfo.embinfo = embinfo
