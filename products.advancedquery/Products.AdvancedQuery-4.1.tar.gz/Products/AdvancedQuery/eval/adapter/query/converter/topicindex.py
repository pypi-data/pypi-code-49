# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: topicindex.py,v 1.1 2019/04/22 05:55:58 dieter Exp $
from zope.interface import implementer
from zope.component import adapter

from Products.PluginIndexes.TopicIndex.TopicIndex import TopicIndex

from . import _TermQuery, SafeInheritance, normalize_spec, \
     QueryIndexQueryCheck, \
     TAnd, TOr, TSet, IndexQueryConverter, conditional_adapter

topicindex_search = SafeInheritance(TopicIndex, "query_index")

@conditional_adapter(topicindex_search, QueryIndexQueryCheck())
@adapter(TopicIndex, _TermQuery)
class TopicIndexQueryConverter(IndexQueryConverter):
  def transform(self, q, context):
    index = self.index
    spec = normalize_spec(q.make_spec())
    op = spec.get("operator", "or")
    def lookup(k):
      f = index.filteredSets.get(k)
      return TSet(f.getIds()) if f is not None else TOr()
    return (TOr if op == "or" else TAnd)(
      *(lookup(k) for k in spec["keys"]))
