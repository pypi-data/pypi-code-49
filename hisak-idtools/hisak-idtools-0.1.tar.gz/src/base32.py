import sys
import binascii

BASE32_ALPHABET = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'
BASE32HEX_ALPHABET = b'0123456789ABCDEFGHIJKLMNOPQRSTUV'
CROCKFORD_ALPHABET = b'0123456789ABCDEFGHJKMNPQRSTVWXYZ'
ZBASE32_ALPHABET = b'ybndrfg8ejkmcpqxotluwisza345h769'

_py3k = sys.version_info.major > 2


class Base32:
    _b32tab = _b32rev = None

    def __init__(self, base32hex=False, crockford=False, zbase32=False):
        # type: (bool, bool, bool) -> None
        if base32hex:
            self._b32alphabet = BASE32HEX_ALPHABET
            self._padding = True
        elif crockford:
            self._b32alphabet = CROCKFORD_ALPHABET
            self._padding = False
        elif zbase32:
            self._b32alphabet = ZBASE32_ALPHABET
            self._padding = False
        else:
            self._b32alphabet = BASE32_ALPHABET
            self._padding = True

    def encode(self, s):
        # type: (bytes) -> bytes
        if self._b32tab is None:
            b32tab = [bytes((i,)) for i in self._b32alphabet] \
                if _py3k else [bytes(i) for i in self._b32alphabet]
            self._b32tab = [a + b for a in b32tab for b in b32tab]
        leftover = len(s) % 5
        if leftover:
            s = s + b'\0' * (5 - leftover)
        b32tab = self._b32tab
        encoded = bytearray()
        if _py3k:
            from_bytes = int.from_bytes
            for i in range(0, len(s), 5):
                c = from_bytes(s[i:i+5], 'big')
                encoded += (b32tab[c >> 30] +
                            b32tab[(c >> 20) & 0x3ff] +
                            b32tab[(c >> 10) & 0x3ff] +
                            b32tab[c & 0x3ff])
        else:
            for i in range(0, len(s), 5):
                c = int(binascii.hexlify(s[i:i+5]), 16)
                encoded += (b32tab[c >> 30] +
                            b32tab[(c >> 20) & 0x3ff] +
                            b32tab[(c >> 10) & 0x3ff] +
                            b32tab[c & 0x3ff])
        if leftover == 1:
            encoded[-6:] = b'======' if self._padding else b''
        elif leftover == 2:
            encoded[-4:] = b'====' if self._padding else b''
        elif leftover == 3:
            encoded[-3:] = b'===' if self._padding else b''
        elif leftover == 4:
            encoded[-1:] = b'=' if self._padding else b''
        return bytes(encoded)

    def decode(self, s):
        # type: (bytes) -> bytes
        if self._b32rev is None:
            self._b32rev = {v: k for k, v in enumerate(self._b32alphabet)}
        leftover = len(s) % 8
        if leftover:
            s = s + b'=' * (8 - leftover)
        size = len(s)
        s = s.rstrip(b'=')
        pad = size - len(s)
        acc = 0
        b32rev = self._b32rev
        decoded = bytearray()
        if _py3k:
            for i in range(0, len(s), 8):
                quanta = s[i: i + 8]
                acc = 0
                try:
                    for c in quanta:
                        acc = (acc << 5) + b32rev[c]
                except KeyError:
                    raise binascii.Error('Non-base32 digit found')
                decoded += acc.to_bytes(5, 'big')
            if size % 8 or pad not in {0, 1, 3, 4, 6}:
                raise binascii.Error('Incorrect padding')
            if pad and decoded:
                acc <<= 5 * pad
                last = acc.to_bytes(5, 'big')
                leftover = (43 - 5 * pad) // 8
                decoded[-5:] = last[:leftover]
        else:
            for i in range(0, len(s), 8):
                quanta = s[i: i + 8]
                acc = 0
                try:
                    for c in quanta:
                        acc = (acc << 5) + b32rev[c]
                except KeyError:
                    raise binascii.Error('Non-base32 digit found')
                decoded += binascii.unhexlify('%010x' % acc)
            if size % 8 or pad not in {0, 1, 3, 4, 6}:
                raise binascii.Error('Incorrect padding')
            if pad and decoded:
                acc <<= 5 * pad
                last = binascii.unhexlify('%010x' % acc)
                leftover = (43 - 5 * pad) // 8
                decoded[-5:] = last[:leftover]
        return bytes(decoded)
