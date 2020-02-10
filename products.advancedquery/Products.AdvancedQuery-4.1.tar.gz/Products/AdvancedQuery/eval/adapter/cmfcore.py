# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: cmfcore.py,v 1.1 2019/04/22 05:55:56 dieter Exp $
"""(Subscription) adapters for `Products.CMFCore.CatalogTool.CatalogTool`."""
from zope.interface import implementer
from zope.component import adapter

from Products.CMFCore.CatalogTool import CatalogTool, processQueue, \
     getSecurityManager, processQueue, \
     _checkPermission, AccessInactivePortalContent, DateTime


from ..interfaces import IQueryRestrict
from ..context import QueryContext
from . import conditional_adapter, SafeInheritance


@adapter(CatalogTool)
class QueryContext(QueryContext):
  def eval(self, *args, **kw):
    processQueue()
    return super(QueryContext, self).eval(*args, **kw)


@conditional_adapter(SafeInheritance(CatalogTool, "__call__"))
@adapter(CatalogTool)
@implementer(IQueryRestrict)
class QueryRestrict(object):
  def __init__(self, catalog): self.catalog = catalog

  def restrict(self, q, **kw):
    cat = self.catalog
    q = q & In("allowedRolesAndUsers", cat._listAllowedRolesAndUsers(
      getSecurityManager().getUser()))
    if not _checkPermission(AccessInactivePortalContent, cat):
      now = DateTime()
      q &= Ge(expires, now) & Le(effective, now)
    return q
