#
# Copyright (c) 2008-2018 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_utils.factory module

This module provides a decorator and a small set of functions to handle object factories.

Instead of directly using a class as an object factory, the object of this module is to
let you create an object based on an interface. The first step is to create an object
implementing this interface, and then to register it as a factory:

.. code-block:: python

    @implementer(IMyInterface)
    class MyClass(object):
        '''Class implementing my interface'''

    register_factory(IMyInterface, MyClass)

Factory registry can also be handle by a decorator called "factory_config":

.. code-block:: python

    @factory_config(IMyInterface)
    class MyClass(object):
        '''Class implementing my interface'''

A class declared as factory for a specific interface automatically implements the given interface.
You can also provide a tuple or set of interfaces in "factory_config()" decorator.

When a factory is registered, you can look for a factory:

.. code-block:: python

    factory = get_object_factory(IMyInterface)
    if factory is not None:
        myobject = factory()
    else:
        myobject = MyDefaultImplementation()

By registering their own objects factories, extension packages can easily provide their
own implementation of any PyAMS interface handled by factories.
"""

import logging

import venusian
from zope.component import adapter
from zope.interface import Interface, classImplements, implementer
from zope.interface.interface import InterfaceClass

from pyams_utils.interfaces import IObjectFactory
from pyams_utils.registry import get_global_registry


__docformat__ = 'restructuredtext'


LOGGER = logging.getLogger('PyAMS (utils)')


def is_interface(obj):
    """Check if given object is an interface"""
    return issubclass(obj.__class__, InterfaceClass)


def get_interface_name(iface):
    """Get interface full name"""
    return iface.__module__ + '.' + iface.__name__


@adapter(Interface)
@implementer(IObjectFactory)
class ObjectFactoryAdapter:
    """Most basic object factory adapter"""

    factory = None

    def __init__(self, context):
        self.context = context

    def __call__(self, *args, **kwargs):
        return self.factory(*args, **kwargs)  # pylint: disable=not-callable


def register_factory(interface, klass, registry=None, name=''):
    """Register factory for a given interface

    :param interface: the interface for which the factory is registered
    :param klass: the object factory
    :param registry: the registry into which factory adapter should be registered; if None, the
        global registry is used
    :param name: custom name given to registered factory
    """

    class Temp(ObjectFactoryAdapter):
        """Object factory matching given interface"""
        classImplements(klass, interface)
        factory = klass

    if_name = get_interface_name(interface)
    if name:
        if_name = '{0}::{1}'.format(if_name, name)
    if registry is None:
        registry = get_global_registry()
    registry.registerAdapter(Temp, name=if_name)


class factory_config:  # pylint: disable=invalid-name,no-member
    """Class decorator to declare a default object factory"""

    venusian = venusian

    def __init__(self, provided, **settings):
        settings['provided'] = provided
        self.__dict__.update(settings)

    def __call__(self, wrapped):
        settings = self.__dict__.copy()
        depth = settings.pop('_depth', 0)

        def callback(context, name, obj):
            factory_name = settings.get('name', '')
            provided = settings.get('provided')
            if not provided:
                raise TypeError("No provided interface(s) was given for registered factory %r" %
                                obj)
            if not isinstance(provided, tuple):
                provided = (provided,)

            config = context.config.with_package(info.module)  # pylint: disable=no-member
            for interface in provided:
                if name:
                    LOGGER.debug("Registering factory %s for interface %s with name %s",
                                 str(obj), str(interface), factory_name)
                else:
                    LOGGER.debug("Registering default factory %s for interface %s",
                                 str(obj), str(interface))
                register_factory(interface, obj, config.registry, factory_name)

        info = self.venusian.attach(wrapped, callback, category='pyams_factory', depth=depth + 1)
        if info.scope == 'class':  # pylint: disable=no-member
            # if the decorator was attached to a method in a class, or
            # otherwise executed at class scope, we need to set an
            # 'attr' into the settings if one isn't already in there
            if settings.get('attr') is None:
                settings['attr'] = wrapped.__name__

        settings['_info'] = info.codeinfo  # pylint: disable=no-member
        return wrapped


def get_object_factory(interface, registry=None, name=''):
    """Get registered factory for given interface

    :param interface: the interface for which a factory is requested
    :param registry: the registry into which registered factory should be looked for
    :param name: name of requested factory
    :return: the requested object factory, or None if it can't be found
    """
    if_name = get_interface_name(interface)
    if name:
        if_name = '{0}::{1}'.format(if_name, name)
    if registry is None:
        registry = get_global_registry()
    return registry.queryAdapter(interface, IObjectFactory, name=if_name)
