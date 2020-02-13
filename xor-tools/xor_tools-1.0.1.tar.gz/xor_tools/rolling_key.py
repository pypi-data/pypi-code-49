#!/usr/bin/env python3

"""
Module containing RollingKey class, implementing
key, that could be used for encryption element by element.

Example:
    rk = RollingKey(b'ABCD')
    ciphertext = [ c^k for c,k in zip(plaintext, rk) ]
"""


class RollingKey:
    """
     Class implementing rolling key, that could be used
    over and over for encrypting with repeated key.

    WARNING: Rolling codes should NOT be used for implementations
             where high security is important component (like OTP).
    """

    def __init__(self, key):
        self.key = key
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.key):
            self.index = 0
        tmp = self.key[self.index]
        self.index += 1
        return tmp

    def __getitem__(self, index):
        return self.key[index % len(self.key)]

    def __str__(self):
        if len(self.key) > 10:
            return "RollingKey(%s ...)" % self.key[:10]
        else:
            return "RollingKey(%s)" % self.key[:10]


def test():
    rk = RollingKey(b'ABCD')

    assert next(rk) == 65
    assert next(rk) == 66
    assert next(rk) == 67
    assert next(rk) == 68
    assert next(rk) == 65

    assert rk[1000] == 65


if __name__ == "__main__":
    test()
