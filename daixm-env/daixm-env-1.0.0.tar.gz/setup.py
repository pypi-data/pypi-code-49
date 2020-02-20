from setuptools import setup, find_packages
import sys, os

version = '1.0.0'

setup(name='daixm-env',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'envparse==0.2.0',
          'simplejson>=3.10.0',
          'six>=1.11.0',
          'pyapollo>=0.0.9',
          'M2Crypto>=0.28.0',
          'pytest<5.0.0',
      ],
      extras_require={
        'testing': ['pytest'],
      },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
