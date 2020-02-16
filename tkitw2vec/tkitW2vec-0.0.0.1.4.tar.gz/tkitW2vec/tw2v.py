# -*- coding: utf-8 -*-
# 对文件进行预处理
# import requests
import tkitFile
import os
import numpy as np
import gensim
import pandas as pd #引入它主要是为了更好的显示效果
from collections import Counter
import gc
import pkuseg
from gensim.models import KeyedVectors
from .word2vec_textrank import  *

class Word2vec:
    def __init__(self):
        # print(__file__,locals())
        # self.parent = os.path.dirname(os.path.realpath(__file__))
        # print(parent)
        
        pass #
    def __del__(self):
        del self.model
        gc.collect()
    def load(self,model_file='model/word2vec.vector.model',model_tpye='all',binary=True,limit=50000):
        """
        加载模型
        >>> model_tpye 'wv' or 'all','fast'
        如果预测关键词只能加载all模型

        """
        # self.model = gensim.models.word2vec.Word2Vec.load(model_file)
        if model_tpye=="wv":
            self.model = gensim.models.KeyedVectors.load_word2vec_format(model_file,binary=binary,limit=limit)
        elif model_tpye=="fast":
            self.model =  KeyedVectors.load(model_file,mmap='r')
            self.model.syn0norm = self.model.syn0 
        else:
            self.model = gensim.models.word2vec.Word2Vec.load(model_file)
    def save(self,model_file='model/word2vec.vector.model',binary=True):
        """
        转化为二进制文件 加载加速
        """
        # self.model = gensim.models.word2vec.Word2Vec.load(model_file)
        self.model.wv.save_word2vec_format(model_file, binary=binary)
    def predict_proba(self,oword, iword):
        """
        
        """
        iword_vec = self.model[iword]
        oword = self.model.wv.vocab[oword]
        oword_l = self.model.syn1[oword.point].T
        dot = np.dot(iword_vec, oword_l)
        lprob = -sum(np.logaddexp(0, -dot) + oword.code*dot)
        # print(lprob)
        return lprob


    def keywords(self,text):
        """
        获取关键词
        
        """
        parent = os.path.dirname(os.path.realpath(__file__))
        seg=pkuseg.pkuseg(model_name = "default", user_dict = parent+"/resources/dict.txt", postag = False)
        text_list=seg.cut(text)      
        s = [w for w in text_list if w in self.model]
        # print(s)
        ws = {w:sum([self.predict_proba(u, w) for u in s]) for w in s}
        # print("Counter(ws).most_common()",Counter(ws).most_common())
        return Counter(ws).most_common()
    # def keywords(self,text):
    #     """
    #     获取关键词
        
    #     """
    #     x = pd.Series(self.keywords(text))
    #     return x
    def most_similar(self,text='',text_b=None,topn=20):
        """
        获取最相关的词语
        """
        parent = os.path.dirname(os.path.realpath(__file__))
        seg=pkuseg.pkuseg(model_name = "default", user_dict = parent+"/resources/dict.txt", postag = False)
        text_list=seg.cut(text)
        print("text_b",text_b)
        if text_b==None:
            text_b_list=None
            return self.model.most_similar(text_list, topn=topn) # 20个最相关的
            pass
        else:
            try:
                text_b_list=seg.cut(str(text_b))
            except :
                text_b_list=str(text_b)
            print(text_b_list)
            return self.model.most_similar(text_list,text_b_list, topn=topn) # 20个最相关的

        # 计算某个词的相关词列表
        
    def doesnt_match(self,text=''):
        """
        获取句子中可能错误的词
        """
        parent = os.path.dirname(os.path.realpath(__file__))
        seg=pkuseg.pkuseg(model_name = "default", user_dict = parent+"/resources/dict.txt", postag = False)
        text_list=seg.cut(text)
        # 计算某个词的相关词列表
        return self.model.doesnt_match(text_list)


    def summary(self,text,topn=5):
        """
        获取摘要
        """
        return do(text,self.model,topn)


# # 计算两个词的相似度/相关程度
# y1 = model.similarity(u"哈士奇", u"狗")

# print(y1)
# # 计算某个词的相关词列表
# y2 = model.most_similar(['柯基','犬'], topn=20) # 20个最相关的
# print(y2)
# # 计算某个词的相关词列表
# y2 = model.similar_by_word(u"柯基犬", topn=20) # 20个最相关的
# print(y2)
# y2 = model.n_similarity(u"柯基犬", topn=20) # 20个最相关的
# print(y2)

# # 寻找对应关系
# print (u"书-不错，质量-")
# y3 = model.most_similar([u'质量', u'不错'], [u'书'], topn=3)
# for item in y3:
#   print (item[0], item[1])
# print ("--------\n")



# # 寻找不合群的词
# y4 = model.doesnt_match(u"书 书籍 教材 很".split())
# print (u"不合群的词：", y4)
# print ("--------\n")