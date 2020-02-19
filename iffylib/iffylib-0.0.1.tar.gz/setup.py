import os
from setuptools import setup, find_packages


# Read in requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='iffylib',
    version='0.0.1',
    description='CLI for giphy searches',
    author='jose idar',
    author_email='jose.idar@gmail.com',
    install_requires=requirements,
    packages=find_packages(exclude=('tests*', 'docs')),
    include_package_data=True,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ),
    entry_points={
        'console_scripts': ['iffy = iffylib.cli:cli', ]},
    tests_require=['tox'],
)
