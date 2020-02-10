# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: set_.py,v 1.1 2019/04/22 05:55:59 dieter Exp $
"""Evaluate the tree as a set."""

from zope.interface import implementer
from zope.component import adapter

from BTrees.IIBTree import intersection, multiunion, difference, IISet
from BTrees.IOBTree import IOBucket, IOBTree

from ....interfaces import ITreeEvaluator_Set
from ....tree import ISet, And, Or, Not, Filter
from . import TreeEvaluator


@implementer(ITreeEvaluator_Set)
class TreeEvaluator(TreeEvaluator): pass


@adapter(ISet)
class SetEvaluator(TreeEvaluator):
  def transform(self, n, context): return _to_set(n.as_set(context))


@adapter(And)
class AndEvaluator(TreeEvaluator):
  def transform(self, n, context):
    if not n: return _to_set(context.get_dids())
    # order children by `wants_focus, complexity_class`
    cs = sorted(n, key=lambda c: (c.wants_focus, c.complexity_class))
    # handle things not needing a focus
    nf = []
    focus = context.env.focus
    if focus is not None: nf.append(focus)
    for i, c in enumerate(cs):
      if c.wants_focus: break
      nf.append(context.transform(c))
    else: i = -1
    if nf:
      # `intersection(A, B)` has typical runtime costs of
      #    #{a < m} + #{b < m} with m = min(max(A), max(B))
      #    Thus, it is typically far more expensive than determining the
      #    length of the sets.
      #    We make use of this by ordering `nf` by length.
      if len(nf) > 1:
        nf = sorted((s for s in nf), key=lambda s: len(s))
      focus = None
      for s in nf:
        focus = intersection(focus, s)
        if not focus: return focus
    # process what wants a focus
    if i >= 0:
      for i in range(i, len(cs)):
        s = context.transform(cs[i], focus=focus)
        focus = intersection(focus, s)
        if not focus: return focus
    return focus


@adapter(Or)
class OrEvaluator(TreeEvaluator):
  def transform(self, n, context):
    if not n: return IISet()
    focus = context.env.focus
    if focus is None:
      return multiunion([context.transform(c) for c in n])
    # we assume that children with `wants_focus` really perform the
    #   intersection and handle the others here
    #   Note that the assumption is not true for index lookup:
    #   all modern indexes accept `resultset` (which we translate
    #   into `wants_focus`) whether or not the really look at it.
    cs = sorted(n, key=lambda c: c.wants_focus)
    nf = []
    for i, c in enumerate(cs):
      if c.wants_focus: break
      nf.append(context.transform(c))
    else: i = -1
    ops = []
    if i >= 0:
      # `wants_focus`
      ops.append(multiunion([context.transform(c) for c in cs[i:]]))
    if nf:
      if len(nf) == 1: ops.append(nf[0])
      else:
        # we must compute a union relative to a focus.
        #  Restricting the operands first to the focus and then perform
        #  the union avoids us potentially the construction of a large
        #  intermediate set - at the cost of many intersections.
        #  Due to the peculiar runtime behaviour of `intersection` this
        #  is often more expensive than delaying the intersection.
        #  We form packets of unions of sufficient size 
        fs = len(focus); limit = 6 * fs
        i = 0; acs = 0 if not ops else len(ops[0])
        pr = []
        while i < len(nf):
          s = nf[i]; ops.append(s); i += 1
          acs += len(s)
          if acs >= limit:
            partial = ops[0] if len(ops) == 1 else multiunion(ops)
            pr.append(intersection(focus, partial))
            acs = 0; ops = []
        if ops:
          partial = ops[0] if len(ops) == 1 else multiunion(ops)
          pr.append(intersection(focus, partial))
        return pr[0] if len(pr) == 1 else multiunion(pr)
    partial = ops[0] if len(ops) == 1 else multiunion(ops)
    return intersection(focus, partial)


@adapter(Not)
class NotEvaluator(TreeEvaluator):
  def transform(self, n, context):
    cs = context.push(focus=None).transform(n[0])
    focus = context.env.focus
    focus = focus if focus is not None else _to_set(context.get_dids())
    return difference(focus, cs)


@adapter(Filter)
class FilterEvaluator(TreeEvaluator):
  def transform(self, n, context):
    focus = context.env.focus
    focus = focus if focus is not None else _to_set(context.get_dids())
    filter = n._filter
    return IISet(did for did in focus if filter(did))


def _to_set(s):
  """Auxiliary to work around a restriction of newer `BTrees` versions."""
  # modern `BTrees` versions no longer support set operations
  # between `IO` and `II` - convert
  return IISet(s) if isinstance(s, (IOBucket, IOBTree)) else s
