"""
setuptools for skidder
"""

from setuptools import setup, find_packages
from os import path


def get_long_desc():
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        return f.read()


setup(name='skidder',
      version='2020.2.14',
      description='A Python logging library',
      url='https://github.com/ktr/skidder',
      author='Kevin Ryan',
      author_email='ktr@26ocb.com',
      license='MIT',
      long_description=get_long_desc(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries',
          'Topic :: System :: Logging',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.8',
      ],
      keywords='logging',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
      project_urls={
          'Bug Reports': 'https://github.com/ktr/skidder/issues',
          'Source': 'https://github.com/ktr/skidder/',
      },
      zip_safe=False)
