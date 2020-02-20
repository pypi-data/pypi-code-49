# coding=utf8
from __future__ import unicode_literals

import six
import abc
import json
import os

if six.PY2:
    from urlparse import urlparse
else:
    from urllib.parse import urlparse

from envparse import shortcut
from six import with_metaclass

from easy_env.backends import DefaultBackend, AbstractBackend
from easy_env.utils import decrypt


class Env(with_metaclass(abc.ABCMeta, object)):
    """base env class"""

    def __init__(self, namespace=None, backend_class=DefaultBackend, **kw):
        self.backend = backend_class(namespace=namespace, **kw)

        if not isinstance(self.backend, AbstractBackend):
            raise TypeError('backend class must be subclass of AbstractBackend')

    def __call__(self, var, *a, **kw):
        return self.backend.__call__(var, *a, **kw)

    def all(self, *a, **kw):
        """ list all config variables in the namespace"""
        return self.backend.all(*a, **kw)

    def read_envfile(self, *a, **kw):
        return self.flush(*a, **kw)

    def flush(self, *a, **kw):
        return self.backend.flush(*a, **kw)


    # shortcuts
    bool = shortcut(bool)
    dict = shortcut(dict)
    float = shortcut(float)
    int = shortcut(int)
    list = shortcut(list)
    set = shortcut(set)
    str = shortcut(str)
    tuple = shortcut(tuple)
    json = shortcut(json.loads)
    url = shortcut(urlparse)
    secret = shortcut(decrypt)


if __name__ == "__main__":
    os.environ.setdefault('HELLOWORLD_SECRET', '3VpavryXEro5CUWph41NGA==')
    env = Env('helloworld')
    print(env.secret('secret'))
