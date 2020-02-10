# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: tests.py,v 1.2 2020/02/10 08:31:41 dieter Exp $
from BTrees.IIBTree import IISet
from BTrees.OOBTree import OOSet

from Products.PluginIndexes.unindex import UnIndex
from Products.PluginIndexes.FieldIndex.FieldIndex import FieldIndex
from Products.PluginIndexes.KeywordIndex.KeywordIndex import KeywordIndex
from Products.PluginIndexes.DateRangeIndex.DateRangeIndex import DateRangeIndex
from Products.PluginIndexes.PathIndex.PathIndex import PathIndex
from Products.PluginIndexes.TopicIndex.TopicIndex import TopicIndex
from Products.ZCTextIndex.ZCTextIndex import ZCTextIndex, PLexicon
from Products.ZCTextIndex.Lexicon import Splitter

from Products.AdvancedQuery import Generic, Filter, LiteralResultSet, \
     And, Or, Not, MatchGlob, Indexed
from Products.AdvancedQuery.tests.layer import AqTest

from ....interfaces import IQueryConverter
from ....transform import Context
from ....tree import IndexLookup as TLookup, Set as TSet, \
     And as TAnd, Or as TOr, Not as TNot, Filter as TFilter
from ... import getMultiSubscriptionAdapter, ConditionalAdapterFactory
from .. import normalize_spec

from . import KeyedIndexConverter, PureNotIndexConverter, \
     ExplicitIndexConverter, ZTermQueryConverter, \
     SpecConverter, _HandlePureNot, _KeyExpander, IndexedQueryConverter
from .pathindex import PathIndexQueryConverter
from .topicindex import TopicIndexQueryConverter
from .zctextindex import ZCTextIndexQueryConverter

class _O(object):
  """Auxiliary object factory."""
  def __init__(self, **kw): self.__dict__.update(kw)

class _IndexedIndex(UnIndex):
  """Auxiliary `indexed` index."""
  # disable the `unindex_search` adapters
  def query_index(*args): return IISet() 

class _UnknownIndex(_IndexedIndex):
  """Auxiliary index class without adapters)."""
  options = "not", "special", "operator"
  # disable the `unindex_unindex` adapters
  def unindex_object(*args): pass

class _LexiconProvider(object):
  def __getattr__(self, k): return PLexicon("", "", Splitter())

class _Resources(object):
  """Mockup resources."""
  indexes = dict(
    fi=FieldIndex("fi"),
    ki=KeywordIndex("ki"),
    dri=DateRangeIndex("dri", "since", "until"),
    pi=PathIndex("pi"),
    ti=TopicIndex("ti"),
    ii=_IndexedIndex("ii"),
    ui=_UnknownIndex("ui"),
    zcti = ZCTextIndex("zcti", extra=_O(index_type="Cosine Measure"),
                       caller=_LexiconProvider()),
    zcti_o = ZCTextIndex("zcti_o", extra=_O(index_type="Okapi BM25 Rank"),
                       caller=_LexiconProvider()),
    )
  def get_index(self, idx): return self.indexes[idx]

resources = _Resources()


# fill some indexes
IDXS = "fi", "ii",
for i, dv in enumerate("1 123 124 2 21".split()):
  for idx in IDXS:
    resources.get_index(idx).index_object(i, _O(**{idx:dv}))


for idx in ("zcti", "zcti_o"):
  x = resources.get_index(idx)
  for i, dv in enumerate(("d w w0 w1 w2",
                         "d w",
                         "d", "e")):
    x.index_object(i, _O(**{idx:dv}))

pi = resources.get_index("pi")
for i, dv in enumerate("/1/11/111/1 /1/12 /2/21".split()):
  pi.index_object(i, _O(pi=dv))


context = Context.make_context(resources, IQueryConverter, has_focus=False)


