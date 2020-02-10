# Copyright (C) 2019 by Dr. Dieter Maurer, Illtalstr. 25, D-66571 Bubach, Germany
# see "LICENSE.txt" for details
"""Auxiliaries."""

from decorator import decorator

@decorator
def instance_cached(f, self, *args, **kw):
  key = self._get_cache_key(f, args, kw)
  cache = self._get_cache()
  r = cache.get(key, cache)
  if r is cache:
    r = cache[key] = f(self, *args, **kw)
  return r
  

class InstanceCache(object):
  """Class supporting caching on the instance."""

  CACHE_TYPE = dict
  __cache = None

  def _get_cache(self):
    cache = self.__cache
    if cache is None:
      cache = self.__cache = self.CACHE_TYPE()
    return cache

  def _get_cache_key(self, f, args, kw):
    return f, args, sorted(kw.items())
