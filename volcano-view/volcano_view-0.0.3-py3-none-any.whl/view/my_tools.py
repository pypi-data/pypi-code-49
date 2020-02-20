import json

from .web_exc import WebException


def to_map(it, key):
    rs = {}
    for item in it:
        rs[item[key]] = item
    return rs


def read_json_wx(file_name, obj=None):
    try:

        with open(file_name, encoding='utf-8') as f:
            return json.load(f)

    except FileNotFoundError as ex:
        if obj is not None:
            return obj
        else:
            raise WebException(ex)

    except Exception as ex:
        raise WebException(ex)


def write_json_wx(json_data, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as outfile:
            json.dump(json_data, outfile, indent=4)
    except Exception as ex:
        raise WebException(ex)


def search(it, fn):
    for item in it:
        if fn(item):
            return item
    return None
