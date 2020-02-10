# Copyright (C) 2003-2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: __init__.py,v 1.1 2019/04/22 05:55:55 dieter Exp $
'''Query evaluation.

Put into its own module to avoid cyclic module imports.
'''
# need this early due to recursive imports
_notPassed = object()

from BTrees.IIBTree import IISet

from zope.interface import Interface, implementer

from Products.ZCatalog.Lazy import LazyCat, LazyMap

from ..sorting import sort as _sort, normSortSpecs as _normSortSpecs

from .interfaces import IQueryContext
from .adapter import getSubscriptionAdapter


def _eval(query, cat, restricted, **kw):
  '''evaluate *query* in the context of *cat* (a 'Products.ZCatalog.ZCatalog.ZCatalog').'''
  return getSubscriptionAdapter(cat, IQueryContext).eval(query, restricted, **kw)


def eval(catalog, query, sortSpecs=(), withSortValues=_notPassed, restricted=False, **kw):
  '''evaluate *query* for *catalog*; sort according to *sortSpecs*.

  *sortSpecs* is a sequence of sort specifications.
  
  A sort spec is either a ranking spec, an index name or a pair
  index name + sort direction ('asc/desc').

  If *withSortValues* is not passed, it is set to 'True' when *sortSpecs*
  contains a ranking spec; otherwise, it is set to 'False'.

  If *withSortValues*, the catalog brains 'data_record_score_' is
  abused to communicate the sort value (a tuple with one
  component per sort spec). 'data_record_normalized_score_' is
  set to 'None' in this case.
  '''
  rs = _eval(query, catalog, restricted, **kw)
  kw["restricted"] = restricted
  if not rs: return LazyCat(())
  sortSpecs, withSortValues = _normSortSpecs(
    sortSpecs, withSortValues, catalog, kw)
  if sortSpecs or withSortValues: rs = _sort(rs, sortSpecs, withSortValues)
  if hasattr(rs, 'keys'): rs= rs.keys() # a TreeSet lacks '__getitem__'
  return LazyMap(catalog._catalog.__getitem__, rs)
