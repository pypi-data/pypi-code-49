# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 17:43:51 2020

@author: Parteek Sharma
"""

from distutils.core import setup
setup(
  name = 'outliers_101703384',         # How you named your package folder (MyLib)
  packages = ['outliers_101703384'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT', 
  entry_points ={ 
    'console_scripts': [ 
        'remove_outliers = outliers_101703384.remove_outliers:main'
    ] 
  }, 
  description = 'outliers removal using quantiles',   # Give a short description about your library
  author = 'Parteek Sharma',                   # Type in your name
  author_email = 'psharma_be17@thapar.edu',      # Type in your E-Mail
  url = 'https://github.com/Parteek-Sharma/outliers_remover_101703384',   # Provide either the link to your github or to your website
  keywords = ['outliers removal', 'remove outliers'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas',
          'scipy',
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
    'Programming Language :: Python :: 3.6',
    
  ],
)

