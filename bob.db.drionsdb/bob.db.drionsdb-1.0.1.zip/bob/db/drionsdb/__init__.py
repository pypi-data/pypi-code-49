#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
DRIONS-DB: DRIONS-DB: Digital Retinal Images for Optic Nerve Segmentation Database

http://www.ia.uned.es/~ejcarmona/DRIONS-DB.html
"""

from .query import Database

def get_config():
  """Returns a string containing the configuration information.
  """

  import bob.extension
  return bob.extension.get_config(__name__)

# gets sphinx autodoc done right - don't remove it
__all__ = [_ for _ in dir() if not _.startswith('_')]