class TestAdapterChoice(AqTest):
  def _check(self, idx, spec, adapter=None):
    if idx is None: q = spec; idx = q.index
    else: q = Generic(idx, spec)
    a = getMultiSubscriptionAdapter((resources.get_index(idx), q), IQueryConverter)
    while isinstance(adapter, ConditionalAdapterFactory):
      adapter = adapter.factory
    self.assertIsInstance(a, adapter)

  def test_keyed(self):
    self._check("fi", {"query":"1", "match":"glob"}, KeyedIndexConverter)
  def test_pure_not(self): self._check("ii", {"not":1}, PureNotIndexConverter)
  def test_explicit(self): self._check("ui", {"query":1, "not":1}, ExplicitIndexConverter)
  def test_zterm(self): self._check("ui", {"query":1, "special":1}, ZTermQueryConverter)
  def test_indexed(self): self._check(None, Indexed("ii"), IndexedQueryConverter)
  def test_zcti(self): self._check("zcti", "1", ZCTextIndexQueryConverter)
  def test_zcti_o(self): self._check("zcti_o", "1", ZCTextIndexQueryConverter)
  def test_pi(self): self._check("pi", "1", PathIndexQueryConverter)
  def test_ti(self): self._check("ti", "1", TopicIndexQueryConverter)


class TestTransform(TestAdapterChoice):
  """test the transform does not result in an exception.
  
  We do not try here to check the correctness of the transform.
  """
  def _check(self, idx, spec, adapter=None):
    if idx is None: q = spec; idx = q.index
    else: q = Generic(idx, spec)
    return self._transform(q)

  def _transform(self, q):
    return context.transform(q)
    
  def test_lrs(self):
    self._transform(LiteralResultSet(IISet()))

  def test_and_or(self):
    for q in (And, Or):
      self._transform(q())

  def test_not(self):
    self._transform(Not(Generic("fi", "1")))

  def test_filter(self):
    self._transform(Filter("fi", lambda x: False))


class _SpecConverter(SpecConverter):
  """`SpecConverter` mockup."""

  def _expand_keys(self, index, keys, range, match):
    return OOSet((range or match,))

  def _handle_pure_not(self, index, not_, lookup): return OOSet(("not",)), None


