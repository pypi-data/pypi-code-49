#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
REFUGE Retinal Fundus Glaucoma Challenge

https://refuge.grand-challenge.org/Home/
http://ai.baidu.com/broad/download?dataset=gon 
"""

from .query import Database

def get_config():
  """Returns a string containing the configuration information.
  """

  import bob.extension
  return bob.extension.get_config(__name__)

# gets sphinx autodoc done right - don't remove it
__all__ = [_ for _ in dir() if not _.startswith('_')]
