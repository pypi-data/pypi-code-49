from setuptools import find_packages
from setuptools import setup
import os

def readme():
    with open('README.rst') as f:
        return f.read()

def version():
    return '0.1.1'

setup(name='lcmap-oxen',
      version=version(),
      description='Create LCMAP aux tiles',
      long_description=readme(),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: Public Domain',
        'Programming Language :: Python :: 3.8',
      ],
      keywords='usgs lcmap eros',
      url='http://eroslab.cr.usgs.gov/lcmap/oxen',
      author='USGS EROS LCMAP',
      author_email='',
      license='Unlicense',
      packages=find_packages(),
      install_requires=[
      ],
      # List additional groups of dependencies here (e.g. development
      # dependencies). You can install these using the following syntax,
      # for example:
      # $ pip install -e .[test]
      extras_require={
          'test': ['pytest',
                   'pytest-cov',
                  ],
          'doc': ['sphinx',
                  'sphinx-autobuild',
                  'sphinx_rtd_theme'],
          'dev': ['twine'],
      },
      entry_points={
          'console_scripts': ['clip_nlcd=oxen.clip_nlcd:main'],
      },
      include_package_data=True,
      zip_safe=False)
