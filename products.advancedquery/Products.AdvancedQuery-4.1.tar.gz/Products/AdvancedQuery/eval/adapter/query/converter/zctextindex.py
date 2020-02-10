# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: zctextindex.py,v 1.2 2020/02/10 08:31:41 dieter Exp $
from zope.interface import implementer, Interface
from zope.component import adapter

from Products.ZCTextIndex.ZCTextIndex import ZCTextIndex, QueryParser
from Products.ZCTextIndex.WidCode import encode
from Products.ZCTextIndex.BaseIndex import BaseIndex
from Products.ZCTextIndex.OkapiIndex import OkapiIndex

from Products.AdvancedQuery import MatchGlob
from ....interfaces import ILookupTreeIndex, IIndexedValue
from ...import ClassBasedCheck, instance_cached

from . import _TermQuery, SafeInheritance, normalize_spec, \
     QueryIndexQueryCheck, \
     TAnd, TOr, TSet, TFilter, TNot, \
     IndexQueryConverter, conditional_adapter, querySubscriptionAdapter, \
     CheckArg0


zctextindex_search = SafeInheritance(ZCTextIndex, "query_index")

class IndexSupported(ClassBasedCheck, CheckArg0):
  @instance_cached
  def __call__(self, *objs):
    idx = self.get_arg(objs)
    lookup = querySubscriptionAdapter(idx, ILookupTreeIndex)
    value = querySubscriptionAdapter(idx, IIndexedValue)
    return value and lookup

index_supported = IndexSupported()

def supported_base_index(zc_index, query):
  return index_supported(zc_index.index)


class _ZCTextIndexQueryConverter(IndexQueryConverter):
  def transform(self, q, context):
    spec = normalize_spec(q.make_spec())
    qs = " ".join(spec["keys"])
    if not qs.strip(): return TOr() # empty query --> empty result
    idx = self.index
    bi = idx.index
    lx = idx.getLexicon()
    tree = QueryParser(lx).parseQuery(qs)
    lookup = querySubscriptionAdapter(bi, ILookupTreeIndex).tree_for_key
    indexed_value = querySubscriptionAdapter(bi, IIndexedValue).indexed_value_for
    def recurse(t):
      tt = t.nodeType()
      if tt in ("AND", "OR"):
        return (TAnd if tt == "AND" else TOr)(
          *(recurse(c) for c in t.getValue()))
      elif tt == "NOT": return TNot(recurse(t.getValue()))
      elif tt == "ATOM":
        return TOr(*(lookup(wid) for wid in lx.termToWordIds(t.getValue())))
      elif tt == "GLOB":
        return TOr(*(lookup(wid) for wid in lx.globToWordIds(t.getValue())))
      elif tt == "PHRASE":
        wids = lx.termToWordIds(t.getValue())
        known_wids = bi._remove_oov_wids(wids)
        if len(wids) != len(known_wids): return TOr()
        return TAnd(
          TAnd(*(lookup(wid) for wid in known_wids)),
          TFilter(
            lambda did, fetch=indexed_value, phrase=encode(known_wids):
            phrase in fetch(did)))
      else: raise NotImplementedError("unsupported node type")
    return recurse(tree)


@conditional_adapter(zctextindex_search, supported_base_index)
@adapter(ZCTextIndex, MatchGlob)
class ZCTextIndexGlobConverter(_ZCTextIndexQueryConverter): pass


@conditional_adapter(zctextindex_search, QueryIndexQueryCheck(), supported_base_index)
@adapter(ZCTextIndex, _TermQuery)
class ZCTextIndexQueryConverter(_ZCTextIndexQueryConverter): pass


base_index_like = SafeInheritance(BaseIndex, "index_doc")

@conditional_adapter(base_index_like)
@adapter(BaseIndex)
@implementer(IIndexedValue)
class BaseIndexIndexedValue(object):
  def __init__(self, index): self.index = index
  def indexed_value_for(self, did): return self.index._docwords.get(did)


@conditional_adapter(base_index_like)
@adapter(BaseIndex)
@implementer(ILookupTreeIndex)
class BaseIndexLookupTreeIndex(object):
  def __init__(self, index): self.index = index
  def tree_for_key(self, wid, context=None):
    dids = self.index._wordinfo.get(wid)
    return TOr() if dids is None else TSet(dids.keys())

from ...index import recondition
okapi_index_like = SafeInheritance(OkapiIndex, "index_doc")

OkapiIndexIndexedValue = recondition(BaseIndexIndexedValue, adapter(OkapiIndex), okapi_index_like)
OkapiIndexLookupTreeIndex = recondition(BaseIndexLookupTreeIndex, adapter(OkapiIndex), okapi_index_like)
