#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
IOSTAR – Retinal Vessel Segmentation (A/V) Dataset (Updated by 6/1/2018)

Jiong Zhang, Behdad Dashtbozorg, Erik Bekkers, Josien P.W. Pluim, Remco Duits, and Bart M. ter Haar Romeny, “Robust retinal vessel segmentation via locally adaptive derivative frames in orientation scores,” IEEE Transactions on Medical Imaging, vol. 35, no. 12, pp. 2631–2644, 2016.

http://www.retinacheck.org/datasets
"""

from .query import Database

def get_config():
  """Returns a string containing the configuration information.
  """

  import bob.extension
  return bob.extension.get_config(__name__)

# gets sphinx autodoc done right - don't remove it
__all__ = [_ for _ in dir() if not _.startswith('_')]
