# Copyright (C) 2004-2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Bubach, Germany
# see "LICENSE.txt" for details
#       $Id: testAdvancedQuery.py,v 1.3 2019/04/22 05:56:00 dieter Exp $

# this no longer works for Zope 2.12 -- we drop this support
### as specified by "ZopeTestCase.framework"
##import os, sys
##if __name__ == '__main__':
##  execfile(os.path.join(sys.path[0], 'framework.py'))
##else: import framework

from Products.AdvancedQuery import *

from .TestBase import TestCase


class TestFieldIndex(TestCase):

  def testSlicing(self):
    c = self.catalog
    r = c.evalAdvancedQuery(Eq('I1', 'a'), ('I1',))
    # must not raise an exception
    r[1:]

  def testEq(self):
    self._checkQuery(Eq('I1','a'), '13')
    self._checkQuery(Eq('I1','a', filter=True), '13')
    self._checkQuery(Eq('I1','c'), '6')
    self._checkQuery(Eq('I1','x'), '')

  def testLe(self):
    self._checkQuery(Le('I1','a'), '13')
    self._checkQuery(Le('I1','a', filter=True), '13')
    self._checkQuery(Le('I1','b'), '1234')

  def testGe(self):
    self._checkQuery(Ge('I1','b'), '246')
    self._checkQuery(Ge('I1','b', filter=True), '246')

  def testIn(self):
    self._checkQuery(In('I1',('a','c')), '136')
    self._checkQuery(In('I1',('a','c'), filter=True), '136')

  def testBetween(self):
    self._checkQuery(Between('I1','a','b'), '1234')
    self._checkQuery(Between('I1','a','b', filter=True), '1234')

  def testGeneric(self):
    self._checkQuery(Generic('I1', {'query':'a'}), '13')
    self._checkQuery(Generic('I1', {'query':'a'}, filter=True), '13')

  def testIndexed(self):
    self._checkQuery(Indexed('I1'), '12346')

  def testAnd(self):
    self._checkQuery(Eq('I1', 'a') & Eq('I2', 'A'), '1')
    self._checkQuery(Eq('I1', 'a') & ~ Eq('I2', 'A'), '3')
    q = And(Eq('I1', 'c')); q &= ~ Eq('I2', 'A'); self._checkQuery(q, '6')
    self._checkQuery(And(), '123456')
    self._checkQuery(~Eq('I1', 'a') & ~Eq('I2', 'A'), '46')
    
  def testOr(self):
    self._checkQuery(Eq('I1', 'a') | Eq('I2', 'A'), '1235')
    self._checkQuery(Or(), '')
    # many or
    q = Or(); qb = Eq('I1', 'a')
    for i in range(10): q |= qb
    self._checkQuery(q, '13')

  def testFilter(self):
    self._checkQuery(Filter("I1", lambda iv: iv == "a"), "13")
    self._checkQuery(Eq("I2", "A") & Filter("I1", lambda iv: iv == "a"), "1")

  # `Not` tested in `testAnd`


class TestKeywordIndex(TestFieldIndex):
  _indexType = "KeywordIndex"
  _multiValued = True

  def testFilter(self):
    self._checkQuery(Filter("I1", lambda iv: "a" in iv), "13")
    self._checkQuery(Eq("I2", "A") & Filter("I1", lambda iv: "a" in iv), "1")


    
class TestSorting(TestCase):
  def testSortSmallIndex(self):
    C = self.catalog
    self._check(C.evalAdvancedQuery(And(), ('I1', ('I2','desc'))), '314265', False)
    self._check(C.evalAdvancedQuery(Eq('I1', 'x'), ('I1', ('I2','desc'))), '', False)

  def testSortLargeIndex(self):
    C = self.catalog; folder = self.folder
    for i in range(7,100): self._addObject(folder, i, repr(i), None)
    q = Eq('I2', 'A')
    self._check(C.evalAdvancedQuery(q, ('I1',)), '125', False)
    self._check(C.evalAdvancedQuery(q, (('I1','desc'),)), '215', False)
    



class TestIndexIndependant(TestCase):
  '''tests independent from index type.'''
  def testMakeAdvancedQuery(self):
    C = self.catalog
    q = C.makeAdvancedQuery({'I1':'a', 'I2': {'query':'A'},})
    self._check(C.evalAdvancedQuery(q), '1')
    q = C.makeAdvancedQuery({'I1':('a','b'), 'I1_usage': 'range:min:max',})
    self._check(C.evalAdvancedQuery(q), '1234')

  def testStr(self):
    self.assertEqual(str(Eq('I1','a')), "I1 = 'a'")
    self.assertEqual(str(Le('I1',1)), 'I1 <= 1')
    self.assertEqual(str(Ge('I1',1)), 'I1 >= 1')
    self.assertEqual(str(MatchGlob('I1',1)), 'I1 =~ 1')
    self.assertEqual(str(MatchRegexp('I1',1)), 'I1 =~~ 1')
    self.assertEqual(str(Generic('I1',1)), 'I1 ~~ 1')
    self.assertEqual(str(In('I1',(1,2))), 'I1 in (1, 2)')
    self.assertEqual(str(Between('I1',1,2)), '1 <= I1 <= 2')
    self.assertEqual(str(Indexed('I1')), 'Indexed(I1)')
    self.assertEqual(str(~Le('I1',1)), '~(I1 <= 1)')
    self.assertEqual(str(Le('I1',1) & Eq('I2',2)), '(I1 <= 1 & I2 = 2)')
    self.assertEqual(str(Le('I1',1) | Eq('I2',2) | Eq('I3',3)), '(I1 <= 1 | I2 = 2 | I3 = 3)' )

  def testRanking_Sum(self):
    self._checkRank(
               RankByQueries_Sum,
               ((In('I1', ('b', 'c')),1), (Eq('I2','A'),1)),
               '221141615130'
               )
    self._checkRank(
               RankByQueries_Sum,
               ((Eq('I1', 'b'),1), (Eq('I2','X'),1)),
               '214110306050'
               )
    self._checkRank(
               RankByQueries_Sum,
               ((Eq('I1', 'x'),1), (Eq('I2','B'),1)),
               '314110206050'
               )

  def testRanking_Max(self):
    self._checkRank(
               RankByQueries_Max,
               ((In('I1', ('b', 'c')),1), (Eq('I2','A'),1)),
               '112141615130'
               )
    self._checkRank(
               RankByQueries_Max,
               ((Eq('I1', 'b'),2), (Eq('I2','A'),1)),
               '224211513060'
               )

  def _checkRank(self, ranker, rs, should):
    all = And()
    C = self.catalog; eval = C.evalAdvancedQuery
    rl = []; c = C._catalog
    for r in eval(all, (ranker(*rs), 'I1', 'I2')):
      rl.append(c.paths[r.data_record_id_])
      rl.append(repr(int(r.data_record_score_[0])))
    self.assertEqual(''.join(rl), should)


class TestMatching(TestCase):
  _stringType = 1

  def testGlob(self):
    self._checkQuery(MatchGlob('I1','*'), '12346')

  def testRegexp(self):
    self._checkQuery(MatchRegexp('I1','.'), '12346')
