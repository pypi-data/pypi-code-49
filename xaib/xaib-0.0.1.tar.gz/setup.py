from setuptools import setup, Command
import os
import sys

setup(name='xaib',
      version='0.0.1',
      description='Explainable AI In Business',
      url='https://github.com/firmai/automated-time-series',
      author='snowde',
      author_email='d.snow@firmai.org',
      license='MIT',
      packages=['xaib'],
      install_requires=[
          'pandas',
          'numpy',
          'scipy',
          'numba',
          'datetime',

      ],
      zip_safe=False)
