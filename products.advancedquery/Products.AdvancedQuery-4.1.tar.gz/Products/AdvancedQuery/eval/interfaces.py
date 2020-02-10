# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Bubach, Germany
# see "LICENSE.txt" for details
"""Evaluation related interfaces."""

from zope.interface import Interface

from BTrees.Interfaces import IKeyed

from .transform import IOptimizer, IOrdered, IOptimizerChain, ITransformer


class IQueryContext(Interface):
  """`ZCatalogWrapper` performing the evaluation."""
  # external API
  def eval(query, restricted, **kw): "the set of documents matching *query*."
  # internal resource API
  def get_index(name): "the index with *name*."
  def index_names(): "the names of available indexes."
  def get_indexes(filter=None): "the indexes, filtered by *filter*."
  def get_dids(): "the set of (known) document ids."


class IQueryRestrict(Interface):
  """Catalog specific query restriction.

  You must register corresponding adapters for
  `CMFCore` and `Plone` catalogs in order to get their
  restrictions for unpriviledged users.
  """
  def restrict(query, **kw):
    """return *query* potentially with additional restrictions."""


class IQueryOptimizerChain(IOptimizerChain):
  """Global syntactic query optimization.

  This is the first step of the query evaluation trying
  to syntactically simplify the query.

  In the standard setup, it is a chain of `IQueryNodeOptimizer`s.
  The standard setup registers node optimizers e.g. for
  the elimination of one element `And` and `Or` queries, the flattening
  of nested `And`, `Or` or `Not` queries and the propagation of empty
  `And` or `Or` queries.
  A `CompositeIndex` optimization could be handled here, too
  (but the standard setup does not do this).
  """

class IQueryNodeOptimizer(IOptimizer, IOrdered):
  """Local syntactic query optimization.

  Typically, the `IQueryOptimizer` chain is based on these
  optimizers.

  In the standard setup, optimizers of this type are registered
  for the following cases. They are executed in this order.
   * convert simple `Generic` queries to more explicit queries
   * eliminate `filter=True` by converting into an explicit `Filter`
     or set `filter=False` depending on whether the index supports filtering.
   * unfold nested queries of the same type,
     e.g. transform "~~q" into "q", or
     "q1 & (q2 & q3)" into "q1 & q2 & q3)".
   * try to propagate empty subqueries, e.g.
     transform `~And()` into `Or()`
     or `q1 & Or()` into `Or()`.
   * eliminate one element `And` or `Or` queries

  The corresponding optimizers used `order` values
  in the range of 0 and 99.

  If `CompositeIndex`es are used in your setup, then
  you may consider to register a corresponding optimizer.
  Its `order` would like be higher than that used by the standard
  optimizers (such that this optimizer sees already a normalized
  state).
  """


class IQueryConverter(ITransformer):
  """transform the query into an evaluation tree."""


class ITreeOptimizerChain(IOptimizerChain):
  """Global evaluation tree optimization. """

class ITreeNodeOptimizer(IOptimizer, IOrdered):
  """Local evaluation tree optimization."""

class ITreeEvaluator_Set(ITransformer):
  """Evaluation tree evaluation. """


class ITreeEvaluator_ISearch(ITransformer):
  """evaluate an evaluation tree into an `ISearch`."""


##############################################################################
## (Adapter) interfaces related to filtering
class IFilterIndex(Interface):
  """does the index support filtering?."""
  def make_filter(query):
    """transform *query* into (typically) a `Filter` query or return `None`."""

class IIndexedValue(Interface):
  def indexed_value_for(did):
    """the indexed value for *did* or `None`."""

class IMultiplicityAware(Interface):
  def multi_valued():
    """`True`, if objects can be indexed under different values.

    If the index can be (subscription) adapted to `IKeyedIndex`
    and `multi_valued` is `False`, then for any document, there
    is at most one key under which the document is indexed.
    This is used for `not` optimizations.

    If the index can be (subscription) adapted to `IIndexedValue`,
    then `multi_valued` specifies whether the indexed
    value should be considered atomic (`multi_valued == False`)
    or a sequence of values (`multi_valued == True`).
    """


class ITermValueMatch(Interface):
  """Interface to indicate that query terms and indexed terms differ."""
  def match(self, indexed_value, query_term):
    """does *query_term* match *indexed_value*?"""


##############################################################################
## (Adapter) interfaces for query converters

class IIndexed(Interface):
  def get_dids(): "the set of indexed document ids."


class IKeyedIndex(IKeyed):
  def keys(min=None, max=None, exclude_min=False, exclude_max=False):
    "the keys >= *min*, <=  *max*."

class IKeyNormalizingIndex(Interface):
  def normalize_key(key): "key -> normalized key"

class ILookupIndex(Interface):
  def dids_for_key(key): "the document ids for *key* (as a set)."

class ILookupTreeIndex(Interface):
  def tree_for_key(key, context=None): "the lookup tree for *key*."
