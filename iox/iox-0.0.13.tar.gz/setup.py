"""
setup.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

from setuptools import setup


# Read version
with open('version.yml', 'r') as f:
    data = f.read().splitlines()
version_dict = dict([element.split(': ') for element in data])

# Convert the version_data to a string
version = '.'.join([str(version_dict[key]) for key in ['major', 'minor', 'patch']])

# Read in README.md as the long description
with open('README.md', 'r') as f:
    long_description = f.read()

# Setup
setup(
    name='iox',
    version=version,
    author='C. Lockhart',
    author_email='chris@lockhartlab.org',
    description='a package for IO connections',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://www.lockhartlab.org",
    packages=[
        'iox'
    ],
    install_requires=[
        'glovebox',
        'google-api-python-client',
        'google-cloud-bigquery==1.22.0',
        'google_auth',
        'google_auth_oauthlib',
        'numpy',
        'pandas',
        'privatize>=0.0.9',
    ],
    include_package_data=True,
    zip_safe=True
)
