from setuptools import find_packages
from setuptools import setup
import os

def readme():
    with open('README.rst') as f:
        return f.read()

def version():
    return '2.3.3.1'

setup(name='lcmap-merlin',
      version=version(),
      description='Python client library for LCMAP rasters',
      long_description=readme(),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: Public Domain',
        'Programming Language :: Python :: 3.6',
      ],
      keywords='usgs lcmap eros',
      url='http://github.com/usgs-eros/lcmap-merlin',
      author='USGS EROS LCMAP',
      author_email='',
      license='Unlicense',
      packages=find_packages(),
      install_requires=[
          'cytoolz',
          'numpy',
          'requests',
          'python-dateutil',
      ],
      # List additional groups of dependencies here (e.g. development
      # dependencies). You can install these using the following syntax,
      # for example:
      # $ pip install -e .[test]
      extras_require={
          'test': ['pytest',
                   'pytest-cov',
                   'hypothesis',
                   'vcrpy',
                  ],
          'doc': ['sphinx',
                  'sphinx-autobuild',
                  'sphinx_rtd_theme'],
          'dev': ['twine'],
      },
      # entry_points={
          #'console_scripts': [''],
      # },
      include_package_data=True,
      zip_safe=False)