class TestSpecConverter(AqTest):
  def _transform(self, spec, idx="ui"):
    # ensure arguments are strings (as we have strings indexed)
    spec = normalize_spec(spec)
    for k in ("keys", "not"):
      if spec.get(k): spec[k] = tuple(map(str, spec[k]))
    # undo renaming by `normalize_spec`
    if "keys" in spec: spec["query"] = spec.pop("keys")
    index = resources.get_index(idx)
    q = Generic(idx, spec)
    c = _SpecConverter(index, q)
    return c.transform(q, context)
  
  def test_range(self):
    c = self._transform(dict(query=1, range="range"))
    self.assertEqual(c[0]._spec, ("range",))

  def test_match(self):
    c = self._transform(dict(query=1, match="glob"))
    self.assertEqual(c[0]._spec, ("glob",))

  def test_pure_not(self):
    c = self._transform({"not":"1"})
    self.assertIsInstance(c, TAnd)
    self.assertIsInstance(c[0], TOr)
    self.assertEqual(len(c[0]), 1)
    self.assertEqual(c[0][0]._spec, ("not",))
    self.assertIsInstance(c[1], TNot)
    self.assertIsInstance(c[1][0], TOr)
    self.assertEqual(len(c[1][0]), 1)
    self.assertEqual(c[1][0][0]._spec, ("1",))

  def test_and_or(self):
    for op, t in (("and", TAnd), ("or", TOr)):
      with self.subTest(op=op):
        c = self._transform(dict(query=(1, 2), operator=op))
        self.assertIsInstance(c, t)
        self.assertEqual(len(c), 2)
        self.assertEqual(c[0]._spec, ('1',))
        self.assertEqual(c[1]._spec, ('2',))

  def test_empty(self):
    # an empty "and" is explicitly mapped to `Or`
    #  even though this is logically wrong
    c = self._transform(dict(query=(), operator="and"))
    self.assertIsInstance(c, TOr)
    self.assertFalse(c)

  def test_and_not(self):
    with self.subTest("overlapping"):
      c = self._transform({"query":(1, 2), "not":1, "operator":"and"})
      self.assertIsInstance(c, TOr)
      self.assertFalse(c)
    with self.subTest("disjunct"):
      for idx in ("dri", "ki", "ui"):
        with self.subTest(idx=idx):
          c = self._transform(
            {"query":(1, 2), "not":(3, 4, 5), "operator":"and"}, idx)
          self.assertIsInstance(c, TAnd)
          self.assertIsInstance(c[0], TAnd) # checked in `and_or` case
          self.assertIsInstance(c[1], TNot)
          self.assertIsInstance(c[1][0], TOr)
          self.assertEqual(len(c[1][0]), 3) # confident that this corresponds to our `not`
      with self.subTest(idx="fi"):
         c = self._transform(
            {"query":(1, 2), "not":(3, 4, 5), "operator":"and"}, "fi")
         self.assertIsInstance(c, TAnd)
         self.assertEqual(len(c), 2)
         for cc in c:
           self.assertIsInstance(cc, TSet)

  def test_or_not(self):
    with self.subTest(idx="ui"):
      c = self._transform({"query":(1, 2), "not":1}, "ui")
      self.assertIsInstance(c, TAnd)
      self.assertIsInstance(c[0], TOr)
      self.assertEqual(len(c[0]), 1)
      self.assertEqual(c[0][0]._spec, ('2',))
      self.assertIsInstance(c[1], TNot)
      self.assertIsInstance(c[1][0], TOr)
      self.assertEqual(len(c[1][0]), 1)
      self.assertEqual(c[1][0][0]._spec, ('1',))
    with self.subTest(idx="fi"):
      c = self._transform({"query":(1, 2), "not":1}, "fi")
      self.assertIsInstance(c, TOr)
      self.assertEqual(len(c), 1) # confident that this corresponds to key "2"


class TestKeyExpander(AqTest):
  def test_match(self):
    for pat, match in (("1*", "glob"), ("1.*", "regexp")):
      self._check(dict(keys=pat, match=match), "1 123 124")
    for pat, match in (("1*4", "glob"), ("1.*4", "regexp")):
      self._check(dict(keys=pat, match=match), "124")

  def test_range(self):
    fi = resources.get_index("fi")
    keys = fi._index.keys
    for m, M in ((None, "2"), ("2", None), ("1", "2")):
      range = []; query = []
      if m is not None: range.append("min"); query.append(m)
      if M is not None: range.append("max"); query.append(M)
      spec = dict(keys=query, range=":".join(range))
      self._check(spec, keys(m, M))

  def _check(self, spec, result):
    fi = resources.get_index("fi")
    # normalize `result`
    if isinstance(result, str): result = result.split()
    if not isinstance(result, list): result = list(result)
    # normalize `keys`
    keys = spec["keys"]
    if isinstance(keys, str): keys = OOSet((keys,))
    if not isinstance(keys, OOSet): keys = OOSet(keys)
    ke = _KeyExpander()
    with self.subTest(spec=spec):
      self.assertEqual(list(ke._expand_keys(
        fi, keys, spec.get("range"), spec.get("match")
        )), result)


class TestPureNot(AqTest):
  def test_indexed(self, idx="ii"):
    keys, tree = self._handle(idx, ("1",))
    self.assertIsNone(keys)
    self.assertIsInstance(tree, TAnd)
    self.assertIsInstance(tree[0], TSet)
    self.assertIsInstance(tree[1], TNot)
    self.assertIsInstance(tree[1][0], TOr)
    self.assertEqual(tree[1][0][0], "1")

  def test_fi_large_not(self):
    fi = resources.get_index("fi")
    i_keys = fi._index.keys()
    keys, tree = self._handle("fi", i_keys)
    self.assertEqual(list(keys), list(i_keys))
    self.assertIsNone(tree)

  def test_fi_small_not(self):
    self.test_indexed("fi")

  def _handle(self, idx, nots):
    idx = resources.get_index(idx)
    pn = _HandlePureNot()
    return pn._handle_pure_not(idx, nots, lambda x: x)


