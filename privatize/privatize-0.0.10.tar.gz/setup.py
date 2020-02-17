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

# Read in requirements.txt
# with open('requirements.txt', 'r') as f:
#     requirements = f.read().splitlines()

# Read in README.md
with open('README.md', 'r') as f:
    long_description = f.read()

# Setup
setup(
    name='privatize',
    version=version,
    author='C. Lockhart',
    author_email='chris@lockhartlab.org',
    description='a package for turning class variables into parameters',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://www.lockhartlab.org",
    packages=[
        'privatize',
    ],
    install_requires=[
        'typelike>=0.0.22',
    ],
    python_requires='>=3.7',
    include_package_data=True,
    zip_safe=True
)
