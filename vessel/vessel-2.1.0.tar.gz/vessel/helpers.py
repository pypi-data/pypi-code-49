

__all__ = ()


def imitate(value, name = None, module = None, doc = None):

    if name:

        value.__name__ = value.__qualname__ = name

    if module:

        value.__module__ = module

    if doc:

        value.__doc__ = doc


def simulate(cls, name = None, module = None, doc = None):

    class meta(type):

        __subclasscheck__ = cls.__subclasscheck__

        __instancecheck__ = cls.__instancecheck__

        __bases__ = (cls,)

    class value(metaclass = meta):

        """.."""

        __slots__ = ()

        def __new__(cls, *args, **kwargs):

            return cls.__bases__[0](*args, **kwargs)

    imitate(value, name = name or cls.__name__, module = module, doc = doc)

    return value
