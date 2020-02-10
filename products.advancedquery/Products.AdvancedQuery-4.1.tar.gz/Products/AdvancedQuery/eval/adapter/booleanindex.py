# Copyright (C) 2019 by Dr. Dieter Maurer, Eichendorffstr. 23, D-66386 St. Ingbert, Germany
#       $Id: booleanindex.py,v 1.1 2019/04/22 05:55:56 dieter Exp $
"""(Subscription) adapters for `BooleanIndex`."""
from zope.interface import implementer
from zope.component import adapter

from BTrees.OOBTree import OOSet

from Products.PluginIndexes.BooleanIndex.BooleanIndex import BooleanIndex

from ..interfaces import \
     IKeyNormalizingIndex, ILookupTreeIndex, \
     IKeyedIndex, IIndexedValue, IMultiplicityAware

from ..tree import Set, And, Not
from .index import IndexAdapter, recondition, SafeInheritance
from . import unindex
from . import conditional_adapter


booleanindex_unindex = SafeInheritance(BooleanIndex, "unindex_object")
booleanindex_search = SafeInheritance(BooleanIndex, "query_index")

@conditional_adapter(booleanindex_search)
@adapter(BooleanIndex)
@implementer(IKeyedIndex)
class KeyedBooleanIndex(IndexAdapter):
  def keys(self, min=None, max=None, exclude_min=False, exclude_max=False):
    idx = self.index
    ind_n = idx._length()
    if not ind_n: keys = OOSet()
    elif ind_n > idx._index_length():
      # we have 2 values
      keys = OOSet((False, True))
    else: keys = OOSet(bool(idx._index_value))
    return keys.keys(min, max, exclude_min, exclude_max)


@conditional_adapter(booleanindex_search)
@adapter(BooleanIndex)
@implementer(ILookupTreeIndex)
class LookupTreeBooleanIndex(IndexAdapter):
  def tree_for_key(self, key, context):
    idx = self.index
    if key is bool(idx._index_value): return Set(idx._index)
    return And(Set(idx._unindex), Not(Set(idx._index)))


@conditional_adapter(booleanindex_search)
@adapter(BooleanIndex)
@implementer(IKeyNormalizingIndex)
class KeyNormalizingBooleanIndex(IndexAdapter):
  def normalize_key(self, key): return bool(key)


# take over from `unindex`
md = globals()
for a in "Indexed IndexedValue MultiplicityAware".split():
  md[a + "BooleanIndex"] = recondition(getattr(unindex, a + "UnIndex"),
                                       adapter(BooleanIndex),
                                       booleanindex_unindex,
                                       )
