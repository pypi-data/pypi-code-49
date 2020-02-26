import numpy as np
import os

from gensim.models import KeyedVectors
from src.analysis.analysis_base import AnalysisBase
import logging
from src.QAsearch import rootpath
logger = logging.getLogger("QAsearch")

class SenEmbeddingBase(AnalysisBase):

    def __init__(self, vec_path=None, remote_path=None):
        self.vec_path = vec_path
        self.remote_path = remote_path
        self._load_vec()
        self.word2id = dict(
            zip(self.w2v.index2word, range(len(self.w2v.index2word))))

    def _load_vec(self):
        if self.vec_path is not None and os.path.exists(self.vec_path):
            if self.vec_path.endswith('model'):
                self.w2v = KeyedVectors.load(self.vec_path)
            elif self.vec_path.endswith('txt'):
                self.w2v = KeyedVectors.load_word2vec_format(
                    self.vec_path, binary=False)
            else:
                raise FileNotFoundError(
                    f"The embedding file: {self.vec_path} is not supported to parse ! ")
        elif self.remote_path is not None:
            print("the first time, need to download the emb file ,please wait 1min....")
            ret = os.system("hadoop fs -get "+self.remote_path+" "+ self.vec_path)
            if ret != 0:
                os.system("cp "+self.vec_path+".small "+self.vec_path)
                print("ATTENTION!!!! can't connect to hdfs, use the partial embfile now, please download the full embfile manually to [{}]/data/embedding.txt!!!!".format(rootpath))
            if self.vec_path.endswith('model'):
                self.w2v = KeyedVectors.load(self.vec_path)
            elif self.vec_path.endswith('txt'):
                self.w2v = KeyedVectors.load_word2vec_format(
                    self.vec_path, binary=False)
            else:
                raise FileNotFoundError(
                    f"The embedding file: {self.vec_path} is not supported to parse ! ")
        else:
            raise FileNotFoundError("The w2v file is not exists ! ")
        logger.info("load vec successfully")

    def get_sen_emb(self, line):
        # line repr one unit, maybe segs[list] or text[str] or others
        raise NotImplementedError(
            "SenEmbedding mush have the function about get_sen_emb")

    def process(self, line):
        return self.get_sen_emb(line)

class SenEmbeddingSSC(SenEmbeddingBase):
    def __init__(self, dict_map, config):
        self.dict_map = dict_map
        self.config = config
        vec_path = ""
        remote_path = ""
        if 'vec_path' in config:
            vec_path = config['vec_path']
        if 'remote_path' in config:
            remote_path = config['remote_path']

        SenEmbeddingBase.__init__(self, vec_path, remote_path)
        # tokens must exists in SenEmbeddingSSC
        #if 'segment_token_basic' not in config['use_dict_name']:
        #    raise KeyError("SenEmbeddingSSC not have segment_token_basic")
        if 'sen_vec_size' not in config:
            raise KeyError("SenEmbeddingSSC not have sen_vec_size")
        self.sen_vec_size = config["sen_vec_size"]
        self._cache_vec = {}

    def _new_vector(self, v):
        return v if v is not None else np.random.randn(self.w2v.vector_size).astype("float32")

    def _max_match_segment(self, text, window_max=5):
        match = False
        idx = 0
        word = []
        while idx < len(text):
            for i in range(window_max, 0, -1):
                cand = text[idx:idx + i]
                if cand in self.w2v:
                    word.append(cand)
                    match = True
                    break
            if not match:
                i = 1
                word.append(text[idx])
            idx += 1
        return word

    def _get_word_emb(self, word):
        v = None
        if word is None:
            return None
        if word in self._cache_vec:
            return self._cache_vec[word]
        if word in self.w2v:
            v = self.w2v[word]
        else:
            words = self._max_match_segment(word)
            vector = np.zeros(self.w2v.vector_size, dtype="float32")
            for token in words:
                if token in self.w2v:
                    vector += self.w2v[token]
                else:
                    # ignore word not in vocab after the max_match_segment function
                    vector += np.zeros(self.w2v.vector_size).astype("float32")
            v = vector / len(words)
        v = self._new_vector(v)
        self._cache_vec[word] = v
        return v

    def get_sen_emb(self, tokens_basic):
        '''
        输入参数，格式如：(terms, tf, idf_dict)
        '''
        # terms repr sentence after tokenizer; list
        terms, tf, idf_dict = tokens_basic
        terms_id = [self.word2id[w] for w in terms if w in self.word2id]
        if len(terms) < 1:
            return (np.zeros(self.sen_vec_size, dtype="float32"), terms_id)
        # build vector
        vector = np.zeros(self.sen_vec_size, dtype="float32")
        w = 0
        for term in terms:
            vector += self._get_word_emb(term) * idf_dict[term]
            w += idf_dict[term]
        if w == 0:
            return (vector, None)
        else:
            return (vector / w, terms_id)
