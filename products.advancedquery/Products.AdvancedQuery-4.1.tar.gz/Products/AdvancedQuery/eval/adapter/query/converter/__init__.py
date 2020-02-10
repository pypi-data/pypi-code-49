# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: __init__.py,v 1.1 2019/04/22 05:55:57 dieter Exp $
"""query --> eval tree converter."""
from zope.interface import implementer
from zope.component import adapter, queryMultiAdapter

from BTrees.OOBTree import OOSet, difference, intersection

from Products.PluginIndexes.interfaces import IPluggableIndex, \
     ILimitedResultIndex, IQueryIndex
from Products.PluginIndexes.unindex import UnIndex

from .....AdvancedQuery import Indexed, Filter, \
     Not, And, Or, Generic, LiteralResultSet, \
     _IndexBasedQuery, _CombiningQuery, _ZTermQuery, _TermQuery
from ....lib import InstanceCache, instance_cached
from ....interfaces import IQueryConverter, \
     IIndexed, IKeyedIndex, ILookupIndex, ILookupTreeIndex, \
     IIndexedValue, IMultiplicityAware, ITermValueMatch, \
     IKeyNormalizingIndex
from ....tree import  \
     Set as TSet, IndexLookup as TLookup, Filter as TFilter, \
     Not as TNot, And as TAnd, Or as TOr
from ... import  \
     PositionArgCheck, \
     conditional_adapter, SafeInheritance, Adaptable, \
     getMultiSubscriptionAdapter, \
     querySubscriptionAdapter, getSubscriptionAdapter, \
     ClassBasedCheck, instance_cached

from .. import normalize_spec, QueryCheck, \
     match_glob, match_regexp


@implementer(IQueryConverter)
class QueryConverter(object):
  """they all adapt a query."""
  def __init__(self, query): pass


@adapter(_IndexBasedQuery)
class IndexBasedQueryConverter(QueryConverter):
  """delegate to index."""
  def transform(self, q, context):
    idx = context.get_index(q.index)
    conv = getMultiSubscriptionAdapter((idx, q), IQueryConverter)
    return conv.transform(q, context)



# Auxiliaries for our conditional adapter factories
class CheckArg0(PositionArgCheck): arg_pos = 0
class CheckArg1(PositionArgCheck): arg_pos = 1


class CheckZQuery(InstanceCache):
  """check whether the ZCatalog default can handle the query."""
  @instance_cached
  def __call__(self, *objs):
    idx, q = objs
    if isinstance(q, Generic): return True
    # we assume the index supports "range" when it does not tell otherwise
    options = idx.query_options if IQueryIndex.providedBy(idx) else ("range", )
    # Note: a `match` query will not arrive here (as it is not a `_ZTermQuery`)
    if isinstance(q, _ComputedQuery): return "range" in options

  def _get_cache_key(self, f, args, kw):
    return tuple(a.__class__ for a in args)


#############################################################################
#############################################################################
## Index based queries

@implementer(IQueryConverter)
class IndexQueryConverter(object):
  """Base class for the index, query adapters."""
  def __init__(self, index, query): self.index = index; self.query = query


class QueryCheck(CheckArg1, QueryCheck): pass

class QueryIndexQueryCheck(QueryCheck):
  """QueryCheck for an `IQueryIndex` index."""
  def __call__(self, *objs):
    idx = objs[0]
    supported = set(opt for opt in idx.query_options if opt not in ("query", "operator"))
    if "operator" in idx.query_options: supported |= set(idx.operators)
    return super(QueryIndexQueryCheck, self).__call__(*objs, supported=supported)


#############################################################################
# Base converter for `ZCatalog` supported searches
#  Note: it will only be applied to `IPluggableIndex` indexes
#    Nevertheless, we claim to adapt `None` (i.e. be applicable
#    for any object). We do this in order to let our
#    optimizations (registered for `IPluggableIndex`) be examined
#    before this default.
@conditional_adapter(CheckZQuery())
@adapter(None, _ZTermQuery)
class ZTermQueryConverter(IndexQueryConverter):
  def transform(self, q, context):
    return TLookup(self.index, q.make_spec())



#############################################################################
# Converter for `keyed_index`
keyed_index = Adaptable(IKeyedIndex)

