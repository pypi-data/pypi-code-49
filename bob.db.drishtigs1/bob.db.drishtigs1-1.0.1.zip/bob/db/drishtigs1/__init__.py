#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
Drishti-GS1 

Drishti-GS is a dataset meant for validation of segmenting OD, cup and detecting notching

http://cvit.iiit.ac.in/projects/mip/drishti-gs/mip-dataset2/Home.php 
"""

from .query import Database

def get_config():
  """Returns a string containing the configuration information.
  """

  import bob.extension
  return bob.extension.get_config(__name__)

# gets sphinx autodoc done right - don't remove it
__all__ = [_ for _ in dir() if not _.startswith('_')]
