"""This module provides the authorization of messages."""

from __future__ import unicode_literals
import binascii
import hashlib
import random

from .utils import random_bytes


__all__ = ['MD5', 'SHA1', 'SHA256', 'SHA512']


class _Algorithm(object):
    """The factory class of keys."""

    def __init__(self, algorithm_id, key_size):
        self.algorithm_id = algorithm_id
        self.key_size = key_size

    def key(self, password):
        """Return an instance of :class:`Key`."""
        return Key(password, self.algorithm_id)


#: (128-bit, 16 byte, 32 character length when hex encoded)
MD5 = _Algorithm('MD5', 16)
#: (160-bit, 20 byte, 40 character length when hex encoded)
SHA1 = _Algorithm('SHA1', 20)
#: (256-bit, 32 byte, 64 character length when hex encoded)
SHA256 = _Algorithm('SHA256', 32)
#: (512-bit, 64 byte, 128 character length when hex encoded)
SHA512 = _Algorithm('SHA512', 64)

MIN_SALT_BYTES = 4
MAX_SALT_BYTES = 16


def random_salt():
    """Generate random salt."""
    num = random.randint(MIN_SALT_BYTES, MAX_SALT_BYTES)
    return random_bytes(num)


class Key(object):
    """The authorization of messages.

    :param password: the password.
    :param salt: the salt of the hashing.  If it is `None`, the random salt is
                 generated.  Defaults to `None`.
    :param algorithm_id: the algorithm of the hashing.  Specify `'MD5'`,
                         `'SHA1'`, `'SHA256'` or `'SHA512'`.
                         Defaults to `'SHA256'`.
    """

    def __init__(self, password, algorithm_id='SHA256', salt=None):
        self.password = password.encode('utf-8')
        self.algorithm_id = algorithm_id
        self.salt = salt or random_salt()

        algorithm = getattr(hashlib, algorithm_id.lower())
        key_basis = self.password + self.salt
        self.key = algorithm(key_basis).digest()
        self.key_hash = algorithm(self.key).digest()

    @property
    def salt_hex(self):
        """The hex-encoded hash of the salt."""
        return binascii.hexlify(self.salt)

    @property
    def key_hex(self):
        """The hex-encoded key."""
        return binascii.hexlify(self.key)

    @property
    def key_hash_hex(self):
        """The hex-encoded hash of the key."""
        return binascii.hexlify(self.key_hash)
