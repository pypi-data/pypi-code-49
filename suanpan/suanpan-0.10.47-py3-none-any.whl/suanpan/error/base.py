# coding=utf-8
from __future__ import absolute_import, print_function


class Error(Exception):
    MESSAGE = "Suanpan Error: {}"

    def __init__(self, *args, **kwargs):
        super(Error, self).__init__(self.MESSAGE.format(*args, **kwargs))
