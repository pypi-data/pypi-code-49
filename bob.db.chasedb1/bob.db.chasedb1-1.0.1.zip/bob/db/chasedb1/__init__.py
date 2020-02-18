#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
CHASE_DB1: Retinal image database

Fraz, M.M, Remagnino, P., Hoppe, A., Uyyanonvara, B., Rudnicka, A.R., Owen, C.G. and Barman S.A. (2012) An ensemble classification-based approach applied to retinal blood vessel segmentation. IEEE Transactions on Biomedical Engineering, 59(9), pp. 2538-2548.

https://blogs.kingston.ac.uk/retinal/chasedb1/
"""

from .query import Database

def get_config():
  """Returns a string containing the configuration information.
  """

  import bob.extension
  return bob.extension.get_config(__name__)

# gets sphinx autodoc done right - don't remove it
__all__ = [_ for _ in dir() if not _.startswith('_')]
