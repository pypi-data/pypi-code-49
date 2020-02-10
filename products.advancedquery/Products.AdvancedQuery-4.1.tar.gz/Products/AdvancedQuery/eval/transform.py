# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Bubach, Germany
# see "LICENSE.txt" for details
"""Adapter based tree transformers.

The module contains a small frameworf for adapter based tree
transformers.

Introduction
============

A transformer transforms the tree either in another tree
of the same kind, we speak then of "optimizer", or into something
else, we speak then of "conversion" (it the result is again tree like)
or "evaluation" (if the result is elementary).


Characteristics
===============

All transformers supported by this framework have some
common characteristics.

Process
_______

A transformer of a tree node *t* always happens in a context *c*
and an environment *e*. *e* is the variable part of *c* (which is otherwise
constant across the transformer). The context gives the transformer
access to relevant resources and parameters.

A transformer of *t* typically transforms subnodes and combines
their result. Subnodes are typically transformed via the same
kind of transform; however, the parent can choose a different transform.
To further control the subnode transformer, the parent can _push
new environment settings to the context.


Identification
--------------

A transformer type is uniquely identified by a transformer
specification (short `tspec`). This is an interface.
Transformers for this type are registered as subscription adapters
with this interface as the provided interface.

The actual transformer at node *t* is obtained
by adapting *t* to the given interface with the given name.


Interfaces
----------

All transformers provide an interface derived from `ITransformer`.
This has one method `transform` with the node to be transformed
and the transformer context as parameters. It returns
the transformer result or (in the optimizer case)
an indication that nothing changed.


Context
=======

The transformer context encapsulates relevant resources
for the transformers. Among them is a variable "environment" (called `env`)
containing a set of parameters with their current values.
Apart from `env`, the context is constant; those parts provide access
to general resources such a indexes.

A context provides `IContext`. Its `transform` method has
the tree node to be transformed as parameter and in addition optional
keyword arguments to update the effective environment to be used by
the transform. It returns either the transformer result alone
or (for optimizers) combined with an "unchanged" indication.


Optimizer
=========

For optimizers, it can be important to know that
an optimizing transformer actually has changed something,
as thin the case, the transformer may have caused new optimizer
kinds (already performed earlier) or made other kinds (formerly possible)
inadequate.
Therefore, optimazations use a specialized context. Its `transform` method
returns a pair *transformed tree*, *unchanged*.

In order to make the reapplication of an optimizing transformer
more efficient, the specialized optimizer context caches
the result of former transformers and thereby assumes that
the result of any transformer kind with fixed environment is
idempotent (which means that a second transformer will not change
the result).
"""
from weakref import WeakKeyDictionary

from zope.interface import Interface, Attribute, implementer
from zope.schema import Int
from zope.component import getAdapter, queryAdapter, getSiteManager

from ..tree import Container

from .adapter import getSubscriptionAdapter, querySubscriptionAdapter


###########################################################################
###  Interfaces

class ITransformer(Interface):
  """A general transformer."""

  def transform(t, context):
    """transform tree (node) *t* in *context*."""


class IOptimizer(Interface):
  def optimize(t, context):
    """optimize tree (node) *t* in *context*.
    
    The result is either the optimized tree, `True` to indicate
    the *t* has already been optimized or (for special cases only)
    a tuple with detailed information.
    """


class IOrdered(Interface):
  """Mixin interface to implement `IOrderedOptimizerChain`."""
  order = Int(description=u"the order in which the optimizers are applied")


class IOptimizerChain(IOptimizer):
  """an optimizer optimizing by applying a chain of (ordered) optimizers."""
  sub_tspec = Attribute(u"""
    Optioanl attribute to specify the `tspec` for the component optimizers.

    If missing or `None`, the subscription adapters registered
    for the chain, tree pair under the current transformation name
    determine the component optimizers.
    """)


class IContext(Interface):
  """A general transformer context."""
  def transform(t, **env_params):
    """transform tree (node) *t* in a new environment updated by *env_params*.

    If *env_params* contains `tspec`, then this specifies the
    new transformer kind to be used. Otherwise, the one in the former
    environment is used.
    """

class IOptimizerContext(IContext):
  """Spechial caching context for optimizers.

  Notes:
  
  All participating optimizer kinds must lead to
  idempotent results (with fixed environment).

  All values used in the environment must be hashable.
  """
  def optimize(t, **env_params):
    """optimize tree (node) *t*  in a new environment updated by *env_params*.

    Return the pair *optimized*, *unchanged*.
    """


#############################################################################
## Environment

class Stacked(object):
  """Auciliary class to implement object stacks."""
  parent = None

  @property
  def root(self):
    return self.__dict__.get("root", self)

  @root.setter
  def root(self, root): self.__dict__["root"] = root

  def _push(self, o):
    o.parent = self
    o.root = self.root
    return o


