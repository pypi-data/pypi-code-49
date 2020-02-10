# Copyright (C) 2019 by Dr. Dieter Maurer, Eichendorffstr. 23, D-66386 St. Ingbert, Germany
#       $Id: unindex.py,v 1.1 2019/04/22 05:55:57 dieter Exp $
"""(Subscription) adapters for `Products.PluginIndexes.unindex.UnIndex."""
from zope.interface import implementer
from zope.component import adapter

from BTrees.IIBTree import IISet

from Products.PluginIndexes.unindex import UnIndex

from ..interfaces import IIndexedValue, IMultiplicityAware, \
     IIndexed, IKeyNormalizingIndex, ILookupIndex, \
     IKeyedIndex, IIndexedValue, IMultiplicityAware

from . import conditional_adapter
from .index import IndexAdapter, SafeInheritance


unindex_unindex = SafeInheritance(UnIndex, "unindex_object")
unindex_search = SafeInheritance(UnIndex, "query_index")

@conditional_adapter(unindex_search)
@adapter(UnIndex)
@implementer(IKeyedIndex)
class KeyedUnIndex(IndexAdapter):
  def keys(self, min=None, max=None, exclude_min=False, exclude_max=False):
    return self.index._index.keys(min, max, exclude_min, exclude_max)


@conditional_adapter(unindex_unindex)
@adapter(UnIndex)
@implementer(IIndexed)
class IndexedUnIndex(IndexAdapter):
  def get_dids(self): return self.index._unindex


@conditional_adapter(unindex_search)
@adapter(UnIndex)
@implementer(ILookupIndex)
class LookupUnIndex(IndexAdapter):
  def dids_for_key(self, key):
    dids = self.index._index.get(key)
    if dids is None: return IISet()
    if isinstance(dids, int): dids = IISet((dids,))
    return dids


@conditional_adapter(unindex_unindex)
@adapter(UnIndex)
@implementer(IIndexedValue)
class IndexedValueUnIndex(IndexAdapter):
  def indexed_value_for(self, did):
    return self.index._unindex.get(did)


@conditional_adapter(unindex_unindex)
@adapter(UnIndex)
@implementer(IMultiplicityAware)
class MultiplicityAwareUnIndex(IndexAdapter):
  def multi_valued(self): return False


@conditional_adapter(unindex_search)
@adapter(UnIndex)
@implementer(IKeyNormalizingIndex)
class KeyNormalizingUnIndex(IndexAdapter):
  def normalize_key(self, key): return self.index._convert(key)
