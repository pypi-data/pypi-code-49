# Copyright (C) 2003-2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Bubach, Germany
# see "LICENSE.txt" for details
#       $Id: AdvancedQuery.py,v 1.3 2019/04/22 05:55:55 dieter Exp $
'''Advanced Query

see 'AdvancedQuery.html' for documentation.
'''
from copy import copy

from ExtensionClass import Base

from BTrees.IIBTree import IISet, IITreeSet

from .tree import Leaf, Container, And, Or, Not



##############################################################################
## Query classes

class _BaseQuery(Base):
  ''''Query' base class.'''
  
  # Interface
  def __str__(self):
    raise NotImplementedError

  def __and__(self, other):
    '''self & other'''
    if isinstance(self,And): r = self._clone()
    else: r = And(self)
    r.addSubquery(other)
    return r

  def __or__(self, other):
    '''self | other'''
    if isinstance(self,Or): r = self._clone()
    else: r = Or(self)
    r.addSubquery(other)
    return r

  def __invert__(self):
    '''~ self'''
    return Not(self)

  def _clone(self):
    return copy(self)

  # auxiliary to provide useful information in exception reports
  def __repr__(self):
    r = super(_BaseQuery, self).__repr__()
    try: readable = str(self)
    except Exception: pass
    else: r = r[:-1] + "[%s]" % readable + r[-1]
    return r


class _LeafQuery(_BaseQuery, Leaf): pass

class _IndexBasedQuery(_LeafQuery):
  def __init__(self, idx, *args, **kw):
    self.index = idx


class _TermQuery(_IndexBasedQuery):
  # to be overridden by derived classes
  _functor= None # transform term into query ("None" means identity)
  _OP= None     # used for display

  def __init__(self, idx, term, filter=False):
    self.index = idx
    self.term = term
    self.filter = filter

  def __str__(self):
    return '%s %s %r' % (self.index, self._OP, self.term)

  def make_spec(self):
    """transform into query spec."""
    term = self.term
    functor = self._functor
    return functor(term) if functor else term

class _ZTermQuery(_TermQuery):
  """`_TermQuery` (directly) supported by `ZCatalog`.

  This is in contrast to an `AdvancedQuery` query extension.
  """

class _ExplicitTermQuery(_ZTermQuery):
  """the terms are explicitly specified, not computed."""

class _ComputedTermQuery(_TermQuery):
  """the effective terms are computed."""

class Eq(_ExplicitTermQuery):
  '''idx = term'''
  _OP = '='
  def _functor(self, term): return (term,)

class Le(_ComputedTermQuery, _ZTermQuery):
  ''' idx <= term'''
  _OP = '<='
  def _functor(self,term): return {'query':term, 'range':'max'}

class Ge(_ComputedTermQuery, _ZTermQuery):
  ''' idx >= term'''
  _OP = '>='
  def _functor(self,term): return {'query':term, 'range':'min'}

class MatchGlob(_ComputedTermQuery):
  '''idx = term'''
  _OP = '=~'
  def _functor(self,term): return {'query':term, 'match':'glob'}

class MatchRegexp(_ComputedTermQuery):
  '''idx = term'''
  _OP = '=~~'
  def _functor(self,term): return {'query':term, 'match':'regexp'}

class Generic(_TermQuery, _ZTermQuery):
  _OP = '~~'


class In(_ExplicitTermQuery):
  _OP = 'in'
  def _functor(self,term): return tuple(term)


class Between(_ComputedTermQuery, _ZTermQuery):
  '''lb <= idx <= ub'''
  def _functor(self, term): return {'query':term, 'range':'min:max',}

  def __init__(self, idx, lb, ub, filter=False):
    super(Between,self).__init__(idx, (lb,ub), filter)
   
  def __str__(self):
    t = self.term
    return '%r <= %s <= %r' % (t[0], self.index, t[1])


class Indexed(_IndexBasedQuery):
  def __init__(self, idx):
    self.index = idx

  def __str__(self): return 'Indexed(%s)' % self.index


class Filter(_IndexBasedQuery):
  def __init__(self, idx, filter):
    """filter out objects not accepted by *filter*.

    *filter* is called with the object's indexed value and should return
    `True` (accept) or `False`.

    Note: you must precisely know how *idx* determines an object's
    indexed value to use this properly.
    """
    super(Filter, self).__init__(idx)
    self.filter = filter

  def __str__(self):
    return "%s/%r" % (self.index, self.filter)

class _CombiningQuery(_BaseQuery, Container):
  _OP = None



class Not(_CombiningQuery, Not):
  '''~(query)'''
  def __str__(self):
    return '~(%s)' % str(self[0])


class _CompositeQuery(_CombiningQuery):
  # to be overridden
  _OP = None

  def __str__(self):
    return (
      '(%s)' % (' %s ' % self._OP).join(map(str, self)) if self
      else "(%s[])" % self._OP
      )

  addSubquery__roles__ = None # Public
  def addSubquery(self,query):
    assert isinstance(query,_BaseQuery)
    self.append(query)
    return self

  def _clone(self):
    return self.__class__(*self)

      
class And(_CompositeQuery, And):
  _OP = '&'
  __iand__ = _CompositeQuery.addSubquery


class Or(_CompositeQuery, Or):
  _OP = '|'
  __ior__ = _CompositeQuery.addSubquery


class LiteralResultSet(_LeafQuery):
  '''Query given by its result set.

  Used to restrict previous query results.
  '''
  def __init__(self, set):
    '''query returning *set*.

    *set* must be an 'IISet' or 'IITreeSet' of catalog record ids.
    '''
    if not isinstance(set, (IISet, IITreeSet)): set = IITreeSet(set)
    self.set = set

  def __str__(self): return 'LiteralResultSet(%s)' % self._set