class TestZCTextIndex(AqTest):
  IDX = "zcti"

  def _transform(self, term=None, q=None):
    if q is None: q = Generic(self.IDX, term)
    return context.transform(q)

  def test_word_sequence(self):
    c = self._transform("d w")
    self.assertIsInstance(c, TAnd)
    self.assertEqual(len(c), 2)
    for cc in c:
      self.assertIsInstance(cc, TOr)
      self.assertIsInstance(cc[0], TSet)

  def test_not(self):
    c = self._transform("d -w")
    self.assertIsInstance(c, TAnd)
    self.assertEqual(len(c), 2)
    self.assertIsInstance(c[0], TOr)
    self.assertIsInstance(c[0][0], TSet)
    self.assertIsInstance(c[1], TNot)

  def test_or(self):
    c = self._transform("d OR w")
    self.assertIsInstance(c, TOr)
    self.assertEqual(len(c), 2)
    for cc in c:
      self.assertIsInstance(cc, TOr)
      self.assertIsInstance(cc[0], TSet)

  def test_glob(self):
    for cls in (Generic, MatchGlob):
      with self.subTest(cls=cls):
        c = self._transform(q=cls(self.IDX, "w*"))
        self.assertIsInstance(c, TOr)
        self.assertEqual(len(c), 4)
        for cc in c: self.assertIsInstance(cc, TSet)

  def test_nested(self):
    c = self._transform("d AND (w1 OR w2)")
    self.assertIsInstance(c, TAnd)
    self.assertIsInstance(c[0], TOr)
    self.assertIsInstance(c[0][0], TSet)
    self.assertIsInstance(c[1], TOr)
    self.assertEqual(len(c[1]), 2)
    for cc in c[1]:
      self.assertIsInstance(cc, TOr)
      self.assertIsInstance(cc[0], TSet)

  def test_phrase(self):
    c = self._transform('"w1 w2"')
    self.assertIsInstance(c, TAnd)
    self.assertEqual(len(c), 2)
    self.assertIsInstance(c[0], TAnd)
    self.assertEqual(len(c[0]), 2)
    for cc in c[0]:
      self.assertIsInstance(cc, TSet)
    self.assertIsInstance(c[1], TFilter)
    f = c[1]._filter
    self.assertTrue(f(0))
    self.assertFalse(f(1))
    
class TestZCTextIndex_Okapi(TestZCTextIndex):
  IDX = "zcti_o"


class TestPathIndex(AqTest):
  def _transform(self, query, **kw):
    return context.transform(Generic("pi", dict(query=query, **kw)))

  def test_and(self):
    c = self._transform("/1", operator="and")
    self.assertIsInstance(c, TAnd)
    # `and` is identical to `or` up to the root

  def test_simple(self):
    c = self._transform("/1")
    self.assertIsInstance(c, TOr)
    self.assertEqual(len(c), 1)
    self.assertIsInstance(c[0], TAnd)
    self.assertEqual(len(c[0]), 1)
    self.assertIsInstance(c[0][0], TSet)

  def test_level(self):
    with self.subTest("too large level"):
      c = self._transform("/1", level=4)
      self.assertIsInstance(c[0], TOr)
      self.assertFalse(c[0])
    with self.subTest("small level"):
      c = self._transform("/11", level=1)
      self.assertIsInstance(c[0], TAnd)
      self.assertEqual(len(c[0]), 1)

  def test_query_level(self):
    c = self._transform((("/1", 4),))
    self.assertIsInstance(c[0], TOr)
    self.assertFalse(c[0])
    
  def test_negative_level(self):
    c = self._transform("/1", level=-1)
    self.assertIsInstance(c[0], TOr)
    self.assertEqual(len(c[0]), 4)

# TopicIndex is sufficiently simple that no explicit test is required
