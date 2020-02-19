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

"""PyAMS_viewlet.metaconfigure module

This module provides ZCML directives handlers.
"""

from pyramid.exceptions import ConfigurationError
from pyramid.interfaces import IRequest, IView
from zope.component import zcml
from zope.component.interface import provideInterface
from zope.interface import Interface, classImplements

from pyams_viewlet.interfaces import IViewlet, IViewletManager
from pyams_viewlet.manager import ViewletManager, ViewletManagerFactory


__docformat__ = 'restructuredtext'


def ViewletManagerDirective(_context, name,
                            context=Interface,
                            layer=IRequest,
                            view=IView,
                            provides=IViewletManager,
                            class_=None,
                            permission=None):
    # pylint: disable=invalid-name,too-many-arguments
    """Viewlet manager ZCML directive"""

    # If class is not given we use the basic viewlet manager.
    if class_ is None:
        class_ = ViewletManager

    # Create a new class based on the class.
    cdict = {'permission': permission}
    new_class = ViewletManagerFactory(name, provides, bases=(class_,), cdict=cdict)

    # Register interfaces
    _handle_for(_context, context)
    zcml.interface(_context, view)

    # Create a checker for the viewlet manager
    # checker.defineChecker(new_class, checker.Checker(required))

    # register a viewlet manager
    _context.action(discriminator=('viewletManager', context, layer, view, name),
                    callable=zcml.handler,
                    args=('registerAdapter', new_class,
                          (context, layer, view),
                          provides, name, _context.info))


def ViewletDirective(_context, name, class_,
                     context=Interface,
                     layer=IRequest,
                     view=IView,
                     manager=IViewletManager,
                     attribute='render',
                     permission=None,
                     **kwargs):
    # pylint: disable=invalid-name,too-many-arguments
    """Viewlet ZCML directive"""

    # Make sure the has the right form, if specified.
    if attribute != 'render':
        if not hasattr(class_, attribute):
            raise ConfigurationError("The provided class doesn't have the specified attribute")

    cdict = {
        '__name__': name,
        '__page_attribute__': attribute,
        'permission': permission
    }
    cdict.update(kwargs)
    new_class = type(class_.__name__, (class_,), cdict)

    classImplements(new_class, IViewlet)

    # Register the interfaces.
    _handle_for(_context, context)
    zcml.interface(_context, view)

    # register viewlet
    _context.action(discriminator=('viewlet', context, layer, view, manager, name),
                    callable=zcml.handler,
                    args=('registerAdapter', new_class,
                          (context, layer, view, manager),
                          IViewlet, name, _context.info))


def _handle_for(_context, for_):
    if for_ is not None:
        _context.action(discriminator=None,
                        callable=provideInterface,
                        args=('', for_))
