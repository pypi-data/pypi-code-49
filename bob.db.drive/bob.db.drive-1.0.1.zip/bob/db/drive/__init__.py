#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
DRIVE: Digital Retinal Images for Vessel Extraction

J.J. Staal, M.D. Abramoff, M. Niemeijer, M.A. Viergever, B. van Ginneken, 
"Ridge based vessel segmentation in color images of the retina",
IEEE Transactions on Medical Imaging, 2004, vol. 23, pp. 501-509.

https://www.isi.uu.nl/Research/Databases/DRIVE/
"""

from .query import Database

def get_config():
  """Returns a string containing the configuration information.
  """

  import bob.extension
  return bob.extension.get_config(__name__)

# gets sphinx autodoc done right - don't remove it
__all__ = [_ for _ in dir() if not _.startswith('_')]
