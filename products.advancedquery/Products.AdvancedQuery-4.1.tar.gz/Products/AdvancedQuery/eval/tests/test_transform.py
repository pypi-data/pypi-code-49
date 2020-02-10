# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: test_transform.py,v 1.1 2019/04/22 05:56:00 dieter Exp $
from zope.component import getGlobalSiteManager as gsm

from Products.AdvancedQuery.tests.layer import AqTest

from ..transform import OptimizerContext, IOptimizer

class _O(object): pass # mockup object

class Optimizer(object):
  called = 0
  def optimize(self, o, context):
    self.called += 1
    return o, True

class TestOptimizerCache(AqTest):
  def setUp(self):
    self.optimizer = Optimizer()
    self.ofact = lambda o: self.optimizer
    gsm().registerSubscriptionAdapter(self.ofact, (None,), IOptimizer)
    self.context = OptimizerContext.make_context(None, IOptimizer, param=1)

  def tearDown(self):
    gsm().unregisterSubscriptionAdapter(self.ofact, (None,), IOptimizer)

  def test_cached(self):
    o = _O()
    context = self.context; opt = self.optimizer
    context.optimize(o)
    self.assertEqual(opt.called, 1)
    context.optimize(o)
    self.assertEqual(opt.called, 1)

  def test_uncached(self):
    o = _O()
    context = self.context; opt = self.optimizer
    context.optimize(o)
    self.assertEqual(opt.called, 1)
    context.push(param=2).optimize(o)
    self.assertEqual(opt.called, 2)
    context.push(param=2).optimize(o) # must be cached
    self.assertEqual(opt.called, 2)
    context.optimize(_O())
    self.assertEqual(opt.called, 3)

