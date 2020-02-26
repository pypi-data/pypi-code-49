#!/anaconda3/bin/python
#coding=utf8
'''
# Author: Gavin King
# Created Time : 二 10/29 17:15:55 2019
'''

import yaml
import sys
import time
import os
rootpath=os.path.abspath(os.path.dirname(__file__))[:-3]
sys.path.append(rootpath)

from src.analysis.analysis_strategy import AnalysisStrategy
from src.retrieval.retrieval_strategy import RetrievalStrategy
from src.matching.matching_strategy import MatchingStrategy
from src.rank.rank_strategy import RankStrategy
from src.common.utils import loaddata, loaddict, QueryInfo, ResultInfo
import logging
from src.common.logger import setlogger
logger = logging.getLogger("QAsearch")

class QAsearch(object):
    def __init__(self, bertip=None, bertport=None):
        # 暂不支持conf地址修改
        conf_path = "conf/simqp.yaml"
        self.status = "fail"
        pwdpath = os.getcwd()
        os.chdir(rootpath)
        try:
            self.config = yaml.safe_load(open(conf_path, 'r', encoding='utf-8'))
            if bertip != None and bertport != None:
                self.config['matching_config']['bert']['server_ip'] = bertip
                self.config['matching_config']['bert']['server_port'] = bertport
            dict_map = loaddict(self.config['dict_config'])
            # 各个子模块的初始化
            self._analysis = AnalysisStrategy(dict_map, self.config['analysis_config'])
            self._retrieval = RetrievalStrategy(dict_map, self.config['retrieval_config'])
            self._matching = MatchingStrategy(dict_map, self.config['matching_config'])
            self._rank = RankStrategy(dict_map, self.config['rank_config'])
            self.dict_map = dict_map
        except:
            os.chdir(pwdpath)
            logger.error("QAsearch init failed")
            raise
        os.chdir(pwdpath)
        setlogger(self.config['logger'])

    def build(self, copus_path=rootpath+"data/corpus-chatbot.txt"):
        idx2ques, idx2label = loaddata(copus_path)
        corpus = self._analysis.buildCorpus(idx2ques, idx2label)
        self.dict_map['corpus'] = corpus
        self._retrieval.buildIndex(corpus)
        self.status = "succ"

    def add_corpus(self, corpus_path=None, corpus=None):
        if corpus_path:
            idx2ques, idx2label = loaddata(corpus_path)
        else:
            idx2ques, idx2label = corpus
        corpus = self._analysis.buildCorpus(idx2ques, idx2label)
        self.dict_map['corpus'] += corpus
        self._retrieval.add_index(corpus)


    def rebuild(self):
        pass

    def query(self, text, num=1):
        if self.status != "succ":
            return None
        try:
            qinfo = QueryInfo(text)
            result = ResultInfo()
            t1 = time.time()
            self._analysis.process(qinfo)
            logger.debug("analysis cost:{}".format(time.time()-t1))
            t1 = time.time()
            self._retrieval.retrieve(qinfo, result)
            logger.debug("retrieval cost:{}".format(time.time()-t1))
            t1 = time.time()
            self._matching.match(qinfo, result)
            logger.debug("matching cost:{}".format(time.time()-t1))
            t1 = time.time()
            self._rank.rank(qinfo, result, num)
            logger.info("rank cost:{}".format(time.time()-t1))
            logger.debug(" ".join([str(i) for i in result.retrieval['allids']]))
            logger.debug(" ".join([str(i) for i in result.matching['bert']]))
            logger.debug(" ".join([str(i[0])+"-"+str(i[1]) for i in result.rank['final']]))
            if num == 1:
                res = (self.dict_map['corpus'][0][int(result.rank['final'][0][1])], self.dict_map['corpus'][1][int(result.rank['final'][0][1])], result.rank['final'][0][0])
            else:
                res = [(self.dict_map['corpus'][0][int(result.rank['final'][i][1])], self.dict_map['corpus'][1][int(result.rank['final'][i][1])], result.rank['final'][i][0]) for i in range(num)]
            return res
        except Exception as e:
            logger.error(e)
            return "","",0.

if __name__ == "__main__":
    #simqp_conf_path = r'./conf/simqp.yaml'
    #copus_path = r'./data/samples.txt'
    #copus_path = "./data/corpus-chatbot.txt"

    Simqp_ins = QAsearch()
    Simqp_ins.build()
    query = "你是谁"
    print(query)
    result = Simqp_ins.query(query, num=3)
    print(result)
    query = "你喜欢什么"
    print(query)
    result = Simqp_ins.query(query)
    print(result)
