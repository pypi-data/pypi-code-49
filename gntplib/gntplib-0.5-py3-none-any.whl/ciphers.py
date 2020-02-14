"""This module provides the encryption of messages built on PyCrypto_.

.. _PyCrypto: http://pycrypto.org/
"""

from __future__ import unicode_literals
import binascii
import struct

import Crypto.Cipher.AES
import Crypto.Cipher.DES
import Crypto.Cipher.DES3

from .utils import random_bytes


__all__ = ['AES', 'DES', 'DES3']


class _Algorithm(object):
    """The factory class of ciphers."""

    def __init__(self, algorithm_id, key_size):
        self.algorithm_id = algorithm_id
        self.key_size = key_size

    def cipher(self, key):
        """Return an instance of :class:`Cipher`."""
        return Cipher(key, self.algorithm_id)


#: key length: 24 bytes (192 bit), block size: 16 byte (128 bit), iv size: 16
#: byte (128 bit)
AES = _Algorithm('AES', 24)
#: key length: 8 bytes (64 bit), block size: 8 byte (64 bit), iv size: 8 byte
#: (64 bit)
DES = _Algorithm('DES', 8)
#: key length: 24 bytes (192 bit), block size: 8 byte (64 bit), iv size: 8 byte
#: (64 bit)
DES3 = _Algorithm('3DES', 24)

ALGORITHM_MAP = {
    'AES': Crypto.Cipher.AES,
    'DES': Crypto.Cipher.DES,
    '3DES': Crypto.Cipher.DES3,
    }
KEY_SIZE_MAP = {
    'AES': 24,
    'DES': 8,
    '3DES': 24,
    }


class Cipher(object):
    """The encryption of messages.

    :param key: the key of the encryption.
    :param algorithm_id: the algorithm of the encryption.  Specify `'AES'`,
                        `'DES'` or `'3DES'`.
    :param iv: the initial value.
    """

    def __init__(self, key, algorithm_id='DES', iv=None):
        self.key = key
        self.key_size = KEY_SIZE_MAP[algorithm_id]
        self.algorithm = ALGORITHM_MAP[algorithm_id]
        self.algorithm_id = algorithm_id
        self.iv = iv or self._random_iv()

    @property
    def iv_hex(self):
        """The hex-encoded iv."""
        return binascii.hexlify(self.iv)

    def encrypt(self, text):
        return self._cipher().encrypt(self._padding(text))

    def decrypt(self, text):
        return self._unpadding(self._cipher().decrypt(text))

    def _cipher(self):
        return self.algorithm.new(self.key.key[:self.key_size],
                                  self.algorithm.MODE_CBC,
                                  self.iv)

    def _padding(self, text):
        """PKCS5 (PKCS7) padding."""
        num = self.algorithm.block_size - len(text) % self.algorithm.block_size
        return text + struct.pack(b'B' * num, *([num] * num))

    def _unpadding(self, text):
        """Reverse PKCS5 (PKCS7) padding."""
        num = ord(text[-1:])
        return text[:-num]

    def _random_iv(self):
        return random_bytes(self.algorithm.block_size)
