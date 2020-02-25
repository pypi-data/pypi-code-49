# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:04:23 2020

@author: aditi
"""

from distutils.core import setup
setup(
  name = 'missing_101703033',         # How you named your package folder (MyLib)
  packages = ['missing_101703033'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Implementation of handling missing values in a dataset in python',   # Give a short description about your library
  author = 'Aditi Tiwari',                   # Type in your name
  author_email = 'atiwari_be17@thapar.edu',      # Type in your E-Mail
  url = 'https://github.com/aditi721999',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/aditi721999/missing_101703033.git',    # I explain this later on
  keywords = ['python', 'missing_values', 'aditi'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'Pandas',
          'Numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)