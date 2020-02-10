# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: tests.py,v 1.1 2019/04/22 05:55:59 dieter Exp $
from BTrees.IIBTree import IISet

from Products.AdvancedQuery.tests.layer import AqTest
from ....tree import Set, And, Or, Not, Lookup
from ....transform import OptimizerContext
from ....interfaces import ITreeOptimizerChain

context = OptimizerContext.make_context(None, ITreeOptimizerChain)

class TestOptimizations(AqTest):
  def test_empty_set(self):
    t, unchanged = context.optimize(Set(IISet()))
    self.assertFalse(unchanged)
    self.assertIsInstance(t, Or)
    self.assertEqual(len(t), 0)

  def test_nested_not(self):
    t0 = Lookup()
    t, unchanged = context.optimize(Not(Not(t0)))
    self.assertFalse(unchanged)
    self.assertIs(t, t0)

  def test_one_element_and_or(self):
    t0 = Lookup()
    for op in (And, Or):
      with self.subTest(op=op):
        t, unchanged = context.optimize(op(t0))
        self.assertFalse(unchanged)
        self.assertIs(t, t0)

  def test_empty_complement(self):
    t0 = Lookup()
    Ops = (And, Or)
    for op in Ops:
      with self.subTest(op=op):
        cop = Ops[Ops.index(op)-1]
        t1 = cop()
        t, unchanged = context.optimize(op(t0, t1))
        self.assertFalse(unchanged)
        self.assertIs(t, t1)

  def test_unfold(self):
    t0 = Lookup(); t1 = Lookup(); t2 = Lookup()
    for op in (And, Or):
      with self.subTest(op=op):
        t, unchanged = context.optimize(op(t0, op(t1, t2)))
        self.assertFalse(unchanged)
        self.assertIsInstance(t, op)
        self.assertEqual(list(t), [t0, t1, t2])

  def test_recurse(self):
    t, unchanged = context.optimize(And(Set(IISet())))
    self.assertFalse(unchanged)
    self.assertIsInstance(t, Or)
    self.assertFalse(t)

  def test_unchanged(self):
    t0 = And()
    t, unchanged = context.optimize(t0)
    self.assertTrue(unchanged)
    self.assertIs(t, t0)
