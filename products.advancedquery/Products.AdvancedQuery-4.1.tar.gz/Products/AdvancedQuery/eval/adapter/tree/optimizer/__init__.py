# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: __init__.py,v 1.1 2019/04/22 05:55:59 dieter Exp $
from zope.interface import implementer
from zope.component import adapter

from .....tree import unfold
from ....tree import Node, Container, And, Or, Not, Set
from ....interfaces import ITreeOptimizerChain, ITreeNodeOptimizer
from ....transform import OptimizerChain


@implementer(ITreeNodeOptimizer)
class NodeOptimizer(object):
  """they adapt `Node`."""
  def __init__(self, node): self.node = node



##############################################################################
## 0 -- empty set conversion
@adapter(Set)
class EmptySet(NodeOptimizer):
  order = 0

  def optimize(self, set, context):
    return True if set.as_set(context) else Or()


##############################################################################
## 20 -- unfold nested queries
@adapter(Container)
class Unfold(NodeOptimizer):

  order = 20

  def unfold(self, q, complement={And:Or, Or:And, Not:Not}):
    return unfold(q, complement)

  def optimize(self, q, context):
   oq = self.unfold(q)
   return True if oq is q else oq



##############################################################################
## the chain

@adapter(Node)
@implementer(ITreeOptimizerChain)
class TreeOptimizerChain(OptimizerChain):
  sub_tspec = ITreeNodeOptimizer
