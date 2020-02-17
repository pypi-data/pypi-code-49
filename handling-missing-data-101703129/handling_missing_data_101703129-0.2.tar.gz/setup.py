# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 19:17:17 2020

@author: Ayush Garg
"""

from distutils.core import setup
setup(
  name = 'handling_missing_data_101703129',
  packages = ['handling_missing_data_101703129'],
  version = '0.2',
  license='MIT',
  description = 'This package will generate a new dataset from your old dataset by removing the records having missing values.',
  author = 'Ayush Garg',
  author_email = '987ayush@gmail.com',
  url = 'https://github.com/ayush7garg/handling_missing_data_101703129',
  download_url = 'https://github.com/ayush7garg/handling_missing_data_101703129/archive/v_02.tar.gz',
  install_requires=[
          'pandas',
          'tkinter',
          'sklearn',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
)