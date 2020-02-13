#!/usr/bin/env python3

import codecs


def plaintext_bytes(string):
    return bytes(codecs.decode(string, 'unicode_escape'), 'utf-8')
