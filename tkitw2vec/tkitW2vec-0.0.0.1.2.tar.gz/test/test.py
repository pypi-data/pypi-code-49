#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

import tkitW2vec


w2v=tkitW2vec.Word2vec()
w2v.load(model_file='../model/data.model')

# 提取关键词
kws=w2v.keywords("柯基犬真是可爱")
print(kws)


# print(w2v.most_similar('柯基犬真是可爱'))

 
 
print(w2v.path)
