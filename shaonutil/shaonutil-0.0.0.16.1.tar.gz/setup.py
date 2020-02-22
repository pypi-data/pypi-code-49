#from distutils.core import setup
from setuptools import setup
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
  name = 'shaonutil',
  packages = ['shaonutil'],
  version = '0.0.0.16.1',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Shaon Majumder',
  author_email = 'smazoomder@gmail.com',
  url = 'https://github.com/ShaonMajumder/shaonutil',
  download_url = 'https://github.com/ShaonMajumder/shaonutil/archive/0.0.0.16.1.tar.gz',
  keywords = ['shaon', 'utility', 'statistics'], 
  classifiers = [],
  setup_requires=['wheel']
)