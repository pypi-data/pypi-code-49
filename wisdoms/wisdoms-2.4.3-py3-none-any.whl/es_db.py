# Created by Q-ays.
# whosqays@gmail.com

# install elasticsearch_dsl before use

# elastic-search tools

from elasticsearch_dsl import Q, Search
from elasticsearch import Elasticsearch
from datetime import datetime


def inner_o2d_filter(o):
    for k in o:
        if isinstance(o[k], dict):
            inner_o2d_filter(o[k])
        if isinstance(o[k], datetime):
            o[k] = o[k].strftime("%Y-%m-%d %H:%M:%S")


def o2d(obj):
    is_arr = isinstance(obj, list)
    is_set = isinstance(obj, set)

    if is_set or is_arr:
        res = []
        for o in obj:
            if not isinstance(o, dict):
                d0 = o.to_dict(include_meta=True)
                d1 = d0.get('_source')
                d1['id'] = d0.get('_id')
                inner_o2d_filter(d1)
                res.append(d1)
            else:
                if o.get('_source'):
                    d0 = o.get('_source')
                    d0['id'] = o.get('_id')
                    inner_o2d_filter(d0)
                    res.append(d0)
                else:
                    inner_o2d_filter(o)
                    res.append(o)

        return res

    if not isinstance(obj, dict):
        d0 = obj.to_dict(include_meta=True)
        d1 = d0.get('_source')
        d1['id'] = d0.get('_id')
        inner_o2d_filter(d1)
        return d1
    else:
        if obj.get('data'):
            data = obj.get('data')
            obj['data'] = o2d(data)

        return obj


def str2arr(value, char=','):
    """分离字符串通过特殊字符"""

    if not value or not isinstance(value, str):
        return None

    sort_list = value.split(char)
    return list(filter(lambda x: x.strip(), sort_list))


class BaseRepo:
    """
    基于es数据库增删改查的公共类
    """

    def __init__(self, ModelType):
        self.Model = ModelType
        self.index = ModelType.Index.name

    def add(self, data):
        print(data)
        model = self.Model(**data)
        model.save()
        return model

    def delete(self, did=None):
        if did:
            res = self.Model.get(did)
            res.delete()
            return res

    def update(self, did, data):
        model = self.Model.get(did)
        for key in data:
            if hasattr(model, key):
                setattr(model, key, data[key])
        model.save()
        return model

    def get(self, did=None, p=None, **kwargs):
        """
        查询对象字段时，参数为对象
        :param did:
        :param p:
        :param kwargs:
        :return:
        """
        if did:
            if isinstance(did, list):
                obj = self.Model.mget(did)
            else:
                obj = self.Model.get(did)
        else:
            s = self.Model.search()
            s = s.extra(track_total_hits=True)
            for key in kwargs:
                if isinstance(kwargs[key], dict):
                    s = s.query('nested', path=key, query=Q('match', **{str(key) + '.id': kwargs[key].get('id')}))
                else:
                    s = s.query('match', **{key: kwargs[key]})

            if isinstance(p, list) or isinstance(p, tuple):
                s = s[p[0]:p[1]]
                res = s.execute()
            else:
                res = s.scan()

            obj = []
            for o in res:
                obj.append(o)

        return obj

    def paging(self, searches: dict, page=(0, 50), sort: str = None, types: str = None, **kwargs):
        """
        搜索并带分页功能
        :param searches: 搜索字典
        :param page: (10,20) {"from": 10, "to": 20}
        :param sort: 排序
        :param types: 搜索类型 term, match 默认wildcard模糊搜索
        :param kwargs:
        :return:
        """

        s = self.Model.search()
        s = s.extra(track_total_hits=True)
        keyword = kwargs.get('keyword') if isinstance(kwargs.get('keyword'), str) else 'keyword'
        if keyword:
            keyword = '.' + keyword

        # 搜索查询
        if searches:
            for key, value in searches.items():
                if isinstance(value, dict):
                    # nested 对象查询
                    q = Q()
                    for k, v in value.items():
                        q = q & Q('match', **{str(key) + '.' + k: v})
                    s = s.query('nested', path=key, query=q)
                elif isinstance(value, list):
                    # 范围查询
                    s = s.query('range', **{key: {'gte': value[0], 'lte': value[1]}})
                else:
                    if types in ['term', 'match']:
                        s = s.filter(types, **{key + keyword: value})
                    else:
                        s = s.filter('wildcard', **{key + keyword: '*' + value + '*'})

        # 处理排序
        sort_list = str2arr(sort)
        if sort_list:
            s = s.sort(*sort_list)  # 排序

        # 分页处理
        page_slice = None
        if (isinstance(page, list) or isinstance(page, tuple)) and len(page) == 2:
            page_slice = slice(page[0], page[1])
            s = s[page_slice]
            func = s.execute
        else:
            func = s.scan

        print('Execute Search Dict:', s.to_dict())

        # 获取结果
        data = {}
        try:
            res = func()
        except Exception as e:
            # 捕捉异常，触发可以处理的异常 `wisdoms 异常`
            # raise
            pass
        else:
            result = [{'id': o.meta.id, **o.to_dict()} for o in res]
            if page_slice:
                data['data'] = result
                data['loc'] = page_slice.start
                data['to'] = page_slice.stop
                data['total'] = res.hits.total.value if hasattr(res.hits.total, 'value') else res.hits.total
            else:
                data = result

        return data


