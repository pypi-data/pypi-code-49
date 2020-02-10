# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: tests.py,v 1.1 2019/04/22 05:55:59 dieter Exp $
from unittest import skipIf

from BTrees.IIBTree import IISet, intersection, multiunion, difference
from BTrees.IOBTree import IOBTree
from Products.PluginIndexes.FieldIndex.FieldIndex import FieldIndex

from Products.AdvancedQuery.tests.layer import AqTest
from ....tree import Set, And, Or, Not, Lookup, Filter, IndexLookup
from ....transform import Context
from ....context import ISearch
from ....interfaces import ITreeEvaluator_Set, ITreeEvaluator_ISearch


class FocusLookup(Lookup):
  focus = False

  def __init__(self, set, wants_focus):
    self.set = set
    self.wants_focus = wants_focus

  def as_set(self, context):
    self.focus = context.env.focus
    return self.set

l2 = FocusLookup(IISet(range(0, 11, 2)), 0)
l3 = FocusLookup(IISet(range(0, 11, 3)), 1)
l5 = FocusLookup(IISet(range(0, 11, 5)), 2)
ls = FocusLookup(IISet((1,)), 0)
lups = [l2, l3, l5, ls]

universe = IISet(range(0, 11))
universe_tree = IOBTree(tuple((i, None) for i in universe))
class _Resources(object):
  def get_dids(self):
    # a real context returns an `IOBTree`
    # return universe
    return universe_tree
resources = _Resources()

fi = FieldIndex("fi")

scontext = Context.make_context(resources, ITreeEvaluator_Set, focus=None)


class SetTests(AqTest):
  def assertEqual(self, x, y):
    # `IISet` has a strange equality check - do our own
    if isinstance(x, IISet): x = list(x); y = list(y)
    super(SetTests, self).assertEqual(x, y)



class TestSet(SetTests):
  def setUp(self):
    for lup in lups: lup.focus = False

  def test_focus_and(self):
    r = scontext.transform(And(l5, l3, l2))
    self.assertEqual(r, IISet((0,)))
    self.assertIsNone(l2.focus)
    self.assertEqual(l3.focus, l2.set)
    self.assertEqual(l5.focus, intersection(l2.set, l3.set))

  def test_focus_or(self):
    r = scontext.transform(Or(l5, l3), focus=l2.set)
    self.assertEqual(r, intersection(multiunion((l5.set, l3.set)), l2.set))
    self.assertIs(l5.focus, l2.set)
    self.assertIs(l3.focus, l2.set)

  def test_focus_not(self):
    r = scontext.transform(Not(l3), focus=l2.set)
    self.assertEqual(r, difference(l2.set, l3.set))

  def test_return_on_empty(self):
    r = scontext.transform(And(l3, ls), focus=l2.set)
    self.assertFalse(r)
    self.assertIs(ls.focus, l2.set)
    self.assertIs(l3.focus, False)

  def test_not(self):
    r = scontext.transform(Not(l2))
    self.assertEqual(r, difference(universe, l2.set))

  def _large_or(self, focus):
    orl = [IISet(range(0, 100, i)) for i in range(2, 11)]
    r = scontext.transform(Or(*(Set(s) for s in orl)), focus=focus)
    self.assertEqual(r, intersection(multiunion(orl), focus))

  def test_large_or_small_focus(self):
    self._large_or(IISet((0, 13)))

  def test_large_or_large_focus(self):
    self._large_or(l2.set)

  # implicitly tested (via `test_large_or*`
  #def test_set

  def test_index_lookup(self):
    r = scontext.transform(IndexLookup(fi, (0,)))
    self.assertEqual(r, IISet())

  def test_filter(self):
    r = scontext.transform(Filter(lambda did: did in l2.set))
    self.assertEqual(r, l2.set)

  def test_focus_filter(self):
    r = scontext.transform(Filter(lambda did: did in l2.set), focus=l3.set)
    self.assertEqual(r, intersection(l2.set, l3.set))

  def test_focus_and_or(self):
    r = scontext.transform(And(Or(l5, l3), l2))
    self.assertEqual(r, intersection(l2.set, multiunion((l5.set, l3.set))))
    self.assertIs(l2.focus, None)
    self.assertIs(l5.focus, l2.set)
    self.assertIs(l3.focus, l2.set)

  def test_focus_and_or_not(self):
    r = scontext.transform(And(Or(l5, Not(ls)), Or(l3), l2))
    self.assertEqual(r, intersection(l3.set, l2.set))
    self.assertIsNone(l2.focus)
    self.assertIs(l3.focus, l2.set)
    self.assertIsNone(ls.focus)
    self.assertEqual(l5.focus, intersection(l3.set, l2.set))

  def test_focus_and_or_filter(self):
    r = scontext.transform(And(Or(l5, Filter(lambda did: did==1)), Or(l3), l2))
    self.assertEqual(r, IISet((0,)))
    self.assertIsNone(l2.focus)
    self.assertIs(l3.focus, l2.set)
    self.assertEqual(l5.focus, intersection(l3.set, l2.set))


icontext = Context.make_context(resources, ITreeEvaluator_ISearch, focus=None)

@skipIf(ISearch is None, "ISearch not installed")
class TestISearch(SetTests):
  def _transform(self, t):
    return icontext.transform(t).asSet()

  def test_set(self):
    self.assertEqual(self._transform(l2), l2.set)

  def test_lookup_index(self):
    self.assertEqual(self._transform(IndexLookup(fi, (1,))), IISet())

  def test_and(self):
    self.assertEqual(self._transform(And(l2, l3)), intersection(l2.set, l3.set))

  def test_or(self):
    self.assertEqual(self._transform(Or(l2, l3)), multiunion((l2.set, l3.set)))

  def test_not(self):
    self.assertEqual(self._transform(Not(l2)), difference(universe, l2.set))

  def test_filter(self):
    self.assertEqual(self._transform(Filter(lambda did: did in l2.set)), l2.set)
