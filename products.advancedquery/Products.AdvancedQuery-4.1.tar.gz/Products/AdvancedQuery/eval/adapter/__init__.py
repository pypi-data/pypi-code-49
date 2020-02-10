# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: __init__.py,v 1.1 2019/04/22 05:55:56 dieter Exp $
"""Adapter

This package provides support for conditional
adaptation and applies it for the optimization/conversion/evaluation
of queries and (evaluation) trees.


Conditional adaptation
======================

Standard adaptation assumes that an adaptation registered for a base
class is also applicable for a derived class, unless there
is a more specific adapter registered for the derived class.

This is not sufficiently safe in our context.
For example, a general adapter for `UnIndex` (applicable for
a wide range of derived indexes) is inappropriate for
the derived `BooleanIndex`. 
This package registers a specialized adapter for `BooleanIndex`,
but this is not sufficiently safe: integrated in an
application, it may try to adapt an unknown index derived from
`UnIndex` and the integrator may be unaware that this index
needs special adapters. The answer to this problem is
conditional adaptation.

Conditional adaptation uses that the adapter `None` is
interpreted as "adapter inadequate" and the registry continues
looking for more general adapters.
A conditional adaptation thus consists of an adapter factory
and a check. It first applies the check and return `None` if
it fails; otherwise, it applies the adapter factory.

Unfortunaletly, zope's adapter related functions interpret
a `None` adapter as "not adaptable" and not as "adapter inadequate"
and they do not lookup for a more genreal adapter.
We therefore implement conditional adaptation by zope's
"subscription adapter"s and implement the "adapter inadequate"
logic ourselves. As a consequence, our adapters cannot have
a name.
"""
from zope.interface import providedBy
from zope.interface.interfaces import ComponentLookupError
from zope.component import getSiteManager, adapter

from ..lib import InstanceCache, instance_cached


def queryMultiSubscriptionAdapter(objs, iface, default=None, context=None):
  sm = getSiteManager(context)
  subscriptions = sm.adapters.subscriptions(
    tuple(map(providedBy, objs)), iface
    )
  # `subscriptions` are most specific last
  i = len(subscriptions)
  while i > 0:
    i -= 1
    s = subscriptions[i]
    a = s(*objs)
    if a is not None: return a
  return default

def querySubscriptionAdapter(obj, iface, default=None, context=None):
  return queryMultiSubscriptionAdapter((obj,), iface, default, context)

def getMultiSubscriptionAdapter(objs, iface, context=None):
  a = queryMultiSubscriptionAdapter(objs, iface, context=context)
  if a is None: raise ComponentLookupError(objs, iface)
  return a


def getSubscriptionAdapter(obj, iface, context=None):
  a = queryMultiSubscriptionAdapter((obj,), iface, context=context)
  if a is None: raise ComponentLookupError(obj, iface)
  return a


class ConditionalAdapterFactory(object):
  def __init__(self, factory, checks):
    self.factory = factory
    self.checks = checks

  def check(self, objs):
    for c in self.checks:
      if not c(*objs): return False
    return True

  def __call__(self, *objs):
    if self.check(objs): return self.factory(*objs)

def conditional_adapter(*checks):
  """factory decorator conditioning by checks."""
  def wrap(factory):
    f = ConditionalAdapterFactory(factory, checks)
    adapts = getattr(factory, "__component_adapts__", None)
    if adapts is not None:
      ifaces = getattr(adapts, "interfaces", adapts)
      f = adapter(*ifaces)(f)
    return f
  return wrap


class ArgCheck(object):
  def get_arg(self, args): raise NotImplementedError

class PositionArgCheck(ArgCheck):
  arg_pos = 0 # to be overridden by derived classes or instances

  def get_arg(self, args): return args[self.arg_pos]


class ClassBasedCheck(InstanceCache, ArgCheck):
  """assumes that a single method is cached."""

  def _get_cache_key(self, f, args, kw):
    return self.get_arg(args).__class__


class SafeInheritance(ClassBasedCheck, PositionArgCheck):
  """check safety based on the class of the first adapted object.

  The adaptation is considered safe, if this call is a subclass
  of a reference class and has not overridden specified methods.

  It is assumed that the checked methods do not change at
  runtime (used for caching).
  """
  arg_pos = 0

  def __init__(self, ref_class, *checked_methods):
    self._ref_class = ref_class; self._methods = checked_methods
    self._cache = {}

  @instance_cached
  def __call__(self, *objs):
    cls = self.get_arg(objs).__class__
    rcls = self._ref_class
    ok = issubclass(cls, rcls)
    if ok:
      def to_func(c, mn):
        f = getattr(c, mn)
        return getattr(f, "__func__", f)
      for m in self._methods:
        if to_func(cls, m) is not to_func(rcls, m): return False
      return True


class Adaptable(ClassBasedCheck, PositionArgCheck):
  """check that the first adapted object is (subscription) adaptable to a set of interfaces.

  Note: we handle this as a class level property while in fact it is
  an instance based property.
  """
  arg_pos = 0

  def __init__(self, *ifaces): self.ifaces = ifaces

  @instance_cached
  def __call__(self, *objs):
    for iface in self.ifaces:
      if querySubscriptionAdapter(self.get_arg(objs), iface) is None: return False
    return True
