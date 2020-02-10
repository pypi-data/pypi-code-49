# Copyright (C) 2004-2019 by Dr. Dieter Maurer, Illtalst. 25, D-66571 Bubach, Germany
# see "LICENSE.txt" for details
#       $Id: TestBase.py,v 1.2 2019/04/22 05:56:00 dieter Exp $
'''Test base class.

This is a `zope.testrunner` testsuite.
'''

from Acquisition import Implicit

from Testing.ZopeTestCase import ZopeTestCase, installProduct

from .layer import AqTest

installProduct('ZCatalog', 1)
installProduct('PluginIndexes', 1)
installProduct('AdvancedQuery', 1)

class Layer(ZopeTestCase.layer, AqTest.layer): pass

class TestCase(AqTest, ZopeTestCase):
  layer = Layer

  _indexType = 'FieldIndex'
  _multiValued = False

  def afterSetUp(self):
    folder = self.folder
    folder.manage_addProduct['ZCatalog'].manage_addZCatalog('Catalog','')
    catalog = self.catalog = folder.Catalog
    catalog.manage_addIndex('I1', self._indexType)
    catalog.manage_addIndex('I2', self._indexType)
    self._addObject(folder, 1, 'a', 'A')
    self._addObject(folder, 2, 'b', 'A')
    self._addObject(folder, 3, 'a', 'B')
    self._addObject(folder, 4, 'b', 'B')
    self._addObject(folder, 5, None, 'A')
    self._addObject(folder, 6, 'c', None)

  def _addObject(self, dest, id, a1, a2):
    id = repr(id)
    if self._multiValued:
      def c(v): return v if v is None else (v,)
    else:
      def c(v): return v
    setattr(dest, id, _Object(id, c(a1), c(a2))); obj = getattr(dest, id)
    obj.indexObject()

  def _checkQuery(self, query, should):
    '''check that the result *query* equals *should*.

    *should* is a sequence of digits (representing ids).
    '''
    C = self.catalog
    return self._check(C.evalAdvancedQuery(query), should)

  def _check(self, result, should, order=True):
    c = self.catalog._catalog
    ids = [c.paths[r.data_record_id_] for r in result]
    if order: ids.sort()
    self.assertEqual(''.join(ids), should)



class _Object(Implicit):
  def __init__(self, id, a1, a2):
    self.id = id
    if a1 is not None: self.I1 = a1
    if a2 is not None: self.I2 = a2

  def indexObject(self):
    self.Catalog.catalog_object(self, uid=self.id)
