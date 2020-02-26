import codecs
import os
import re
# import string
import jieba
import jieba.analyse
from collections import Counter, defaultdict
from src.analysis.analysis_base import AnalysisBase

class SegmentJiebaSSC(AnalysisBase):
    """
        Description:
            tokenize str into a list of word
    """

    def __init__(self, dict_map, config):
        self.dict_map = dict_map
        self.config = config
        self._load_userdict()
        self.stopwords = []
        if 'stopwords' in self.config['use_dict_name']:
            self.stopwords = self.dict_map['stopwords']
        # 去掉字母和数字
        self.prefilter = self.config['prefilter']
        # 是否移除停用词
        self.ifremove = self.config['ifremove']
        self.iflower = self.config['iflower']

    def _load_userdict(self):
        self.ents = []
        if 'user_dict_path' in self.config and os.path.exists(self.config['user_dict_path']):
            jieba.load_userdict(self.config['user_dict_path'])
            self.ents = self.dict_map['user_dict_path']

    def extract_tags(self, text):
        return jieba.analyse.extract_tags(text, topK=10, withWeight=True)

    def seg(self, text):
        tokens = []
        if self.iflower and isinstance(text, str):
            text = text.lower()
        # python3
        if self.prefilter:  # 去掉所有字母和数字
            text = re.sub(r"[\w\d]+", " ", text, flags=re.ASCII)

        for x in jieba.cut(text, cut_all=False):
            x = x.strip()
            if self.ifremove and x in self.stopwords:
                continue
            if len(x) < 1:
                continue
            tokens.append(x)
        return tokens

    def process(self, text):
        terms = self.seg(text)
        tf = Counter(terms)
        idf_dict = defaultdict(float)
        for i, v in self.extract_tags(text):
            if i in self.ents:
                if v < 5:
                    idf_dict[i] = v + 1
                else:
                    idf_dict[i] = v
            else:
                idf_dict[i] = v
        for term in terms:
            if not term in idf_dict:
                if term in self.ents:
                    idf_dict[term] = 5
                else:
                    idf_dict[term] = 0.5
        return (terms, tf, idf_dict)


class SegmentHanlp(AnalysisBase):

    def __init__(self, dict_map, config):
        from pyhanlp import HanLP
        self.dict_map = dict_map
        self.config = config
        self.stopwords = []
        if 'stopwords' in self.config['use_dict_name']:
            self.stopwords = self.dict_map['stopwords']
        # 去掉字母和数字
        self.prefilter = False
        # 是否移除停用词
        self.ifremove = True
        self.iflower = True

    def seg(self, text):
        tokens = []
        if self.iflower:
            text = text.lower()
        # python3
        if self.prefilter:  # 去掉所有字母和数字
            text = re.sub(r"[\w\d]+", " ", text, flags=re.ASCII)
        for x in HanLP.segment(text, cut_all=False):
            x = x.word.strip()
            if self.ifremove and x in self.stopwords:
                continue
            if len(x) < 1:
                continue
            tokens.append(x)
        return tokens

    def process(self, text):
        return self.seg(text)
