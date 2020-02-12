# -*- coding: utf-8 -*-
# 对文件进行预处理
# import requests
import tkitFile
import os
import numpy as np
import gensim
import pandas as pd #引入它主要是为了更好的显示效果
from collections import Counter

class Word2vec:
    def __init__(self):
        pass #

    def load(self,model_file='model/word2vec.model')
    """
    加载模型
    """
        self.model = gensim.models.word2vec.Word2Vec.load(model_file)
    def predict_proba(self,oword, iword):
        """
        
        """
        iword_vec = model[iword]
        oword = model.wv.vocab[oword]
        oword_l = model.syn1[oword.point].T
        dot = np.dot(iword_vec, oword_l)
        lprob = -sum(np.logaddexp(0, -dot) + oword.code*dot)
        return lprob


    def keywords(self,s):
        """
        获取关键词
        """
        s = [w for w in s if w in model]
        ws = {w:sum([predict_proba(u, w) for u in s]) for w in s}
        return Counter(ws).most_common()



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