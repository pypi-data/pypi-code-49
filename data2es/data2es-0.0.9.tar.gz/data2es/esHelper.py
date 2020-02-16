#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# File Name: esHelper.py
# Author: stosc
# Mail: stosc@sidaxin.com
# Created Time:  2020-2-8 19:17:34
#############################################
from elasticsearch import Elasticsearch
import elasticsearch.helpers

from datetime import datetime


class EsHelper(object):

    def __init__(self, hosts, user="", password=""):
        super().__init__()
        if user == "":
            self.es = Elasticsearch([hosts])
        else:
            self.es = Elasticsearch([hosts], http_auth="%s:%s" % (user, password))

    def saveData(self, index_name, datas, idName="", docName="_doc"):
        '''
        向es插入数据
        '''
        actions = [
            {
                '_op_type': 'index',
                '_index': index_name,
                '_type': docName,
                '_id': d[idName],
                '_source': d
            } if idName != "" else {
                '_op_type': 'index',
                '_index': index_name,
                '_type': docName,
                '_source': d
            }
            for d in datas
        ]
        elasticsearch.helpers.bulk(self.es, actions)


if __name__ == "__main__":
    es = Elasticsearch(['134.175.225.22:9200'], http_auth="elastic:amituofo")

    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        '@timestamp': datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+0800")
    }
    res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
    print(res)

    res = es.get(index="test-index", doc_type='tweet', id=1)
    print(res['_source'])

    es.indices.refresh(index="test-index")

    res = es.search(index="test-index", body={"query": {"match_all": {}}})

    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
