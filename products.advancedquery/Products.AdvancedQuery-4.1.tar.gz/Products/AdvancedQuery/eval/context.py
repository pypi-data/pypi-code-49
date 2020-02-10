# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Bubach, Germany
# see "LICENSE.txt" for details
"""Evaluation context."""
from zope.interface import implementer

from .interfaces import IQueryContext, IQueryRestrict, \
     IQueryOptimizerChain, IQueryConverter, \
     ITreeOptimizerChain, ITreeEvaluator_Set, ITreeEvaluator_ISearch
from .transform import Context, OptimizerContext
from .lib import instance_cached, InstanceCache
from .adapter import getSubscriptionAdapter
from .adapter.tree.evaluator.set_ import _to_set

try: from dm.incrementalsearch import ISearch
except ImportError: ISearch = None


@implementer(IQueryContext)
class QueryContext(InstanceCache):
  def __init__(self, catalog):
    self._catalog = catalog
    self._cat = catalog._catalog

  def get_index(self, name): return self._cat.getIndex(name)

  @instance_cached
  def get_indexes(self, filter=None):
    return [idx for idx
            in (self.get_index(name) for name in self._cat.indexes.keys())
            if filter(idx)
            ]

  def get_dids(self): return self._cat.paths

  def eval(self, q, restricted, **kw):
    if restricted:
      q = getSubscriptionAdapter(self._catalog, IQueryRestrict).restrict(q, **kw)
    # optimize query
    o_context = OptimizerContext.make_context(self, IQueryOptimizerChain)
    q, _ = o_context.optimize(q)
    # transform query to tree
    c_context = Context.make_context(self, IQueryConverter, has_focus=False)
    t = c_context.transform(q)
    # optimize tree
    o_context = OptimizerContext.make_context(self, ITreeOptimizerChain)
    t, _ = o_context.optimize(t)
    # evaluate the tree
    c_context = Context.make_context(
      self,
      (ITreeEvaluator_Set if ISearch is None else ITreeEvaluator_ISearch),
      focus=None
      )
    r = c_context.transform(t)
    return r if ISearch is None else _to_set(r.asSet())
