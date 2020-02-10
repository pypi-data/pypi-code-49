# Copyright (C) 2019 by Dr. Dieter Maurer, Eichendorffstr. 23, D-66386 St. Ingbert, Germany
#       $Id: index.py,v 1.1 2019/04/22 05:55:57 dieter Exp $
"""Utilities for index adaptation."""
from . import ConditionalAdapterFactory, conditional_adapter, SafeInheritance


class IndexAdapter(object):
  def __init__(self, index): self.index = index


def recondition(ca, adapter, *checks):
  """replace the checks on conditional adapter *ca* by *checks*.

  Also declare new adaptation *adapter*.
  """
  assert isinstance(ca, ConditionalAdapterFactory)
  return conditional_adapter(*checks)(adapter(_Wrap(ca.factory)))


class _Wrap(object):
  """Auxiliary class to wrap a factory.

  Used to ensure that the `adapter` call above does not
  change the original object.
  """
  def __init__(self, factory): self.factory = factory

  def __call__(self, *args): return self.factory(*args)

  def __getattr__(self, k): return getattr(self.factory, k)
