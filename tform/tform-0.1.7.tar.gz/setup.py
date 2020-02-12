#!usr/bin/python
from setuptools import setup, find_packages
setup(
  name = 'tform',
  version = '0.1.7',
  packages = find_packages(),
  install_requires=[
    'certifi>=2018',
    'chardet>=3.0',
    'fire==0.1.3',
    'idna>=2.5',
    'PyYAML==3.13',
    'requests==2.21.0',
    'six==1.12.0',
    'urllib3==1.24.1'
  ],
  entry_points = {
    'console_scripts': [
      'tform = tform.__main__:main'
    ]
  }
)
