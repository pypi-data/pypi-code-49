# -*- coding: utf-8 -*-
from . import utils

import json

try:
    from html import escape
except ImportError:
    from cgi import escape

try:
    # plone.app.content 3
    from plone.app.content.browser import contents as fc
except ImportError:
    try:
        # 2.2.x
        from plone.app.content.browser import folder as fc
    except ImportError:
        # 2.1.x and lower do not need this patch
        fc = None


if fc is not None:
    # Patch the utils module that was imported by fc.
    fc.utils = utils

    # Patch ContextInfo
    fc.ContextInfo._orig___call__ = fc.ContextInfo.__call__


    def context_info_call(self):
        result = self._orig___call__()
        data = json.loads(result)
        obj = data.get("object", None)
        if obj is None:
            return result
        orig_title = obj.get("Title", None)
        if not orig_title:
            return result
        escaped_title = escape(orig_title)
        if escaped_title == orig_title:
            return result
        obj["Title"] = escaped_title
        result = json.dumps(data)
        return result


    fc.ContextInfo.__call__ = context_info_call
