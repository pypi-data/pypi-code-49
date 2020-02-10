# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: isearch.py,v 1.1 2019/04/22 05:55:59 dieter Exp $
"""Evaluate the tree as an ISearch."""
from zope.interface import implementer
from zope.component import adapter

from dm.incrementalsearch import IBTree, Enumerator, \
     IAnd_int, IOr_int, INot, IFilter_int

from ....interfaces import ITreeEvaluator_ISearch
from ....tree import And, Or, Not, Filter, ISet
from . import TreeEvaluator


@implementer(ITreeEvaluator_ISearch)
class TreeEvaluator(TreeEvaluator): pass


@adapter(ISet)
class SetEvaluator(TreeEvaluator):
  def transform(self, n, context): return IBTree(n.as_set(context))


@adapter(And)
class AndEvaluator(TreeEvaluator):
  def transform(self, n, context):
    if not n: return IBTree(context.get_dids())
    is_and = IAnd_int(*(context.transform(c)
                        for c in sorted(n, key=lambda c: c.wants_focus)))
    is_and.complete()
    return is_and

@adapter(Or)
class OrEvaluator(TreeEvaluator):
  def transform(self, n, context):
    is_or = IOr_int(*(context.transform(c)
                      for c in sorted(n, key=lambda c: c.wants_focus)))
    is_or.complete()
    return is_or
    return is_and

@adapter(Not)
class NotEvaluator(TreeEvaluator):
  def transform(self, n, context):
    return INot(context.transform(n[0]), Enumerator(context.get_dids()))

@adapter(Filter)
class FilterEvaluator(TreeEvaluator):
  def transform(self, n, context):
    return IFilter_int(n._filter, Enumerator(context.get_dids()))
