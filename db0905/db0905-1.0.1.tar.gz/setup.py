# -*- coding: utf-8 -*-

import sys
from setuptools import setup,find_packages
import db0905

if sys.version_info[:2] < (2, 7) or sys.version_info[0] >= 3:
    sys.exit('Python 2.7.x is required.')

with open('README.md') as fp:
    readme = fp.read()

setup(
      name="db0905",
      version=db0905.__version__,
      description=db0905.__description__,
      long_description=readme,
      long_description_content_type="text/markdown",

      maintainer=db0905.__author__,

      url='https://github.com/heronotears/db0905',
      author=db0905.__author__,
      author_email=db0905.__author_email__,

      packages=find_packages(),
      license=db0905.__license__,
      install_requires = ["numpy"],
      platforms = "any"
)
