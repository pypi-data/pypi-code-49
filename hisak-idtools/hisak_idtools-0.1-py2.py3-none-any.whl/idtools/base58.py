import sys
from hashlib import sha256

BITCOIN_ALPHABET = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
RIPPLE_ALPHABET = b'rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz'
FLICKR_ALPHABET = b'123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'

_py3k = sys.version_info.major > 2
_b58size = 58


class Base58:
    _b58tab = _b58rev = None

    def __init__(self, ripple=False, flickr=False):
        # type: (bool, bool, bool) -> None
        if ripple:
            self._b58alphabet = RIPPLE_ALPHABET
        elif flickr:
            self._b58alphabet = FLICKR_ALPHABET
        else:
            self._b58alphabet = BITCOIN_ALPHABET

    def encode(self, s):
        # type: (bytes) -> bytes
        if self._b58tab is None:
            self._b58tab = [bytes((i,)) for i in self._b58alphabet] \
                if _py3k else [bytes(i) for i in self._b58alphabet]
        pad = len(s)
        s = s.lstrip(b'\0')
        pad -= len(s)
        p, acc = 1, 0
        if _py3k:
            for c in reversed(s):
                acc += p * c
                p <<= 8
        else:
            for c in reversed(s):
                acc += p * ord(c)
                p <<= 8
        buf = b''
        b58tab = self._b58tab
        while acc:
            acc, i = divmod(acc, _b58size)
            buf = b58tab[i] + buf
        return b58tab[0] * pad + buf

    def encode_check(self, s):
        # type: (bytes) -> bytes
        s += sha256(sha256(s).digest()).digest()[:4]
        return self.encode(s)

    def decode(self, s):
        # type: (bytes) -> bytes
        if self._b58rev is None:
            self._b58rev = {v: k for k, v in enumerate(self._b58alphabet)}
        pad = len(s)
        s = s.lstrip(self._b58tab[0])
        pad -= len(s)
        b58rev = self._b58rev
        acc = 0
        buf = b''
        for c in s:
            acc = acc * _b58size + b58rev[c]
        if _py3k:
            buf_ = []
            while acc:
                acc, c = divmod(acc, 256)
                buf_.append(c)
            buf = bytes(reversed(buf_))
        else:
            while acc:
                acc, c = divmod(acc, 256)
                buf = chr(c) + buf
        return b'\0' * pad + buf

    def decode_check(self, s):
        # type: (bytes) -> bytes
        buf = self.decode(s)
        buf, check = buf[:-4], buf[-4:]
        if check != sha256(sha256(buf).digest()).digest()[:4]:
            raise ValueError('Invalid checksum')
        return buf
