# -*- coding: utf-8 -*-

import re
import json
import datetime

camel_pat = re.compile(r'([A-Z])')
under_pat = re.compile(r'_([a-z])')


def camel_to_underscore(name):
    return camel_pat.sub(lambda x: '_' + x.group(1).lower(), name)


def underscore_to_camel(name):
    return under_pat.sub(lambda x: x.group(1).upper(), name)


class K8sDataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, object):
            if hasattr(obj, 'to_dict'):
                return obj.to_dict()
            else:
                return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


def filter_dict_null_value(obj):
    if type(obj) is list:
        return [filter_dict_null_value(item) for item in obj]
    if type(obj) is not dict:
        return obj
    ret = {}
    for k, v in obj.items():
        if type(v) is dict:
            new_v = filter_dict_null_value(v)
        elif type(v) is list:
            new_v = [filter_dict_null_value(item) for item in v]
        elif v is None:
            continue
        else:
            new_v = v
        ret[underscore_to_camel(k)] = new_v
    return ret
