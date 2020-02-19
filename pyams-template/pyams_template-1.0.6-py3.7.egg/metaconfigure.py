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

"""PyAMS_template.metadirectives module

Is module allows to handle <template /> and <layout > directives in ZCML files.
"""

import os

from pyramid.exceptions import ConfigurationError
from pyramid.interfaces import IRequest
from zope.component import zcml
from zope.interface import Interface, directlyProvides

from pyams_template.interfaces import IContentTemplate, ILayoutTemplate
from pyams_template.template import TemplateFactory


__docformat__ = 'restructuredtext'


def template_directive(_context, template, name='',
                       for_=Interface,
                       layer=IRequest,
                       provides=IContentTemplate,
                       content_type='text/html',
                       macro=None,
                       context=None):
    # pylint: disable=too-many-arguments
    """ZCML <template /> directive handler"""
    # Make sure that the template exists
    template = os.path.abspath(str(_context.path(template)))
    if not os.path.isfile(template):
        raise ConfigurationError("No such file", template)

    factory = TemplateFactory(template, content_type, macro)
    directlyProvides(factory, provides)

    for_ = (context, layer, for_)

    # register the template
    zcml.adapter(_context, (factory,), provides, for_, name=name)


def layout_template_directive(_context, template, name='',
                              for_=Interface,
                              layer=IRequest,
                              provides=ILayoutTemplate,
                              content_type='text/html',
                              macro=None,
                              context=None):
    # pylint: disable=too-many-arguments
    """ZCML <layout /> directive handler"""
    template_directive(_context, template, name, for_, layer, provides,
                       content_type, macro, context)
