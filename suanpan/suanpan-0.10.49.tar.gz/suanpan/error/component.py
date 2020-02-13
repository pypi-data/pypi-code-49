# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.error import base


class ComponentError(base.Error):
    MESSAGE = "Suanpan Component Error: {}"