class EsSearch:
    '''
     es查询其实是对repo_ref中get方法的完善（nested查询）
    '''

    def __init__(self, ES_HOST, http_auth=None):
        if isinstance(ES_HOST, list):
            self.es = Elasticsearch(ES_HOST, http_auth=http_auth)
        else:
            self.es = Elasticsearch([ES_HOST], http_auth=http_auth)

    def es_search(self, index, p=None, ns_key='id', **kwargs):
        s = Search(using=self.es, index=index)
        for key in kwargs:
            if isinstance(kwargs[key], dict):
                s = s.query('nested', path=key, query=Q('match', **{str(key) + '.' + ns_key: kwargs[key].get(ns_key)}))
            else:
                s = s.filter('term', **{key + '.keyword': kwargs[key]})

        if isinstance(p, list) or isinstance(p, tuple):
            s = s[p[0]:p[1]]
            res = s.execute()
        else:
            res = s.scan()

        return [{"id": o.meta.id, **o.to_dict()} for o in res]

    def paging(self, index: str, searches: dict, page=(0, 50), sort: str = None, types: str = None, **kwargs):
        """
        搜索并带分页功能
        :param index: index名称
        :param searches: 搜索字典
        :param page: (10,20) {"from": 10, "to": 20}
        :param sort: 排序
        :param types: 搜索类型 term, match 默认wildcard模糊搜索
        :param kwargs:
        :return:
        """

        s = Search(using=self.es, index=index)
        s = s.extra(track_total_hits=True)
        keyword = kwargs.get('keyword') if isinstance(kwargs.get('keyword'), str) else 'keyword'
        if keyword:
            keyword = '.' + keyword

        # 搜索查询
        if searches:
            for key, value in searches.items():
                if isinstance(value, dict):
                    # nested 对象查询
                    q = Q()
                    for k, v in value.items():
                        q = q & Q('match', **{str(key) + '.' + k: v})
                    s = s.query('nested', path=key, query=q)
                elif isinstance(value, list):
                    # 范围查询
                    s = s.query('range', **{key: {'gte': value[0], 'lte': value[1]}})
                else:
                    if types in ['term', 'match']:
                        s = s.filter(types, **{key + keyword: value})
                    else:
                        s = s.filter('wildcard', **{key + keyword: '*' + value + '*'})

        # 处理排序
        sort_list = str2arr(sort)
        if sort_list:
            s = s.sort(*sort_list)  # 排序

        # 分页处理
        page_slice = None
        if (isinstance(page, list) or isinstance(page, tuple)) and len(page) == 2:
            page_slice = slice(page[0], page[1])
            s = s[page_slice]
            func = s.execute
        else:
            func = s.scan

        print('Execute Search Dict:', s.to_dict())

        # 获取结果
        data = {}
        try:
            res = func()
        except Exception as e:
            # 捕捉异常，触发可以处理的异常 `wisdoms 异常`
            # raise
            pass
        else:
            result = [{'id': o.meta.id, **o.to_dict()} for o in res]
            if page_slice:
                data['data'] = result
                data['loc'] = page_slice.start
                data['to'] = page_slice.stop
                data['total'] = res.hits.total.value if hasattr(res.hits.total, 'value') else res.hits.total
            else:
                data = result

        return data

    def delete_by_ids(self, index: str, ids):
        """
        删除数据，通过ids
        :param index:
        :param ids: id 或者id列表
        :return:
        """
        s = Search(using=self.es, index=index)
        s = s.query('ids', values=ids)
        res = s.delete()
        return res.to_dict()


Repo = BaseRepo
