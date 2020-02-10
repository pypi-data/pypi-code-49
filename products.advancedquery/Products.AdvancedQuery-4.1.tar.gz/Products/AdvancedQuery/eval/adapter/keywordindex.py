# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: keywordindex.py,v 1.1 2019/04/22 05:55:57 dieter Exp $
"""(Subscription) adapters for `KeywordIndex`."""
from zope.interface import implementer
from zope.component import adapter

from Products.PluginIndexes.KeywordIndex.KeywordIndex import KeywordIndex

from ..interfaces import IMultiplicityAware

from .index import IndexAdapter, recondition, SafeInheritance
from . import unindex
from . import conditional_adapter


keywordindex_unindex = SafeInheritance(KeywordIndex, "unindex_object")


@conditional_adapter(keywordindex_unindex)
@adapter(KeywordIndex)
@implementer(IMultiplicityAware)
class MultiplicityAwareKeywordIndex(IndexAdapter):
  def multi_valued(self): return True


# Take over from `unindex`
md = globals()
for a in "Indexed IndexedValue".split():
  md[a + "KeywordIndex"] = recondition(getattr(unindex, a + "UnIndex"),
                                         adapter(KeywordIndex),
                                         keywordindex_unindex,
                                         )