class _Environment(Stacked):
  """Auxiliary class to implement the transformer environment."""
  def __init__(self, params={}, parent=None):
    self.keys = parent.keys if parent is not None else sorted(params.keys())
    self.params = params

  def __getitem__(self, k):
    if k not in self.keys: raise KeyError(k)
    e = self
    while True:
      if k in e.params: return e.params[k]
      e = e.parent

  __getattr__ = __getitem__

  def _push(self, env_params):
    if not env_params: return self
    keys = self.keys
    # we might want to allow an optimization to add parameters
    ukeys = [k for k in env_params if k not in keys]
    if ukeys: raise ValueError("unknows parameters", ukeys)
    return super(_Environment, self)._push(_Environment(env_params, self))

  _digest = None
  def digest(self):
    digest = self._digest
    if digest is None:
      digest = self._digest = tuple(self[k] for k in self.keys)
    return digest



#############################################################################
## Context

@implementer(IContext)
class Context(Stacked):
  """A general transformer context.

  Application code typically uses the class method `make_context`
  to create a context.
  """
  def __init__(self, resources, env):
    self.resources = resources
    self.env = env

  def transform(self, t, **env_params):
    return self._push(env_params)._transform(t)

  @classmethod
  def make_context(cls, resources, tspec, **env_params):
    """return a context for transformer *tspec* with parameters *env_params* accessing *resources*."""
    env_params["tspec"] = tspec
    return cls(resources, _Environment(env_params))


  def _lookup(self, t, tspec):
    return getSubscriptionAdapter(t, tspec)

  def _transform(self, t):
    env = self.env; tspec = env.tspec
    adapter = self._lookup(t, tspec)
    return adapter.transform(t, self)

  def push(self, **env_params): return self._push(env_params)

  def _push(self, env_params):
    return (
      self if not env_params
      else super(Context, self)._push(
        self.__class__(self.resources, self.env._push(env_params))))

  def __getattr__(self, k): return getattr(self.resources, k)



@implementer(IOptimizerContext)
class OptimizerContext(Context):
  """not thread safe."""
  def __init__(self, *args, **kw):
    super(OptimizerContext, self).__init__(*args, **kw)
    self.cache = WeakKeyDictionary()

  def optimize(self, t, **env_params):
    return self._push(env_params)._optimize(t)

  def transform(self, *args, **kw):
    return self.optimize(*args, **kw)[0]

  def _lookup(self, t, tspec):
    return querySubscriptionAdapter(t, tspec)

  def _optimize(self, t):
    cache = self.root.cache; env = self.env; digest = None
    if t in cache:
      digest = self.env.digest()
      if digest in cache[t]: return t, True
    env = self.env; tspec = env.tspec
    adapter = self._lookup(t, tspec)
    r = adapter.optimize(t, self) if adapter is not None else True
    r = rt, unchanged = (t, True) if r is True else r
    if digest is None:
      digest = env.digest()
    ce = cache.get(rt)
    if ce is None: ce = cache[rt] = set()
    ce.add(digest)
    return r

def flatten(it):
  for x in it:
    if hasattr(x, "__iter__"):
      for y in flatten(x): yield y
    yield x

@implementer(IOptimizerChain)
class OptimizerChain(object):
  """A optimizer chain implemented via subscription adapters.

  Subscription adapters have the advantage that it is very
  easy to add new adapters. On the other hand, it is
  very difficult to remove or customize existing adapters.
  Override `lookup` in a derived class to determine the chain
  in a different way.

  The implementation assumes that the lookup returns an iterator
  over optimizer components. This is `flatten`ed to optain
  the sub optimizers. All those must support `IOrdered`.
  They are ordered by their order to form the chain.

  The `optimize` of an optimizer in this chain may return
  a one element tuple containing the optimization result.
  This indicates that the optimization is so significant
  that the optimization needs to start over with the provided
  result. Note that such a start over is automatic if
  the optimization changed the root's class (as following steps
  likely would no longer understand the new type).
  """
  sub_tspec = None

  def __init__(self, t):
    """an optimizer chain for *t*."""
    self.t = t

  def lookup(self, t):
    tspec = self.sub_tspec
    required, provided = (
      ((t,), tspec) if tspec is not None
      else ((self, t), IOptimizer)
    )
    return getSiteManager().subscribers(required, provided)

  def start_over(self, nt, ot):
    """compare new *nt* against old *ot* to determine whether we must start over"""
    return nt.__class__ is not ot.__class__

  def optimize(self, t, context):
    unchanged = True
    if isinstance(t, Container):
      # optimize children
      children = []
      for c in t:
        oc, cu = context.optimize(c)
        if not cu: unchanged = False
        children.append(oc)
      if not unchanged: t = t.new_children(children)
    # optimize root
    for o in sorted(flatten(self.lookup(t)), key=lambda o: o.order):
      ot = o.optimize(t, context)
      if ot is True or ot is t: continue
      unchanged = False
      if isinstance(ot, tuple):
        ot = ot[0]; start_over = True
      else: start_over = self.start_over(ot, t)
      if start_over:
        ot, _ = context.optimize(ot)
        return ot, False
      t = ot
    return t, unchanged
