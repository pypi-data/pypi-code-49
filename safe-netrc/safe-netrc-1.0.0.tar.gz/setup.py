import sys

from setuptools import setup
import versioneer

setup_requires = ['setuptools >= 30.3.0']
if {'pytest', 'test', 'ptr'}.intersection(sys.argv):
    setup_requires.append('pytest-runner')

setup(cmdclass=versioneer.get_cmdclass(),
      version=versioneer.get_version(),
      setup_requires=setup_requires)
