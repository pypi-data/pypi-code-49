#!/usr/bin/env python3
# coding: utf-8

import threading

import mmh3
from bitarray import bitarray

from joker.minions import utils


def _bitarray_get(bitarr, idx):
    try:
        return bitarr[idx]
    except IndexError:
        return False


class BloomFilter(object):
    def __init__(self, size, seed=3):
        self.size = size
        self.seed = seed
        self.bitarr = bitarray(size)
        self.bitarr ^= self.bitarr

    def _compute_hash(self, item):
        return mmh3.hash(item, self.seed) % self.size

    def get(self, key):
        idx = self._compute_hash(key)
        return self.bitarr[idx]

    def getset(self, key, value):
        idx = self._compute_hash(key)
        rv = self.bitarr[idx]
        self.bitarr[idx] = bool(value)
        return rv

    def toggle(self, key):
        idx = self._compute_hash(key)
        with threading.Lock():
            rv = not bool(self.bitarr[idx])
            self.bitarr[idx] = rv
            return rv


class BloomMixin(object):
    val_toggle = b'~'

    def __init__(self, size, seed=3):
        self.bloom = BloomFilter(size, seed)

    def execute(self, verb, payload):
        rv = self._execute(verb, payload)
        return b'01'[int(rv)]

    def _execute(self, verb, key):
        if verb == b'get':
            return self.bloom.get(verb)
        elif verb == b'set':
            return self.bloom.getset(key, True)
        elif verb == b'toggle':
            return self.bloom.toggle(verb)
        elif verb in (b'del', b'pop'):
            return self.bloom.getset(key, False)
        return 0


class BloomServer(BloomMixin, utils.ServerBase):
    pass


class PipedBloomServer(BloomMixin, utils.PipedServerBase):
    pass
