#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function
# from collections import defaultdict
# This line replaces 'from setuptools import setup'
from skbuild import setup
# from skbuild.cmaker import get_cmake_version
# from skbuild.exceptions import SKBuildError
# from packaging.version import LegacyVersion
# from distutils.version import LooseVersion

# from ctypes.util import find_library
setup_requires = []
install_requires = [
    'filelock',
    'nose',
    'numpy',
    'Cython',
]


MOD_NAMES = [ 
    'pi_calculator', 
    'rect', 
]


setup(name='scikit-build-template',
      description='cython cmake template modules',
      url='http://github.com/sirokujira/cython-cmake-template',
      version='0.0.1dev',
      author='Tooru Oonuma',
      author_email='t753github@gmail.com',
      maintainer='Tooru Oonuma',
      maintainer_email='t753github@gmail.com',
      license='BSD',
      # cmake_args=['-DSOME_FEATURE:BOOL=OFF']
      # packages=find_packages(),
      packages=[
          'temp',
      ],
      zip_safe=False,
      # The extra '/' was *only* added to check that scikit-build can handle it. 
      package_dir={'scikit-build-template': 'temp/'}, 
      setup_requires=setup_requires,
      install_requires=install_requires,
      classifiers=[
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      tests_require=['mock', 'nose'],
      test_suite='tests'
)
