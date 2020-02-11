# -*- coding: utf-8 -*-
try:
    # plone.app.layout 3.1.0 and 3.1.1
    from plone.app.layout.navigation.navtree import NavTreeProvider as Base
except ImportError:
    # plone.app.layout 3.1.2+
    from plone.app.layout.viewlets.common import GlobalSectionsViewlet as Base

try:
    from html import escape
except ImportError:
    from cgi import escape


if hasattr(Base, "render_item"):
    Base._orig_render_item = Base.render_item

    def render_item(self, item, path):
        if "title" in item:
            item["title"] = escape(item["title"])
        if "name" in item:
            item["name"] = escape(item["name"])
        return self._orig_render_item(item, path)

    Base.render_item = render_item
