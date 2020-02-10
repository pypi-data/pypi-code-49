#!/usr/bin/env python
from setuptools import setup


packages = [
    'dataops-salesforce-bulk',
]

requires = [
    'six',
    'requests>=2.2.1',
    'unicodecsv>=0.14.1',
    'simple-salesforce>=0.69',

]

with open('README.txt', 'r') as f:
    long_description = f.read()

setup(
    name='dataops-salesforce-bulk',
    version='0.0.5',
    description='Python interface to the Salesforce.com Bulk API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Scott Persinger',
    author_email='scottp@heroku.com',
    url='https://github.com/puppetlabs/salesforce-bulk',
    packages=packages,
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
)
