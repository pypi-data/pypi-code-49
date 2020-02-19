#
# Copyright (c) 2007 Zope Foundation and Contributors.
# Copyright (c) 2015-2020 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_utils.testing module

This module provides small testing helpers.
"""

import lxml.etree
import lxml.html

__docformat__ = 'restructuredtext'


def render_xpath(view, xpath='.'):
    """Render only an XPath selection of a full HTML code

    >>> from pyams_utils.testing import render_xpath
    >>> class View:
    ...     def __call__(self):
    ...         return '''<div><div class="row"><p>Row 1</p></div> \
                          <div class="row"><p>Row 2</p></div></div>'''
    >>> view = View()
    >>> render_xpath(view, './/div[2][@class="row"]')
    '<div class="row">\\n  <p>Row 2</p>\\n</div>\\n'
    """
    method = getattr(view, 'render', None)
    if method is None:
        method = view.__call__

    string = method()
    if string == "":
        return string

    try:
        root = lxml.etree.fromstring(string)
    except lxml.etree.XMLSyntaxError:
        root = lxml.html.fromstring(string)

    output = ""
    for node in root.xpath(
        xpath, namespaces={'xmlns': 'http://www.w3.org/1999/xhtml'}):
        s = lxml.etree.tounicode(node, pretty_print=True)
        s = s.replace(' xmlns="http://www.w3.org/1999/xhtml"', ' ')
        output += s

    if not output:
        raise ValueError("No elements matched by %s." % repr(xpath))

    # let's get rid of blank lines
    output = output.replace('\n\n', '\n')

    # self-closing tags are more readable with a space before the
    # end-of-tag marker
    output = output.replace('"/>', '" />')

    return output


def format_html(input):
    """Render formatted HTML code by removing empty lines and spaces ending lines

    >>> from pyams_utils.testing import format_html
    >>> format_html('''<div>      \\n<b>This is a test</b>    \\n\\n</div>    ''')
    '<div>\\n<b>This is a test</b>\\n</div>'
    """
    return '\n'.join(filter(bool, map(str.rstrip, input.split('\n'))))
