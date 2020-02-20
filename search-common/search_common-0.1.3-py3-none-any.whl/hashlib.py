"""Hash library.

Hash functions commonly used for information retrieval.
"""
from hashlib import md5


def hash32(s):
    """Get the 32-hash of s using first 4 bytes of md5."""
    m = md5(s.encode())
    return int.from_bytes(m.digest()[:4], byteorder='big', signed=True)


def hash64(s):
    """Get the 64-hash of s using first 8 bytes of md5."""
    m = md5(s.encode())
    return int.from_bytes(m.digest()[:8], byteorder='big', signed=True)


def termhash32(s):
    """Get the term hash 32."""
    return hash32('_term_' + s)


def termhash64(s):
    """Get the term hash 64."""
    return hash64('_term_' + s)
