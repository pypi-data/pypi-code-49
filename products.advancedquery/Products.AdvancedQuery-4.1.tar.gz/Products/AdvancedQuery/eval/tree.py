# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: tree.py,v 1.1 2019/04/22 05:55:56 dieter Exp $
"""Intermediate lookup tree (used for optimizations).

The trees in this module are used to represent a query at
an intermediate level. Their leaves are lookups and filters.
They can be arbitrarily combined with `And`, `Or` and `Not`.

If we have `q1 & q2`, then the evaluation of `q2` does not
need to give all hits for `q2`, it is sufficient to give
the hits that are also hits for `q1`. Taking this into account
can significantly reduce evaluation time.
This module generalizes this: the context of a subquery `q`
defines a so called `focus` (a set or `None`) and the evaluation
of `q` in this context needs only give hits in this `focus` (provided
it is not `None`).
Tree nodes provide information in an attribute `wants_focus` to
indicate the importance of a good focus. See below, for details.
"""
from zope.interface import Interface, implementer
from zope.schema import Int

from Products.PluginIndexes.interfaces import ILimitedResultIndex

from ..tree import Node, Leaf, Container, And, Or, Not

class ILookupTree(Interface):
  wants_focus = Int(
    title=u"wants_focus",
    description=u" 0 -- focus not relevant "
                u" 1 -- focus profitable "
                u" 2 -- focus needed ",
    min=0, max=2,
    )

  complexity_class = Int(
    title=u"indication of the classes complexity",
    description=u" 0 -- a `Set` "
                u" 1 -- a combination of complexity 0 and 1 via `And` or `Or` "
                u" 2 -- a `Lookup` or combination of complexity <= 2 "
                u" 3 -- a `Not` or something involving `Not` "
                u" 4 -- a `Filter` or something involving a filter ",
    min=0, max=4,
    )


class ISet(Interface):

  def as_set(context):
    """the hits within *context*.

    Likely, the most important information in *context*
    is 'context.env.focus`, the context's *focus*.
    """


@implementer(ILookupTree)
class Node(Node):
  wants_focus = 0


class Leaf(Node, Leaf): pass

class Container(Node, Container):
  node_complexity_class = 1
  focus_combiner = None # to be defined by derived classes

  _cc = None
  @property
  def complexity_class(self):
    cc = self._cc
    if cc is None:
      self._cc = cc = max(self.node_complexity_class,
                          *(c.complexity_class for c in self)
                          )
    return cc

  _wf = None
  @property
  def wants_focus(self):
    wf = self._wf
    if wf is None:
      wf = self._wf = self.focus_combiner(c.wants_focus for c in self)
    return wf


@implementer(ISet)
class Set(Leaf):
  """encapsulates a set of hits."""
  complexity_class = 0

  def __init__(self, set): self._set = set
  def as_set(self, unused): return self._set


@implementer(ISet)
class Lookup(Leaf):
  """a delayed lookup.
  """
  complexity_class = 2

  def as_set(self, context): raise NotImplementedError()


class IndexLookup(Lookup):
  def __init__(self, index, spec):
    self._index = index; self._spec = spec
    self.wants_focus = ILimitedResultIndex.providedBy(index)

  def as_set(self, context):
    idx = self._index
    rs = (context.env.focus,) if self.wants_focus else ()
    return idx._apply_index({idx.id:self._spec}, *rs)[0]


class Filter(Leaf):
  wants_focus = 2
  complexity_class = 4

  def __init__(self, filter): self._filter = filter


class Not(Container, Not):
  wants_focus = 2
  node_complexity_class = 3


class _Op(Container): pass  # common base for `And` and `Or`

class And(_Op, And): focus_combiner = min
class Or(_Op, Or): focus_combiner = max
