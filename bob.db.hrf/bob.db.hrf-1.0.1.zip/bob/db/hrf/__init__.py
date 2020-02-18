#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
HRF: High-Resolution Fundus (HRF) Image Database

https://www5.cs.fau.de/research/data/fundus-images/
"""

from .query import Database

def get_config():
  """Returns a string containing the configuration information.
  """

  import bob.extension
  return bob.extension.get_config(__name__)

# gets sphinx autodoc done right - don't remove it
__all__ = [_ for _ in dir() if not _.startswith('_')]
