#!/usr/bin/env python3
# coding: utf-8

import os
import threading
from collections import OrderedDict

from joker.minions import utils


class CacheMixin(object):
    def __init__(self, data=None):
        self.data = {} if data is None else data

    def execute(self, verb, payload):
        key = payload
        if verb == b'get':
            return self.data.get(key, b'')
        if verb == b'set':
            key, val = utils.split(payload)
            self.data[key] = val
        if verb == b'pop':
            return self.data.pop(key, b'')
        if verb == b'del':
            del self.data[key]
        return b''


class CacheServer(CacheMixin, utils.ServerBase):
    pass


class PipedCacheServer(CacheMixin, utils.PipedServerBase):
    pass


class SizedDict(object):
    default_sizelimit = 2 ** 26

    def __init__(self, sizelimit, *args, **kwargs):
        self.data = OrderedDict(*args, **kwargs)
        self.sizelimit = sizelimit or self.default_sizelimit
        lengths = ((len(k) + len(v)) for k, v in self.data.items())
        self.freespace = sizelimit - sum(lengths)

    def pop(self, key, *default):
        val = self.data.pop(key, *default)
        if (val,) != default:
            self.freespace += len(key) + len(val)
        return val

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, val):
        with threading.Lock():
            pval = self.data.get(key, '')
            self.data[key] = val
            self.freespace += len(pval) - len(val)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def evict(self):
        while self.freespace <= 0:
            self.data.popitem(last=False)


class WarmConf(SizedDict):
    comment = b'#'

    def __init__(self, sizelimit, path):
        path = os.path.expanduser(path)
        data = self.parse(path)
        super(WarmConf, self).__init__(sizelimit, data)
        self.mtime = self._getmtime(path)
        self.path = path

    def __bool__(self):
        return True

    @staticmethod
    def _getmtime(path):
        return int(os.path.getmtime(path) * 1000)

    @classmethod
    def parse(cls, path):
        data = OrderedDict()
        with open(path, 'rb') as fin:
            for line in fin:
                line = line.strip()
                if not line or line.startswith(cls.comment):
                    continue
                parts = line.split(maxsplit=1)
                if len(parts) != 2:
                    continue
                k, v = parts
                data[k] = v
        return data

    def reload(self):
        mtime = self._getmtime(self.path)
        if mtime == self.mtime:
            return
        self.data = self.parse(self.path)
        self.evict()

    def update(self):
        mtime = self._getmtime(self.path)
        if mtime == self.mtime:
            return
        data = self.parse(self.path)
        for k, v in data.items():
            self.data[k] = v
        self.evict()
