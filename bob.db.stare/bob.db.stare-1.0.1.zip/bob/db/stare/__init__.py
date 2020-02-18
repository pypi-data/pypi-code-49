#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
STARE: STructured Analysis of the Retina

A. Hoover, V. Kouznetsova and M. Goldbaum, "Locating Blood Vessels in Retinal Images by Piece-wise Threhsold Probing of a Matched Filter Response", IEEE Transactions on Medical Imaging , vol. 19 no. 3, pp. 203-210, March 2000.

http://cecas.clemson.edu/~ahoover/stare/probing/index.html
"""

from .query import Database

def get_config():
  """Returns a string containing the configuration information.
  """

  import bob.extension
  return bob.extension.get_config(__name__)

# gets sphinx autodoc done right - don't remove it
__all__ = [_ for _ in dir() if not _.startswith('_')]
