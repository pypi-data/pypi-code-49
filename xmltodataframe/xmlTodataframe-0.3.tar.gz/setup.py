# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 14:54:12 2020

@author: raghav.sharma11
"""

from distutils.core import setup
setup(
  name = 'xmlTodataframe',
  packages = ['xml2dataframe'],
  version = '0.3',
  license='GPL-3.0-only',
  description = 'xmlTodataframe convert given xml file to csv file!',
  author = 'Raghav Sharma',
  author_email = 'raghavsharma582@gmail.com',
  url = 'https://github.com/raghav582/xmlTodataframe',
  download_url = 'https://github.com/raghav582/xmlTodataframe/archive/0.3.tar.gz',
  keywords = ['xml', 'xmltocsv', 'csv'],
  install_requires=[
          'pandas'
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
