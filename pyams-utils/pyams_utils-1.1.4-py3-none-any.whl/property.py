#
# Copyright (c) 2008-2015 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_utils.property module

This module is used to define:
 - a cached property; this read-only property is evaluated only once; it's value is stored into
   object's attributes, and so should be freed with the object (so it should behave like a
   Pyramid's "reify" decorator, but we have kept it for compatibility of existing code)
 - a class property; this decorator is working like a classic property, but can be assigned to a
   class; to support class properties, this class also have to decorated with the
   "classproperty_support" decorator

    >>> from pyams_utils.property import cached_property

    >>> class ClassWithCache:
    ...     '''Class with cache'''
    ...     @cached_property
    ...     def cached_value(self):
    ...         print("This is a cached value")
    ...         return 1

    >>> obj = ClassWithCache()
    >>> obj.cached_value
    This is a cached value
    1

On following calls, cached property method shouldn't be called again:

    >>> obj.cached_value
    1

Class properties are used to define properties on class level:

    >>> from pyams_utils.property import classproperty, classproperty_support

    >>> @classproperty_support
    ... class ClassWithProperties:
    ...     '''Class with class properties'''
    ...
    ...     class_attribute = 1
    ...
    ...     @classproperty
    ...     def my_class_property(cls):
    ...         return cls.class_attribute

    >>> ClassWithProperties.my_class_property
    1
"""

__docformat__ = 'restructuredtext'


class cached_property:  # pylint: disable=invalid-name
    """A read-only property decorator that is only evaluated once.

    The value is cached on the object itself rather than the function or class; this should prevent
    memory leakage.
    """
    def __init__(self, fget, doc=None):
        self.fget = fget
        self.__doc__ = doc or fget.__doc__
        self.__name__ = fget.__name__
        self.__module__ = fget.__module__

    def __get__(self, obj, cls):
        if obj is None:
            return self
        obj.__dict__[self.__name__] = result = self.fget(obj)
        return result


class classproperty:  # pylint: disable=invalid-name
    """Same decorator as property(), but passes obj.__class__ instead of obj to fget/fset/fdel.

    Original code for property emulation:
    https://docs.python.org/3.5/howto/descriptor.html#properties
    """
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("Unreadable attribute")
        return self.fget(obj.__class__)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("Can't set attribute")
        self.fset(obj.__class__, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("Can't delete attribute")
        self.fdel(obj.__class__)

    def getter(self, fget):
        """Property getter"""
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        """Property setter"""
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        """Property deleter"""
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


def classproperty_support(cls):
    """Class decorator to add metaclass to a class.

    Metaclass uses to add descriptors to class attributes
    """
    class Meta(type):
        """Meta class"""

    for name, obj in vars(cls).items():
        if isinstance(obj, classproperty):
            setattr(Meta, name, property(obj.fget, obj.fset, obj.fdel))

    class Wrapper(cls, metaclass=Meta):
        """Wrapper class"""
    return Wrapper
