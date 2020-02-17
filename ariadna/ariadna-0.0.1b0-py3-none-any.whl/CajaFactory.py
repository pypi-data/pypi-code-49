import inspect
import importlib
import collections.abc
from operator import itemgetter

class CajaFactory(type):

    traits_cache = {}
    exceptions = frozenset([str, range])

    def __call__(cls, content=None, *args, **kwds):
        from .Caja import Caja # cached
        if cls is Caja:
            return CajaFactory.wrapper_type(content)(content, *args, **kwds)
        return type.__call__(cls, content, *args, **kwds)

    @staticmethod
    def import_cajas() -> frozenset:
        mod = importlib.import_module('ariadna')
        return frozenset([getattr(mod, name) for name in mod.__cajas__])

    @staticmethod
    def import_default_caja() -> frozenset:
        mod = importlib.import_module('ariadna')
        return mod.__DEFAULT_NONE_CAJA__

    @staticmethod
    def trait_filters(klass) -> frozenset:
        k = CajaFactory
        if klass not in k.traits_cache.keys():
            tfilter = lambda member: inspect.isclass(member) \
                                 and inspect.isclass(member) \
                                 and issubclass(member, collections.abc.Collection) \
                                 and issubclass(klass, member)
            k.traits_cache[klass] = frozenset(map(itemgetter(1),inspect.getmembers(collections.abc, tfilter)))
        return k.traits_cache[klass]

    @staticmethod
    def trait_match(traits1, traits2) -> bool:
        return traits1 == traits2

    @staticmethod
    def wrapper_type(content):
        k = CajaFactory
        if type(content) not in k.exceptions:
            if content is None:
                return k.import_default_caja()
            caja_classes = k.import_cajas()
            content_traits = k.trait_filters(type(content))
            for caja_class in caja_classes:
                if k.trait_match(k.trait_filters(caja_class), content_traits):
                    return caja_class
        raise TypeError(f'CajaFactory does not know how to wrap content type {type(content)}')
