#!/usr/bin/env python

#
# Copyright 2012-2018 BloomReach, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
SageMakerRegistry, setup.py
"""

import os
import stat

from setuptools import find_packages, setup
from setuptools.command.install import install as _install

__author__ = "Felix Gao"
__copyright__ = "Copyright 2012-2020."
__license__ = "http://www.apache.org/licenses/LICENSE-2.0"
__version__ = "0.0.1"
__maintainer__ = "Felix Gao"
__status__ = "Development"

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
  long_description = f.read()

class install(_install):
  def run(self):
    _install.run(self)
    
setup(name='sgr',
      version=__version__,
      description='SageMaker Registry',
      author=__author__,
      license=__license__,
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/felixgao/sgr.git',
      py_modules=['sgr'],
      scripts=[], 
      install_requires=[],
      cmdclass={'install': install},
    )
