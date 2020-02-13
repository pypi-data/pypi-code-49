#!/usr/bin/python
"""
Setup script for Intrepyd
"""

import platform
import sys
import os
from setuptools import setup, find_packages

with open('VERSION') as version_file:
    version = version_file.read().strip()

system_str = platform.system()
bits, _ = platform.architecture()

if bits != "64bit":
    print('Error: only 64bits architectures are supported. For other OSes please write to roberto.bruttomesso@gmail.com.')
    sys.exit(1)

arch_data_files = None
if system_str == 'Linux':
    arch_data_files = [('intrepyd', ['libs/linux64/_api.so'])]
elif system_str == 'Windows':
    arch_data_files = [('Lib/site-packages/intrepyd', ['libs/windows/_api.pyd', 'libs/windows/libz3.dll'])]
elif system_str == 'Darwin':
    arch_data_files = [('intrepyd', ['libs/osx/_api.so'])]

long_desc = """
========
Intrepyd
========
Intrepyd is a python module that provides a simulator and model checkers in form of
a rich API, to allow the rapid prototyping of **formal methods** algorithms
for the rigorous analysis of circuits, specifications, models.

============================
Formal Methods Little Corner
============================
A collection of experiences using Intrepyd can be found `here <https://formalmethods.github.io>`_.

====
FAQs
====
Please refer to the dedicated `Wiki page <https://github.com/formalmethods/intrepyd/wiki/FAQs>`_.
"""

setup(name='intrepyd',
      version=version,
      description='Intrepyd Model Checker',
      author='Roberto Bruttomesso',
      author_email='roberto.bruttomesso@gmail.com',
      maintainer='Roberto Bruttomesso',
      maintainer_email='roberto.bruttomesso@gmail.com',
      # url='http://github.com/formalmethods/intrepyd',
      # download_url='http://github.com/formalmethods/intrepyd/archive/' + version + '.tar.gz',
      install_requires=['pandas', 'antlr4-python3-runtime==4.8', 'enum'],
      packages=find_packages(),
      data_files=arch_data_files,
      # Does not work for sdist!
      package_data={'libs' : ['linux64/*.so', 'windows/*.dll', 'windows/*.pyd', 'osx/*.so']},
      license='BSD-3-Clause',
      platforms=['Windows', 'Linux', 'Darwin'],
      long_description=long_desc
)

