# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Bubach, Germany
# see "LICENSE.txt" for details
#       $Id: test_unindexes.py,v 1.1 2019/04/22 05:55:58 dieter Exp $
"""Tests for `Products.PluginIndexes.unindex.UnIndex` derivatives."""

from Products.AdvancedQuery.tests.layer import AqTest

from ...interfaces import IIndexed, IKeyedIndex, IKeyNormalizingIndex, \
     ILookupIndex, ILookupTreeIndex, IIndexedValue, IMultiplicityAware, \
     ITermValueMatch

from .. import getSubscriptionAdapter, querySubscriptionAdapter


class O(object):
  def __init__(self, p, value):
    self.id = value if p != "Keyword" else (value,)

unindexes = "Un Boolean Field Keyword UUID".split()
uid = {}
for p in unindexes:
  idx_name = p + "Index"
  idx_mp = "unindex" if p == "Un" else idx_name + "." + idx_name
  idx_mod = __import__("Products.PluginIndexes." + idx_mp, fromlist=(idx_name,))
  idx = getattr(idx_mod, idx_name)("id")
  uid[p] = idx
  idx.index_object(0, O(p, 0))
  idx.index_object(1, O(p, 1))

# `DateRangeIndex`
from Products.PluginIndexes.DateRangeIndex.DateRangeIndex import DateRangeIndex

class BO(object):
  def __init__(self, **kw): self.__dict__.update(kw)

uid["DateRange"] = dri = DateRangeIndex("id", "since", "until")
dri.index_object(0, BO(since=None, until=None))
dri.index_object(1, BO(since=0, until=1))

# `DateIndex`
from Products.PluginIndexes.DateIndex.DateIndex import DateIndex
class DateIndex(DateIndex):
  # override `_convert` to better know the expected objects
  def _convert(self, value, default=None): return value

uid["Date"] = di = DateIndex("id")
di.index_object(0, O("Date", 0))
di.index_object(1, O("Date", 1))


class TestIfaces(AqTest):
  EXCS = dict(DateRange=(IKeyedIndex,))

  def test_IIndexed(self):
    for p, idx in uid.items():
      a = getSubscriptionAdapter(idx, IIndexed)
      self.assertEqual(list(a.get_dids()), [0, 1])

  def test_IKeyedIndex(self):
    for p, idx in uid.items():
      if p == "DateRange": continue
      a = getSubscriptionAdapter(idx, IKeyedIndex)
      self.assertEqual(list(a.keys()), [0, 1])

  def test_ILookup(self):
    for p, idx in uid.items():
      if p == "DateRange": continue # tested separately
      a = querySubscriptionAdapter(idx, ILookupIndex)
      if a is not None:
        def lookup(k): return a.dids_for_key(k)
      else:
        a = getSubscriptionAdapter(idx, ILookupTreeIndex)
        # it is too complicated to check the correct value here
        #   we provide a fake `lookup` which will succeed
        def lookup(k): a.tree_for_key(k, None); return k,
      for k in (0, 1):
        self.assertEqual(list(lookup(k)), [k])

  def test_IKeyNormalizingIndex(self):
    for p, idx in uid.items():
      a = getSubscriptionAdapter(idx, IKeyNormalizingIndex)
      self.assertEqual(a.normalize_key(0), 0)

  def test_IIndexedValue(self):
    for p, idx in uid.items():
      if p == "DateRange": continue
      mv = getSubscriptionAdapter(idx, IMultiplicityAware).multi_valued()
      a = getSubscriptionAdapter(idx, IIndexedValue)
      self.assertEqual(a.indexed_value_for(0), [0,] if mv else 0)

  def test_IMultiplicityAware(self):
    for p, idx in uid.items():
      mv = getSubscriptionAdapter(idx, IMultiplicityAware).multi_valued()
      self.assertEqual(mv, p == "Keyword")
    

class TestBoolean(AqTest):
  def test_lookup(self):
    idx = uid["Boolean"]
    gt = getSubscriptionAdapter(idx, ILookupTreeIndex).tree_for_key
    from ...tree import Set, And, Not
    l0 = gt(False, None); l1 = gt(True, None)
    self.assertTrue(isinstance(l0, Set) ^ isinstance(l1, Set))
    sets = []
    for l in (l0, l1):
      if isinstance(l, Set): sets.append(l.as_set(None))
      else:
        self.assertIsInstance(l, And)
        self.assertIsInstance(l[0], Set)
        self.assertEqual(list(l[0].as_set(None)), [0, 1])
        self.assertIsInstance(l[1], Not)
        self.assertIsInstance(l[1][0], Set)
        sets.append(l[1][0].as_set(None))
    self.assertEqual(sets[0], sets[1])


class TestDateRange(AqTest):
  def test_lookup(self):
    idx = uid["DateRange"]
    gt = getSubscriptionAdapter(idx, ILookupTreeIndex).tree_for_key
    from BTrees.IIBTree import IISet
    from ...interfaces import ITreeEvaluator_Set
    from ...transform import Context
    class Resources(object):
      dids = IISet((0, 1))
      def get_dids(self): return self.dids
    c = Context.make_context(Resources(), ITreeEvaluator_Set, focus=None,)
    for k in range(-1, 3):
      t = gt(k, None)
      ts = c.transform(t)
      self.assertEqual(list(ts), [0, 1] if 0 <= k <= 1 else [0])

  def test_match(self):
    idx = uid["DateRange"]
    match = getSubscriptionAdapter(idx, ITermValueMatch).match
    for r in ((None, None), (-1, None), (0, None), (None, 1), (None, 0),
              (0, 0), (-1, 1)):
      self.assertTrue(match(r, 0))
    for r in ((1, None), (None, -1), (1, 2), (-2, -1)):
      self.assertFalse(match(r, 0))

