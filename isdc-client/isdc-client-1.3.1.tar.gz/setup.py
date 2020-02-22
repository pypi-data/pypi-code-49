from setuptools import setup
import ast
import sys

setup_requires = ['setuptools >= 30.3.0']
if {'pytest', 'test', 'ptr'}.intersection(sys.argv):
    setup_requires.append('pytest-runner')


setup(name='isdc-client',
      long_description=open('README.md').read(),
      version="1.3.1",
      setup_requires=setup_requires)
