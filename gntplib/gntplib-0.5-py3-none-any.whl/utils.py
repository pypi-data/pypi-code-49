"""This module provides utilities."""

from __future__ import unicode_literals
import random
import struct


def random_bytes(num):
    """Return a bytes containing `n` bytes of random data."""
    return struct.pack(b'B' * num,
                       *[random.randint(0, 255) for _ in range(num)])
