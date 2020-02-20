# coding=utf8
import abc
import os

from envparse import Env as _Env
from six import with_metaclass


class AbstractBackend(with_metaclass(abc.ABCMeta, object)):
    """abstract backend"""

    def __init__(self, namespace='', **kw):
        self.namespace = namespace

    @abc.abstractmethod
    def __call__(self, *a, **kw):
        pass

    @abc.abstractmethod
    def all(self, *a, **kw):
        pass

    @abc.abstractmethod
    def flush(self, *a, **kw):
        pass


class DummyBackend(AbstractBackend):
    """Null Object"""

    def __call__(self, var, cast=None):
        return

    def all(self, *a, **kw):
        return {}

    def flush(self, *a, **kw):
        return {}


class DefaultBackend(AbstractBackend):
    """system environment backend"""

    def __init__(self, namespace, **kw):
        super(DefaultBackend, self).__init__(namespace=namespace, **kw)

        self.client = _Env(**kw)
        self.namespace = self.namespace and namespace.upper() or ''

        if not self.namespace:
            self.prefix = ''
        else:
            self.prefix = self.namespace + '_'

        self.tmpl = self.prefix + '{}'

        # patching schema
        self.schema = dict([(self.tmpl.format(k), v) for k, v in self.client.schema.items()])

    def __call__(self, var, *a, **kw):
        var = var.replace('-', '_').upper()
        return self.client.__call__(self.tmpl.format(var), **kw)

    def all(self, *args, **kw):
        """ list all environment variables in the namespace"""
        return dict([(k, v) for k, v in os.environ.items() if k.startswith(self.prefix)])

    def flush(self, *a, **kw):
        return self.client.read_envfile(*a, **kw)