class KeyedIndexQueryCheck(QueryCheck):
  """Check that the query can be handled by our standard `IKeyedIndex` converter."""
  SUPPORTED = frozenset(("and", "or", "glob", "regexp", "not", "range"))

  def __call__(self, *objs):
    # must exclude "pure not" because we can handle it via keys only
    #  for single valued indexes
    return super(KeyedIndexQueryCheck, self).__call__(*objs) \
           and not pure_not_query_check(*objs)

keyed_index_query_check = KeyedIndexQueryCheck()

class SpecConverter(IndexQueryConverter):
  def transform(self, q, context):
    spec = normalize_spec(q.make_spec())
    index = self.index
    normalize = querySubscriptionAdapter(index, IKeyNormalizingIndex)
    normalize = normalize.normalize_key if normalize is not None \
                else lambda key: key
    kil = querySubscriptionAdapter(index, ILookupIndex)
    if kil is not None:
      def lookup(key): return TSet(kil.dids_for_key(key))
    else:
      kil = querySubscriptionAdapter(index, ILookupTreeIndex)
      if kil is not None:
        def lookup(key): return kil.tree_for_key(key, context)
      else:
        def lookup(key): return TLookup(index, (key,))
    keys = spec.get("keys")
    if keys: keys = OOSet(map(normalize, keys))
    not_ = spec.get("not")
    if not_: not_ = OOSet(map(normalize, not_))
    range = spec.get("range")
    match = spec.get("match")
    op = spec.get("operator")
    if op is None: op = getattr(index, "use_operator", "or")
    if range and match:
      raise ValueError("cannot have both `match` and `range`")
    if not keys:
      if range or match:
        raise ValueError("need keys for `match`/`range`")
      if not_: # pure not
        keys, tree = self._handle_pure_not(index, not_, lookup)
        if tree is not None: return tree
    if range or match:
      keys = self._expand_keys(index, keys, range, match)
    if not_:
      keys = difference(keys, not_) if  op == "or" else \
             None if intersection(keys, not_) else keys
    # mirror the behaviour of `ZCatalog` to treat an empty `keys`
    #  as a query without results -- even for `and` (where this
    #  is logically wrong)
    if not keys: return TOr()
    t = (TAnd if op == "and" else TOr)(*(lookup(k) for k in keys))
    if not_:
      special = querySubscriptionAdapter(index, ITermValueMatch)
      ma = querySubscriptionAdapter(index, IMultiplicityAware)
      if special is not None or ma is None or ma.multi_valued():
        t = TAnd(t, TNot(TOr(*(lookup(k) for k in not_))))
    return t

class _Match(object):
  """Auxiliary to handle matching."""

  #SPECIAL = special characters

  def prefix(self, pattern):
    """return the passive prefix of *pattern*."""
    special = self.SPECIAL
    for i, c in enumerate(pattern):
      if c in special: break
    else: return pattern
    return pattern[:i]

  def prepare(self, pattern):
    """return a passive prefix and a filter."""
    prefix = self.prefix(pattern)
    return prefix, self.matcher(prefix, pattern)

class _Glob(_Match):
  SPECIAL = "*?[]"

  def matcher(self, prefix, pattern):
    if len(prefix) == len(pattern): return lambda s, l=len(prefix): len(s) == l
    
    l = len(prefix)
    return lambda s, l=l, match=match_glob(pattern[l:]): match(s, l)

class _Regex(_Match):
  SPECIAL = ".^$*+?{}\\[]|()"

  def matcher(self, prefix, pattern):
    l = len(prefix)
    return lambda s, match=match_regexp(pattern[l:]), l=l: match(s, l)

MATCH = dict(glob=_Glob().prepare, regexp=_Regex().prepare)


class _HandlePureNot(object):
  def _handle_pure_not(self, index, not_, lookup):
    # can implement the "pure not" via key expansion only
    #  for single valued indexes
    ki = querySubscriptionAdapter(index, IKeyedIndex) \
         if single_valued(index) else None
    indexed = querySubscriptionAdapter(index, IIndexed)
    if ki is None and indexed is None: # should not be possible
      raise ValueError('"pure not" supported only for `IKeyedIndex` or `IIndexed` indexes')
    if indexed is not None:
      il = 10000000 if ki is None else index.indexSize()
      if il > 2 * len(not_):
        return None, TAnd(TSet(indexed.get_dids()),
                          TNot(TOr(*(lookup(k) for k in not_)))
                          )
    return ki.keys(), None

