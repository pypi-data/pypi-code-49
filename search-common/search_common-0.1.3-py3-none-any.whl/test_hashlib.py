"""Hash functions unittest.

"""
from search_common import hashlib


def test_hash64():
    h64 = hashlib.hash64('hello world')
    assert h64 == 6824707963431612112


def test_hash32():
    h32 = hashlib.hash32('good morning')
    assert h32 == 730109184
