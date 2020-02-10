# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: __init__.py,v 1.1 2019/04/22 05:55:58 dieter Exp $
from itertools import chain

from zope.interface import implementer
from zope.component import adapter

from Products.PluginIndexes.interfaces import IQueryIndex
from Products.ZCatalog.query import IndexQuery

from .....AdvancedQuery import Generic, Eq, Le, Ge, In, And, Or, Not, \
     MatchGlob, MatchRegexp, Between, \
     _TermQuery, _BaseQuery, _CombiningQuery
from .....tree import unfold
from ....interfaces import \
     IFilterIndex, IQueryOptimizerChain, IQueryNodeOptimizer

from ....transform import OptimizerChain
from ... import queryMultiSubscriptionAdapter, querySubscriptionAdapter
from .. import normalize_spec


@implementer(IQueryNodeOptimizer)
class QueryNodeOptimizer(object):
  """they all adapt a query."""

  def __init__(self, query): pass


class IndexBasedQueryOptimizer(QueryNodeOptimizer):
  """they adapt an `_IndexBasedQuery`.

  They give the index the possibility to override
  a generic optimization implemented by `_optimize`.

  The index' `optimize` can return `None` to indicate
  that it decided not to transform the query.
  """
  def optimize(self, q, context):
    # see whether the index provides a special optimization
    idx = context.get_index(q.index)
    idx_a = self._get_index_optimizer(idx, q)
    if idx_a is not None:
      r = idx_a.optimize(q, context)
      if r is None: return True # index decided not to transform
      if r is not True and r is not q: return r # index transformed
    # delegate to `_optimize`
    return self._optimize(idx, q, context)

  def _get_index_optimizer(self, idx, q):
    """return index specific optimizer or `None`."""
    return queryMultiSubscriptionAdapter((idx, q), IQueryNodeOptimizer)


##############################################################################
## 0 -- `Generic` conversion

@adapter(Generic)
class ConvertGeneric(IndexBasedQueryOptimizer):
  """check `Generic` queries for sanity and potentially convert them.

  The conversion has the task to make it easy for indexes to
  optimize specific queries.
  """
  order = 0

  def _optimize(self, idx, q, context):
    t = normalize_spec(q.make_spec())
    op = t.get("operator", "or"); keys = t["keys"]
    # check sanity
    #   We cannot handle the combinations of `and` with a computed query
    #   (because we cannot determine all keys, only those for
    #   which there are indexed objects)
    if op == "and" and (t.get("range") or t.get("match")):
      raise ValueError("cannot combine `and` with `range` or `match`", q)
    #  We cannot handle both "range" and "match"
    if t.get("range") and t.get("match"):
      raise ValueError("cannot have both `match` and `range`", q)
    # check that we understand everything
    for k in t.keys():
      if k not in ("keys", "operator", "range", "match"): return True
    if op not in ("or", "and"): return True
    if op == "and" and len(keys) != 1: return True
    filter = q.filter
    range = t.get("range", "")
    if range:
      with_min = "min" in range; with_max = "max" in range
      if with_min and with_max:
        return Between(q.index, min(keys), max(keys), filter)
      elif with_min:
        return Ge(q.index, min(keys), filter)
      elif with_max:
        return Le(q.index, max(keys), filter)
    match = t.get("match", "")
    if match:
      if len(keys) != 1: return True
      if match == "glob": qc = MatchGlob
      elif match == "regexp": qc = MatchRegexp
      else: return True
      return qc(q.index, keys[0], filter)
    tq, term = (Eq, keys[0]) if len(keys) == 1 else (In, keys)
    return tq(q.index, term, filter)


##############################################################################
## 10 -- eliminate `filter = True`

@adapter(_TermQuery)
class HandleFilterTrue(IndexBasedQueryOptimizer):
  """Convert into an explicite `Filter` query or set `filter` to `False`"""

  order = 10

  def _optimize(self, idx, q, context):
    if not getattr(q, "filter", False): return True
    fa = querySubscriptionAdapter(idx, IFilterIndex)
    if fa is not None:
      filter = fa.make_filter(q)
      if filter is not None: return filter
    q = q._clone()
    q.filter = False
    return q


##############################################################################
## 20 -- unfold nested queries
@adapter(_CombiningQuery)
class Unfold(QueryNodeOptimizer):

  order = 20

  def unfold(self, q, complement={And:Or, Or:And, Not:Not}):
    return unfold(q, complement)

  def optimize(self, q, context):
   oq = self.unfold(q)
   return True if oq is q else oq
    


##############################################################################
## the chain

@adapter(_BaseQuery)
@implementer(IQueryOptimizerChain)
class QueryOptimizerChain(OptimizerChain):
  sub_tspec = IQueryNodeOptimizer
