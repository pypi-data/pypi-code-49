# -*- coding: utf-8 -*-
# This module should be the same as utils.py from CMFPlone,
# except that we override one function.  So we start with importing everything.
from Products.CMFPlone.utils import *

try:
    from html import escape
except ImportError:
    from cgi import escape


orig_pretty_title_or_id = pretty_title_or_id


def pretty_title_or_id(*args, **kwargs):
    result = orig_pretty_title_or_id(*args, **kwargs)
    return escape(result)
