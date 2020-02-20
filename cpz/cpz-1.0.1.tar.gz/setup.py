# -*- coding: utf-8 -*-

import sys
from setuptools import setup,find_packages
import cpz

if sys.version_info[:2] < (2, 7) or sys.version_info[0] >= 3:
    sys.exit('Python 2.7.x is required.')

with open('README.md') as fp:
    readme = fp.read()

setup(
      name="cpz",
      version=cpz.__version__,
      description=cpz.__description__,
      long_description=readme,
      long_description_content_type="text/markdown",

      maintainer=cpz.__author__,

      url='https://github.com/heronotears/cpz',
      author=cpz.__author__,
      author_email=cpz.__author_email__,

      packages=find_packages(),
      license=cpz.__license__,
      install_requires = ["numpy"],
      platforms = "any"
)
