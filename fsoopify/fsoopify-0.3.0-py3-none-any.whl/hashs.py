# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import binascii
import hashlib

ALGORITHMS = set(hashlib.algorithms_available)
ALGORITHMS.add('crc32')

class Crc32Proxy:
    def __init__(self):
        self._value = 0

    def update(self, buffer):
        self._value = binascii.crc32(buffer, self._value)

    def hexdigest(self):
        return "%08x" % self._value

def _create(algorithm: str):
    if algorithm == 'crc32':
        return Crc32Proxy()
    return hashlib.new(algorithm)

def hashfile_hexdigest(path: str, algorithms: tuple, *, blocksize=1024 * 64):
    for algorithm in algorithms:
        if not algorithm in ALGORITHMS:
            raise ValueError(f'unsupport algorithm: {algorithm}')
    ms = [_create(x) for x in algorithms]
    with open(path, 'rb') as stream:
        while True:
            buffer = stream.read(blocksize)
            if not buffer:
                break
            for m in ms:
                m.update(buffer)
    return tuple(m.hexdigest() for m in ms)
