# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import functools

def gettercache(method):
    key = object()
    @functools.wraps(method)
    def wrapper(self):
        if key not in vars(self):
            vars(self)[key] = method(self)
        return vars(self)[key]
    return wrapper
