# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: filter_.py,v 1.1 2019/04/22 05:55:58 dieter Exp $
from zope.interface import implementer, Interface
from zope.component import adapter

from BTrees.OOBTree import OOSet, intersection, difference

from Products.PluginIndexes.interfaces import IPluggableIndex

from .....AdvancedQuery import Or, Filter
from ....interfaces import IFilterIndex, IIndexedValue, IMultiplicityAware, \
     ITermValueMatch, IKeyNormalizingIndex
from ... import conditional_adapter, \
     querySubscriptionAdapter, getSubscriptionAdapter, \
     Adaptable
from .. import normalize_spec, QueryCheck, match_glob, match_regexp


class CheckFilterQuery(QueryCheck):
  SUPPORTED = frozenset(("and", "or", "not", "range", "glob", "regexp"))

filterable = CheckFilterQuery()


@conditional_adapter(Adaptable(IIndexedValue, IMultiplicityAware))
@adapter(IPluggableIndex)
@implementer(IFilterIndex)
class FilterIndex(object):
  def __init__(self, index): self.index = index

  def make_filter(self, q):
    if not filterable(q): return
    spec = normalize_spec(q.make_spec())
    index = self.index
    special = querySubscriptionAdapter(index, ITermValueMatch)
    normalize = querySubscriptionAdapter(index, IKeyNormalizingIndex)
    keys = OOSet(spec.get("keys", ())); not_ = OOSet(spec.get("not", ()))
    if not keys and not not_: return Or()
    if normalize is not None:
      keys = OOSet(map(normalize.normalize_key, keys))
      not_ = OOSet(map(normalize.normalize_key, not_))
    ma = getSubscriptionAdapter(index, IMultiplicityAware)
    multi_valued = ma.multi_valued()
    single_key_indexed = special is None and not multi_valued
    if multi_valued:
      def combine(indexed_value, check): return any(map(check, indexed_value))
      def filter(indexed_value, key): return key in indexed_value
    else:
      def combine(indexed_value, check): return check(indexed_value)
      def filter(indexed_value, key): return key == indexed_value
    if special is not None:
      for unsupported in ("range", "match"):
        if spec.get(unsupported): return
      filter = special.match
    conds = [] # sequence of "indexed_value --> bool" functions to be anded
    # handle `range`, `match`; `op` == "or"` in this case
    range = spec.get("range"); match = spec.get("match"); check = None
    if range or match:
      if range: # no `match` in this case 
        lmin = lmax = None
        if "min" in range: lmin = min(keys)
        if "max" in range: lmax = max(keys)
        if lmin is None and lmax is None: pass # match everything
        else:
          check = \
            (lambda x: lmin <= x) if lmax is None else \
            (lambda x: x <= lmax) if lmin is None else \
            (lambda x: lmin <= x <= lmax)
      else: # match
        if not keys: return Or()
        matcher = dict(glob=match_glob, regexp=match_regexp)[match]
        matcher = list(map(matcher, keys))
        check = lambda x, matcher=matcher: any(m(x) for m in matcher)
      if check:
        conds.append(lambda indexed_value: combine(indexed_value, check))
    else: # explicit keys
      op = spec.get("operator", "or")
      if not keys: # "pure not"
        op = "and"
      if op == "and":
        if (single_key_indexed and len(keys) > 1) or intersection(keys, not_):
          return Or()
      else: # op == "or"
        keys = difference(keys, not_)
        if not keys: return Or()
        if single_key_indexed: not_ = OOSet()
      # ensure closed `lambfa`s below (to avoid name clashed)
      if op == "and":
        if keys:
          conds.append(lambda iv, filter=filter, keys=keys: all(filter(iv, k) for k in keys))
      else: # `op == "or"`
        conds.append(lambda iv, filter=filter, keys=keys: any(filter(iv, k) for k in keys))
    if not_:
      conds.append(lambda iv, filter=filter, nots=not_: all(not filter(iv, k) for k in not_))
    if not conds: filter = lambda iv: True
    if len(conds) == 1: filter = conds[0]
    else: filter = lambda iv: all(c(iv) for c in conds)
    return Filter(index.id, filter)
