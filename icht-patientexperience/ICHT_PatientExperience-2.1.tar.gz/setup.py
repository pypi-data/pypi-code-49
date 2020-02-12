import codecs
import os
import sys
try:
	from setuptools import setup, find_packages
except ImportError:
	from distutils.core import setup, find_packages

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = 'ICHT_PatientExperience',
      description = 'A pre-trained text classification model',
      long_description = read("README.txt"),
      version = '2.01',
      author = 'Jingxian You',
      author_email = 'jingxian.you@nhs.net',
      packages = find_packages(),
      url = "https://github.com/ykevingrox/ICHT_PatientExperience",
      
      package_data={
              'ICHT_PatientExperience.models': ['*'],
              },
      include_package_data=True,
      
      )