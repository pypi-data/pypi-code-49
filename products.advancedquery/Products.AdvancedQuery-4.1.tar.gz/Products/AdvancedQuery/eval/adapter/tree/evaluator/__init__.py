# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: __init__.py,v 1.1 2019/04/22 05:55:59 dieter Exp $
"""Tree evaluation."""
from ....tree import Node


class TreeEvaluator(object):
  """they adapt a `Node`."""
  def __init__(self, node): self.node = node
