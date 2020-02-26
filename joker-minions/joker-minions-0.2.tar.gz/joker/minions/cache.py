#!/usr/bin/env python3
# coding: utf-8

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
