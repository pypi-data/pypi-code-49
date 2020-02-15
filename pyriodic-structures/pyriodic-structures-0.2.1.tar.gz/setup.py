#!/usr/bin/env python

import os
from setuptools import setup

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

version_fname = os.path.join(THIS_DIR, 'pyriodic', 'version.py')
with open(version_fname) as version_file:
    exec(version_file.read())

readme_fname = os.path.join(THIS_DIR, 'README.md')
with open(readme_fname) as readme_file:
    long_description = readme_file.read()

setup(name='pyriodic-structures',
      author='Matthew Spellings',
      author_email='matthew.p.spellings@gmail.com',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
      ],
      description='Library to list and manipulate well-known 3D structures',
      entry_points={
          'pyriodic_sources': ['standard = pyriodic.unit_cells:load_standard'],
      },
      extras_require={},
      install_requires=[
          'numpy',
      ],
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=[
          'pyriodic',
          'pyriodic.unit_cells',
      ],
      project_urls={
          'Documentation': 'http://pyriodic.readthedocs.io/',
          'Source': 'https://github.com/klarh/pyriodic'
          },
      python_requires='>=3',
      url='http://github.com/klarh/pyriodic-aflow',
      version=__version__
      )
