#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
RIM-ONE Release 3

The dataset consists of 159 stereo retinal fundus images. The optic 
disc and optic cup of each image has been segmented by 2 experts 
in ophthalmology to create the ground truth. The average segmentation 
is also available to use as the reference segmentation or gold standard.

http://medimrg.webs.ull.es/research/retinal-imaging/rim-one/
"""

from .query import Database

def get_config():
  """Returns a string containing the configuration information.
  """

  import bob.extension
  return bob.extension.get_config(__name__)

# gets sphinx autodoc done right - don't remove it
__all__ = [_ for _ in dir() if not _.startswith('_')]
