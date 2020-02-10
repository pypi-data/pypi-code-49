# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: pathindex.py,v 1.1 2019/04/22 05:55:57 dieter Exp $
from zope.interface import implementer
from zope.component import adapter

from Products.PluginIndexes.PathIndex.PathIndex import PathIndex

from . import _TermQuery, SafeInheritance, normalize_spec, \
     QueryIndexQueryCheck, \
     TAnd, TOr, TSet, IndexQueryConverter, conditional_adapter


pathindex_search = SafeInheritance(PathIndex, "query_index")


@conditional_adapter(pathindex_search, QueryIndexQueryCheck())
@adapter(PathIndex, _TermQuery)
class PathIndexQueryConverter(IndexQueryConverter):
  def transform(self, q, context):
    index = self.index
    spec = normalize_spec(q.make_spec())
    op = spec.get("operator", "or")
    default_level = spec.get("level", 0)
    def _lookup(comps, level):
      if level < 0:
        return TOr(*(_lookup(comps, i) for i in range(index._depth + 2 - len(comps))))
      empty = TOr()
      if level + len(comps) > index._depth + 1: return empty # too long
      cts = []
      for i, c in enumerate(reversed(comps)):
        ct = index._index.get(c)
        if ct is None: return empty
        ct = ct.get(level + i)
        if ct is None: return empty
        cts.append(TSet(ct))
      return TAnd(*cts)
    def lookup(k, level):
      if not isinstance(k, str): k, level = k[0], k[1]
      comps = list(filter(None, k.split("/")))
      if not comps: return TAnd()
      return _lookup(comps, level)
    return (TOr if op == "or" else TAnd)(
      *(lookup(k, default_level) for k in spec["keys"]))
