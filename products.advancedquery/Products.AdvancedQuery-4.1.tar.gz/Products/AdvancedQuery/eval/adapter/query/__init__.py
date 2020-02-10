# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Eppelborn, Germany
#       $Id: __init__.py,v 1.1 2019/04/22 05:55:57 dieter Exp $
"""Query optimization and conversion."""
from re import compile, escape

from .. import PositionArgCheck

def normalize_spec(spec):
  """transform ZCatalog query specification *spec* into a `dict`.

  This mimicks `IndexQuery`.
  """
  if hasattr(spec, "items"): spec = dict(spec) # verify, this works for `record`!
  if not isinstance(spec, dict): spec = dict(query=spec)
  if "query" in spec:
    keys = spec.pop("query")
    if not isinstance(keys, (list, tuple)): keys = keys,
  else: keys = () # might want `None` here
  spec["keys"] = keys
  if "not" in spec:
    not_ = spec["not"]
    if not isinstance(not_, (list, tuple)): spec["not"] = not_,
  return spec


class QueryCheck(PositionArgCheck):
  """check that a query used only supported features."""
  arg_pos = 0
  # to be defined by derived classes
  # SUPPORTED = set(....)
  def __call__(self, *objs, **kw):
    supported = kw.pop("supported", None)
    if supported is None: supported = self.SUPPORTED
    options = self.get_options(objs)
    for o in options:
      if o not in supported: return False
    return True

  def get_options(self, objs):
    q = self.get_arg(objs)
    spec = normalize_spec(q.make_spec())
    opts = []
    for op, arg in spec.items():
      if op == "keys": continue
      opts.append(arg if op in ("operator", "match") else op)
    return opts
    

def match_glob(glob):
  """a matcher for *glob*."""
  re = escape(glob) \
       .replace("\\?", ".") \
       .replace("\\*", ".*") \
       .replace("\\[", "[") \
       .replace("\\]", "]")
  return compile(re + "$").match

def match_regexp(regexp):
  """a matcher for *regexp*."""
  return compile(regexp).match

