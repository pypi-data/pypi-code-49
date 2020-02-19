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

"""PyAMS_viewlet.metadirectives module

This template provides definition of ZCML directives.
"""

from zope.configuration.fields import GlobalInterface, GlobalObject
from zope.interface import Interface
from zope.schema import TextLine

from pyams_viewlet.interfaces import IViewletManager


__docformat__ = 'restructuredtext'


class IContentProvider(Interface):
    """A directive to register a simple content provider.

    Content providers are registered by their context (`for` attribute), the
    request (`layer` attribute) and the view (`view` attribute). They also
    must provide a name, so that they can be found using the TALES
    ``provider`` namespace. Other than that, content providers are just like
    any other views.
    """

    view = GlobalObject(title="The view the content provider is registered for",
                        description="The view can either be an interface or a class. By "
                                    "default the provider is registered for all views, "
                                    "the most common case.",
                        required=False,
                        default=Interface)

    name = TextLine(title="The name of the content provider",
                    description="The name of the content provider is used in the TALES "
                                "``provider`` namespace to look up the content "
                                "provider.",
                    required=True)

    for_ = GlobalObject(title="The interface or class this view is for",
                        required=False)

    permission = TextLine(title="Permission",
                          description="The permission needed to use the view",
                          required=False)

    class_ = GlobalObject(title="Class",
                          description="A class that provides attributes used by the view",
                          required=False)

    layer = GlobalInterface(title="The layer the view is in",
                            description="A skin is composed of layers; layers are defined as "
                                        "interfaces, which are provided to the request when the "
                                        "skin is applied. It is common to put skin "
                                        "specific views in a layer named after the skin. If the "
                                        "'layer' attribute is not supplied, it defaults to "
                                        "IRequest, which is the base interface of any request.",
                            required=False)


class IViewletManagerDirective(IContentProvider):
    """A directive to register a new viewlet manager.

    Viewlet manager registrations are very similar to content provider
    registrations, since they are just a simple extension of content
    providers. However, viewlet managers commonly have a specific provided
    interface, which is used to discriminate the viewlets they are providing.
    """

    provides = GlobalInterface(title="The interface this viewlet manager provides",
                               description="A viewlet manager can provide an interface, which "
                                           "is used to lookup its contained viewlets.",
                               required=False,
                               default=IViewletManager)


class IViewletDirective(IContentProvider):
    """A directive to register a new viewlet.

    Viewlets are content providers that can only be displayed inside a viewlet
    manager. Thus they are additionally discriminated by the manager. Viewlets
    can rely on the specified viewlet manager interface to provide their
    content.

    The viewlet directive also supports an undefined set of keyword arguments
    that are set as attributes on the viewlet after creation. Those attributes
    can then be used to implement sorting and filtering, for example.
    """

    manager = GlobalObject(title="Manager",
                           description="The interface or class of the viewlet manager",
                           required=False,
                           default=IViewletManager)


# Arbitrary keys and values are allowed to be passed to the viewlet.
# pylint: disable=no-value-for-parameter
IViewletDirective.setTaggedValue('keyword_arguments', True)
