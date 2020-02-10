# Copyright (C) 2019 by Dr. Dieter Maurer, Eichendorffstr. 23, D-66386 St. Ingbert, Germany
#       $Id: daterangeindex.py,v 1.1 2019/04/22 05:55:56 dieter Exp $
"""(Subscription) adapters for `DateRangeIndex`."""
from zope.interface import implementer
from zope.component import adapter

from Products.PluginIndexes.DateRangeIndex.DateRangeIndex import DateRangeIndex

from ..interfaces import IKeyNormalizingIndex, ILookupTreeIndex, \
     ITermValueMatch


from ..tree import Set, And, Or, Not
from .index import IndexAdapter, recondition, SafeInheritance
from . import unindex
from . import conditional_adapter


daterangeindex_unindex = SafeInheritance(DateRangeIndex, "unindex_object")
daterangeindex_search = SafeInheritance(DateRangeIndex, "query_index")


@conditional_adapter(daterangeindex_search)
@adapter(DateRangeIndex)
@implementer(ILookupTreeIndex)
class LookupTreeDateRangeIndex(IndexAdapter):
  def tree_for_key(self, key, context):
    idx = self.index
    # a `DateRangeIndex` indexes either nothing or everything.
    if idx._since_field is None: return Or() # nothing indexed
    # everything indexed
    # we implement as a `Not` - assuming that most documents have no
    #  restriction (which makes the `Not` small)
    until_only = Or(*(map(Set, idx._until_only.values(None, key - 1))))
    since_only = Or(*(map(Set, idx._since_only.values(key + 1))))
    until = Or(*(map(Set, idx._until.values(None, key - 1))))
    since = Or(*(map(Set, idx._since.values(key + 1))))
    return Not(Or(since, since_only, until_only, until))


@conditional_adapter(daterangeindex_search)
@adapter(DateRangeIndex)
@implementer(IKeyNormalizingIndex)
class KeyNormalizingDateRangeIndex(IndexAdapter):
  def normalize_key(self, key): return self.index._convertDateTime(key)


# unconditional
@adapter(DateRangeIndex)
@implementer(ITermValueMatch)
class TermValueMatchDateRangeIndex(IndexAdapter):
  def match(self, indexed_value, term):
    since, until = indexed_value
    return (since is None or term >= since) \
           and (until is None or term <= until)



# take over from `unindex`
md = globals()
for a in "Indexed IndexedValue MultiplicityAware".split():
  md[a + "DateRangeIndex"] = recondition(getattr(unindex, a + "UnIndex"),
                                       adapter(DateRangeIndex),
                                       daterangeindex_unindex,
                                       )
