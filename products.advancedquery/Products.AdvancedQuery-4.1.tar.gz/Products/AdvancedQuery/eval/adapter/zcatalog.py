# Copyright (C) 2019 by Dr. Dieter Maurer, Eichendorffstr. 23, D-66386 St. Ingbert, Germany
#       $Id: zcatalog.py,v 1.1 2019/04/22 05:55:57 dieter Exp $
"""`ZCatalog` (subscription) adapter."""
from zope.interface import implementer
from zope.component import adapter

from Products.ZCatalog.ZCatalog import ZCatalog

from ..interfaces import IQueryContext, IQueryRestrict
from ..context import QueryContext
from . import conditional_adapter, SafeInheritance


# Att: `adapter` modifies its argument; we do not want this here
#QueryContext = adapter(ZCatalog)(QueryContext)
@adapter(ZCatalog)
class QueryContext(QueryContext): pass


@conditional_adapter(SafeInheritance(ZCatalog, "__call__"))
@adapter(ZCatalog)
@implementer(IQueryRestrict)
class Unrestricted(object):
  def __init__(self, catalog): pass
  def restrict(self, q, **kw): return q
