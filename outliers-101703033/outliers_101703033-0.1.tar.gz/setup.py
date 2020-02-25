# -*- coding: utf-8 -*-
"""
Created on Mon feb 10 20:04:23 2020

@author: aditi
"""

from distutils.core import setup
setup(
  name = 'outliers_101703033',         # How you named your package folder (MyLib)
  packages = ['outliers_101703033'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Finding outliers in a dataset in python',   # Give a short description about your library
  author = 'Aditi Tiwari',                   # Type in your name
  author_email = 'atiwari_be17@thapar.edu',      # Type in your E-Mail
  url = 'https://github.com/aditi721999',
  download_url = 'https://github.com/aditi721999/outliers_101703033.git',    

  keywords = ['python', 'outliers', '101703033'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas',
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