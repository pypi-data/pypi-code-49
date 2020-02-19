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

"""PyAMS_utils.cache module

This module provides a small set of adapters which can be used to provide a "cache key" value
to any kind of object.

The goal of such a cache key value is to provide a string representation, as stable as possible,
of a given object; this string can be used as a cache key, but also to define an object ID inside
an HTML page.
A TALES helper extension is also provided to get an object's cache key from a Chameleon template.
"""

from persistent.interfaces import IPersistent
from zope.interface import Interface

from pyams_utils.adapter import ContextRequestViewAdapter, adapter_config
from pyams_utils.interfaces import ICacheKeyValue
from pyams_utils.interfaces.tales import ITALESExtension


__docformat__ = 'restructuredtext'


@adapter_config(context=object, provides=ICacheKeyValue)
def object_cache_key_adapter(obj):
    """Cache key adapter for any object

    >>> from pyramid.testing import setUp, tearDown
    >>> config = setUp()

    >>> from pyams_utils.interfaces import ICacheKeyValue
    >>> from pyams_utils.cache import object_cache_key_adapter
    >>> config.registry.registerAdapter(object_cache_key_adapter, (object, ), ICacheKeyValue)

    >>> value = object()
    >>> key = ICacheKeyValue(value)
    >>> key == str(id(value))
    True

    >>> tearDown()
    """
    return str(id(obj))


@adapter_config(context=str, provides=ICacheKeyValue)
def string_cache_key_adapter(obj):
    """Cache key adapter for string value

    >>> from pyramid.testing import setUp, tearDown
    >>> config = setUp()

    >>> from pyams_utils.interfaces import ICacheKeyValue
    >>> from pyams_utils.cache import string_cache_key_adapter
    >>> config.registry.registerAdapter(string_cache_key_adapter, (str, ), ICacheKeyValue)

    >>> value = 'my test string'
    >>> key = ICacheKeyValue(value)
    >>> key == value
    True

    >>> tearDown()
    """
    return obj


@adapter_config(context=IPersistent, provides=ICacheKeyValue)
def persistent_cache_key_adapter(obj):
    """Cache key adapter for persistent object"""
    # pylint: disable=protected-access
    if obj._p_oid:
        return str(int.from_bytes(obj._p_oid, byteorder='big'))
    return str(id(obj))


@adapter_config(name='cache_key', context=(Interface, Interface, Interface),
                provides=ITALESExtension)
class CacheKeyTalesExtension(ContextRequestViewAdapter):
    """extension:cache_key(context) TALES extension

    A PyAMS TALES extension which allows to render cache key value for a given context.
    """

    def render(self, context=None):
        """Rendering of TALES extension"""
        if context is None:
            context = self.request.context
        return ICacheKeyValue(context)
