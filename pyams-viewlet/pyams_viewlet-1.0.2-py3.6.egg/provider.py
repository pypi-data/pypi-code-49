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

"""PyAMS_viewlet.provider module

This module provides the "provider:" TALES expression, which allows inclusion of any registered
content provider into a Chameleon or ZPT template.
"""

import re

from chameleon.astutil import Symbol
from chameleon.tales import StringExpr
from zope.contentprovider.interfaces import BeforeUpdateEvent, ContentProviderLookupError, \
    IContentProvider
from zope.contentprovider.tales import addTALNamespaceData
from zope.location.interfaces import ILocation

from pyams_utils.tales import ContextExprMixin


__docformat__ = 'restructuredtext'


FUNCTION_EXPRESSION = re.compile(r'(.+)\((.+)\)', re.MULTILINE | re.DOTALL)
ARGUMENTS_EXPRESSION = re.compile(r'[^(,)]+')

CONTENT_PROVIDER_NAME = re.compile(r'([A-Za-z0-9_\-\.]+)')


def render_content_provider(econtext, name):
    """TALES provider: content provider

    This TALES expression is used to render a registered "content provider", which
    is an adapter providing IContentProvider interface; adapter lookup is based on
    current context, request and view.

    The requested provider can be called with our without arguments, like in
    ${structure:provider:my_provider} or ${structure:provider:my_provider(arg1, arg2)}.
    In the second form, arguments will be passed to the "update" method; arguments can be
    static (like strings or integers), or can be variables defined into current template
    context; other Python expressions including computations or functions calls are actually
    not supported, but dotted syntax is supported to access inner attributes of variables.

    Provider arguments can be passed by position but can also be passed by name, using classic
    syntax as in ${structure:provider:my_provider(arg1, arg3=var3)}
    """

    def get_value(econtext, arg):
        """Extract argument value from context

        Extension expression language is quite simple. Values can be given as
        positioned strings, integers or named arguments of the same types.
        """
        arg = arg.strip()
        if arg.startswith('"') or arg.startswith("'"):
            # may be a quoted string...
            return arg[1:-1]
        if '=' in arg:
            key, value = arg.split('=', 1)
            value = get_value(econtext, value)
            return {key.strip(): value}
        try:
            arg = int(arg)  # check integer value
        except ValueError:
            args = arg.split('.')
            result = econtext.get(args.pop(0))
            for arg in args:  # pylint: disable=redefined-argument-from-local
                result = getattr(result, arg)
            return result
        else:
            return arg

    name = name.strip()
    context = econtext.get('context')
    request = econtext.get('request')
    view = econtext.get('view')

    args, kwargs = [], {}
    func_match = FUNCTION_EXPRESSION.match(name)
    if func_match:
        name, arguments = func_match.groups()
        for arg in map(lambda x: get_value(econtext, x), ARGUMENTS_EXPRESSION.findall(arguments)):
            if isinstance(arg, dict):
                kwargs.update(arg)
            else:
                args.append(arg)
    else:
        match = CONTENT_PROVIDER_NAME.match(name)
        if match:
            name = match.groups()[0]
        else:
            raise ContentProviderLookupError(name)

    registry = request.registry
    provider = registry.queryMultiAdapter((context, request, view), IContentProvider, name=name)

    # raise an exception if the provider was not found.
    if provider is None:
        raise ContentProviderLookupError(name)

    # add the __name__ attribute if it implements ILocation
    if ILocation.providedBy(provider):
        provider.__name__ = name

    # Insert the data gotten from the context
    addTALNamespaceData(provider, econtext)

    # Stage 1: Do the state update
    registry.notify(BeforeUpdateEvent(provider, request))
    provider.update(*args, **kwargs)

    # Stage 2: Render the HTML content
    return provider.render()


class ProviderExpr(ContextExprMixin, StringExpr):
    """provider: TALES expression"""

    transform = Symbol(render_content_provider)
