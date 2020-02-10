# Copyright (C) 2003-2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Bubach, Germany
# see "LICENSE.txt" for details
#       $Id: __init__.py,v 1.4 2019/04/22 05:55:55 dieter Exp $
'''Advanced Query

see 'AdvancedQuery.html' for documentation.
'''

from AccessControl import allow_module as _allow_module, ClassSecurityInfo

try: from AccessControl.class_init import InitializeClass
except ImportError: from Globals import InitializeClass

from .AdvancedQuery import Eq, In, Le, Ge, \
     MatchGlob, MatchRegexp, \
     Between, Not, And, Or, Generic, Indexed, Filter, \
     _CompositeQuery, LiteralResultSet

from .eval import eval as _eval, _notPassed

from .ranking import RankByQueries_Sum, RankByQueries_Max


############################################################################
## Security
_allow_module('Products.AdvancedQuery')
_s = ClassSecurityInfo(); _s.declarePublic('addSubquery')
_CompositeQuery._s = _s; InitializeClass(_CompositeQuery)
del _CompositeQuery


############################################################################
## ZCatalog extension
def _makeAdvancedQuery(self, catalogSearchSpec):
  '''advanced query corresponding to *catalogSearchSpec* (a dictionary).'''
  q = And(); get = catalogSearchSpec.get
  for i in self.Indexes.objectIds():
    vi = get(i)
    if vi is None or vi == '': continue
    # The condition below checks for an old style spec
    if not (isinstance(vi, dict) and vi.get('query') is not None
            or getattr(vi, 'query', None) is not None):
      usage = get(i+'_usage')
      if usage is not None:
        if not usage.startswith('range:'):
          raise ValueError('unsupported usage spec: %s' % usage)
        vi = {'query' : vi, 'range' : usage[6:]}
    q.addSubquery(Generic(i,vi))
  return q

def _evalAdvancedQuery(self, query, sortSpecs=(), withSortValues=_notPassed, **kw):
  # no docstring - we do not want this to be publishable
  return _eval(self, query, sortSpecs, withSortValues, restricted=True, **kw)

from Products.ZCatalog.ZCatalog import ZCatalog
ZCatalog._unrestrictedEvalAdvancedQuery = _eval
ZCatalog.evalAdvancedQuery = _evalAdvancedQuery
ZCatalog.makeAdvancedQuery = _makeAdvancedQuery
del ZCatalog
