# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: tests.py,v 1.1 2019/04/22 05:55:58 dieter Exp $
from Products.PluginIndexes.FieldIndex.FieldIndex import FieldIndex
from Products.PluginIndexes.KeywordIndex.KeywordIndex import KeywordIndex
from Products.PluginIndexes.DateRangeIndex.DateRangeIndex import DateRangeIndex

from Products.AdvancedQuery import Generic, Eq, And, Or, Not, Filter, \
     Le, Ge, Between, In, MatchGlob, MatchRegexp
from Products.AdvancedQuery.tests.layer import AqTest

from ....transform import OptimizerContext
from ....interfaces import IQueryOptimizerChain
from ... import getSubscriptionAdapter
from . import IQueryOptimizerChain

class _UnknownIndex(FieldIndex):
  """An index which is not adaptable by our conditional adapters."""
  def unindex_object(*args, **kw): pass
  def query_index(*args, **kw): pass


class _ContextMockup(object):
  idxs = dict(fi=FieldIndex("fi"),
              ui=_UnknownIndex("ui"),
              ki=KeywordIndex("ki"),
              di=DateRangeIndex("di", "s", "u"),
              )

  def get_index(self, idx): return self.idxs[idx]

context = OptimizerContext.make_context(_ContextMockup(), IQueryOptimizerChain)


class TestBase(AqTest):
  def optimize(self, q):
    return context.optimize(q)

class TestConvertGeneric(TestBase):
  def optimize(self, spec, filter=False, idx="fi"):
    return super(TestConvertGeneric, self).optimize(Generic(idx, spec, filter))

  def test_validity(self):
    for s in (
      dict(operator="and", range="abc"),
      dict(operator="and", match="abc"),
      dict(range="abc", match="abc"),
      ):
      with self.subTest(spec=s):
        with self.assertRaises(ValueError):
          self.optimize(s)

  def test_unchanged(self):
    for s in (
      dict(operator="and"),
      dict(operator="and", query=(1, 2)),
      {'not':1},
      dict(match="xyz", query=1,),
      dict(match="glob"),
      ):
      with self.subTest(spec=s):
        self.assertTrue(self.optimize(s)[1])

  def test_converted(self):
    for qc in (Eq, Le, Ge, MatchGlob, MatchRegexp, Between, In,):
      args = ("1", "2") if qc is Between else (("1", "2"),) if qc is In else ("1",)
      q = qc("fi", *args)
      with self.subTest(q=str(q)):
        qo = self.optimize(q.make_spec())[0]
        self.assertEqual(str(q), str(qo))
        self.assertFalse(qo.filter)
        qo = self.optimize(q.make_spec(), True)[0]
        self.assertIsInstance(qo, Filter)


class TestFilter(TestBase):
  def optimize(self, spec, idx="fi"):
    return super(TestFilter, self).optimize(Generic(idx, spec, True))[0]

  def test_unfilterable(self):
    for (spec, idx) in ((dict(query=1), "ui"), (dict(level=0), "fi")):
      with self.subTest(spec=spec, idx=idx):
        q = self.optimize(spec, idx)
        self.assertFalse(q.filter)

  def test_empty(self):
    self.assertIsInstance(self.optimize({}), Or)

  def test_fi(self):
    with self.subTest(idx="fi"):
      self._test("fi", ('0', '12.3', '14.5', '9'))

  def test_ki(self):
    with self.subTest(idx="ki"):
      self._test("ki", (('0', '12.3', '14.5', '9'), ('0', '9')))

  def _test(self, idx, idx_values):
    def check(filter, idx_val, cmp):
      cmp_val = idx_val if isinstance(idx_val, tuple) else (idx_val,)
      self.assertEqual(filter(idx_val), cmp(cmp_val))
    def checks(spec, cmp):
      with self.subTest(range=range):
        q = self.optimize(spec, idx=idx)
        filter = getattr(q, "filter", lambda v: False)
        for v in idx_values:
          with self.subTest(idx_value = v):
            check(filter, v, cmp)
    # ranges
    for (min, max) in ((None, '2'), ('1', None), ('1', '2')):
      keys = []; range = []
      if min: keys.append(min); range.append("min")
      if max: keys.append(max); range.append("max")
      range = ":".join(range)
      checks(dict(query=keys, range=range),
             lambda vs: any(
               (min is None or min <= v) and (max is None or v <= max)
               for v in vs))
    # range + not
    checks({"query":('0', '9'), "range":"min:max", "not":('0', '9')},
           lambda vs: any('0' <= v <= '9' for v in vs)
           and all(n not in vs for n in ('0', '9')))
    # match
    for m in ("glob", "regexp"):
      checks(dict(query=('12.*', '14.*'), match=m),
             lambda vs: any(v.startswith('1') for v in vs) # this it not fit in general
             )
    # match + not
    checks({"query":('12.*', '14.*'), "match":"glob", "not":"12.3"},
           lambda vs: any(v.startswith("1") for v in vs) and "12.3" not in vs)
    # pure "not"
    checks({"not": ('0', '9')},
           lambda vs: all(n not in vs for n in ("0", "9")))
    # "and", "or", "not"
    query = ("0", "12.3")
    for op in ("and", "or"):
      for nots in ((), ('9',)):
        checks({"query":query, "operator":op, "not":nots},
               lambda vs, comb=all if op == "and" else any:
               comb(k in vs for k in query) and
               all(n not in vs for n in nots))

  def test_di(self):
    def match(iv, t):
      s, u = iv
      return (s is None or s <= t) and (u is None or t <= u)
    ivs = (None, None), (0, None), (None, 0), (0, 1),
    def check(keys, nots=(), op = "or"):
      if not isinstance(keys, tuple): keys = keys,
      spec = {"query":keys, "operator":op, "not":nots}
      with self.subTest(spec=spec):
        q = self.optimize(spec, idx="di")
        comb = all if op == "and" else any
        for iv in ivs:
          with self.subTest(iv=iv):
            self.assertEqual(q.filter(iv),
                             comb(match(iv, t) for t in keys)
                             and all(not match(iv, n) for n in nots)
                             )
    # single values
    check(-1); check(0); check(2)
    # or
    check((0, 2)); check((0, 2), nots=(2,))
    # and
    check((0, 1), op="and"); check((0, 2), op="and")
    check((0, 1), nots=(2,), op="and")


def TestUnfold(TestBase):
  def optimize(self, q):
    return super(TestUnfold, self).optimize(q)[0]

  @classmethod
  def setUpClass(cls):
    cls.q = Eq("fi", 0)

  def test_not_not(self):
    q = self.q
    self.assertIs(self.optimize(~~q), q)

  def test_not_empty(self):
    for op, cop in ((And, Or), (Or, And)):
      with self.subTest(op=op):
        q = op()
        oq = self.optimize(q)
        self.assertFalse(oq)
        self.assertIsInstance(oq, cop)

    def test_op_op(self):
      q = self.q
      for op in (And, Or):
        with self.subTest(op=op):
          oq = self.optimize(op(q, op()))
          self.assertIsInstance(oq, op)
          self.assertEqual(len(oq), 1)
          self.assertIs(oq[0], q)

  def test_op_empty_cop(self):
    for op, cop in ((And, Or), (Or, And)):
        with self.subTest(op=op):
          oq = self.optimize(op(q, cop()))
          self.assertIsInstance(oq, cop)
          self.assertFalse(oq)
