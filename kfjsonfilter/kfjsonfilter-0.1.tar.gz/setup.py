from setuptools import setup
from os import path

current_dir = path.abspath(path.dirname(__file__))

with open(path.join(current_dir, 'README.md')) as f:
    long_description = f.read()

setup(
      name='kfjsonfilter',
      version='0.1',
      description='Json Data Filter for django and django rest framework',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://gitlab.com/kas-factory/packages/drf-json-filter',
      author='Aurora @ KF',
      author_email='aurora@kasfactory.net',
      license='COPYRIGHT',
      packages=['kfjsonfilter'],
      install_requires=[
          'django>=3.0.2',
          'djangorestframework>=3.10.3'
      ],
      zip_safe=False)