class _KeyExpander(object):
  def _expand_keys(self, index, keys, range, match):
    ki = getSubscriptionAdapter(index, IKeyedIndex)
    if range:
      lmin = lmax = None
      if "min" in range: lmin = keys.minKey()
      if "max" in range: lmax = keys.maxKey()
      keys = ki.keys(lmin, lmax)
    if match:
      new_keys = OOSet()
      match = MATCH[match]
      for k in keys:
        prefix, filter= match(k)
        for nk in ki.keys(prefix):
          if not nk.startswith(prefix): break
          if filter(nk): new_keys.add(nk)
      keys = new_keys
    return keys
  

@conditional_adapter(keyed_index, keyed_index_query_check)
@adapter(IPluggableIndex, _TermQuery)
class KeyedIndexConverter(SpecConverter, _KeyExpander): pass


class PureNotQueryCheck(QueryCheck):
  """Check that the query is a "pure not"."""
  SUPPORTED = frozenset(("and", "or", "not"))

  def __call__(self, *objs):
    spec = normalize_spec(objs[1].make_spec())
    return spec.get("not") and not spec.get("keys") and \
           super(PureNotQueryCheck,self).__call__(*objs)

pure_not_query_check = PureNotQueryCheck()
indexed = Adaptable(IIndexed)

class SingleValuedIndexCheck(CheckArg0, ClassBasedCheck):
  @instance_cached
  def __call__(self, *objs):
    idx = self.get_arg(objs)
    ma = querySubscriptionAdapter(idx, IMultiplicityAware)
    return not (ma is None or ma.multi_valued())
single_valued = SingleValuedIndexCheck()

class PureNotIndexCheck(CheckArg0, ClassBasedCheck):
  @instance_cached
  def __call__(self, *objs):
    return indexed(*objs) or (keyed_index(*objs) and single_valued(*objs))


@conditional_adapter(PureNotIndexCheck(), pure_not_query_check)
@adapter(IPluggableIndex, _TermQuery)
class PureNotIndexConverter(SpecConverter, _HandlePureNot): pass


class ExplicitQueryCheck(QueryCheck):
  """Check for an explicite query (not a pure not)."""
  SUPPORTED = frozenset(("and", "or", "not"))

  def __call__(self, *objs):
    spec = normalize_spec(objs[1].make_spec())
    return spec.get("keys") and super(ExplicitQueryCheck,self).__call__(*objs)


@conditional_adapter(ExplicitQueryCheck())
@adapter(IPluggableIndex, _TermQuery)
class ExplicitIndexConverter(SpecConverter): pass


#############################################################################
# `Indexed` converter
@conditional_adapter(indexed)
@adapter(IPluggableIndex, Indexed)
class IndexedQueryConverter(IndexQueryConverter):
  def transform(self, q, context):
    return TSet(getSubscriptionAdapter(self.index, IIndexed).get_dids())


#############################################################################
# `LiteralResultSet` converter
@adapter(LiteralResultSet)
class LiteralResultSetConverter(QueryConverter):
  def transform(self, q, context): return TSet(q.set)
  


#############################################################################
# `Filter` converter
@conditional_adapter(Adaptable(IIndexedValue, IMultiplicityAware))
@adapter(IPluggableIndex, Filter)
class FilterConverter(IndexQueryConverter):
  def transform(self, q, context):
    index = self.index
    fetch_value = getSubscriptionAdapter(index, IIndexedValue).indexed_value_for
    def tfilter(did, fetch=fetch_value, filter=q.filter):
      value = fetch(did)
      return value is not None and filter(value)
    return TFilter(tfilter)


#############################################################################
#############################################################################
## `_CombiningQuery`

CQMap = {Not:(TNot, False), And:(TAnd, True), Or:(TOr, None)}

@adapter(_CombiningQuery)
class _CombiningConverter(QueryConverter):
  def transform(self, q, context):
    op, focus = CQMap[q.__class__]
    if focus is not None and focus is not context.env.has_focus:
      context = context.push(has_focus = focus)
    ct = context.transform
    return op(*(ct(c) for c in q))


