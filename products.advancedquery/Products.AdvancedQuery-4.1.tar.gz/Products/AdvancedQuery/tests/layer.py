# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Bubach, Germany
# see "LICENSE.txt" for details
#       $Id: layer.py,v 1.1 2019/04/22 05:56:00 dieter Exp $
"""Layer to get independent of external configuration of the component registry."""
from contextlib import contextmanager
from unittest import TestCase

from zope import component
from zope.component import globalregistry, _api
from zope.component.globalregistry import \
     globalSiteManager, BaseGlobalComponents
from zope.component.hooks import getSite, setSite
from zope.configuration.xmlconfig import file as load_config

import Products.AdvancedQuery as aq

class AqzcmlLayer(object):
  context = None

  @classmethod
  def setUp(cls):
    cls.reg = globalSiteManager
    # set up new component registry
    globalregistry.base = globalregistry.globalSiteManager = BaseGlobalComponents("base")
    # `_api` caches `base` -- invalidate
    _api.base = None
    # in a Plone environment `setSite` has been called and cached `base`
    #   reset
    cls.site = getSite()
    setSite(None)
    # initialize
    cls.context = load_config("meta.zcml", component, cls.context)
    # our zcml
    cls.context = load_config("configure.zcml", aq, cls.context)

  @classmethod
  def tearDown(cls):
    # restore former registry
    globalregistry.base = globalregistry.globalSiteManager = cls.reg
    # `_api` caches `base` -- invalidate
    _api.base = None
    setSite(cls.site)
    cls.context = None


class AqTest(TestCase):
  layer = AqzcmlLayer

  # `TestCase.subTest` currently does not work due to
  #   "https://bugs.python.org/issue34900" (fixed in Python 3.9) and
  #   "https://github.com/zopefoundation/zope.testrunner/issues/91"
  # We overwrite to work around these issues
  subtest_descs = ()
  @contextmanager
  def subTest(self, msg=None, **params):
    """unlike `TestCase.subTest`, we fail for the first failure."""
    saved_stds = self.subtest_descs
    adds = []
    if msg is not None: adds.append("[%s]" % msg)
    for k in sorted(params):
      adds.append("(%s=%r)" % (k, params[k]))
    if adds:
      self.subtest_descs += tuple(adds)
    try:
      yield
    except Exception: raise
    else: self.subtest_descs = saved_stds

  def __str__(self):
    return " ".join((super(AqTest, self).__str__(),) + self.subtest_descs)

