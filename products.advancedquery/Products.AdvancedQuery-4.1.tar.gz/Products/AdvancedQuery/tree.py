# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Bubach, Germany
# see "LICENSE.txt" for details
"""Tree structure.

Note: the classes in this module are not thread safe.
"""
from copy import copy

class Node(object):
  """general tree node."""

class Leaf(Node):
  """a leaf node."""

class Container(Node):
  """A node with children."""
  def __init__(self, *children):
    self._children = list(children)

  def __len__(self): return len(self._children)
  def __iter__(self): return iter(self._children)
  def __getitem__(self, i): return self._children[i]

  def append(self, child): self._children.append(child)

  def new_children(self, new_children):
    """a copy with children *new_children*."""
    c = copy(self)
    Container.__init__(c, *new_children)
    return c

class Not(Container): pass
class And(Container): pass
class Or(Container): pass


def unfold(t, complement={And:Or, Or:And, Not:Not}):
  """simplify the root part of *t* based on the semantics of `And`, `Or` and `Not`.

  Note: `complement` must be specialized for derived classes
  """
  tcl = t.__class__
  comp = complement.get(tcl)
  if comp is None: return t # not handled root
  if issubclass(tcl, Not):
    if isinstance(t[0], Container):
      t0 = t[0]
      if isinstance(t0, Not): return t0[0] # Not(Not(t)) --> t
      elif len(t0) == 0:
        comp = complement.get(t0.__class__, None)
        # Not(And()) -> Or();  Not(Or()) -> And()
        return t if comp is None else comp()
    return t
  # `And` or `Or`
  if len(t) == 1: return t[0]
  new_children = []; changed = False
  for tc in t:
    if tcl is tc.__class__: new_children.extend(tc); changed = True; continue
    elif comp is tc.__class__ and len(tc) == 0: return tc
    new_children.append(tc)
  return t.new_children(new_children) if changed else t


