#!/usr/bin/env python
import os, sys
from setuptools import setup, find_packages
# https://stackoverflow.com/questions/49837301/pip-10-no-module-named-pip-req
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

if sys.version_info < (3, 6):
    raise NotImplementedError(
        """Nextcode SDK does not support Python versions older than 3.6"""
    )

root_dir = 'nextcodecli'


def get_version_string():
    with open(os.path.join(root_dir, 'VERSION')) as version_file:
        return version_file.readlines()[0].strip()


version = get_version_string()
if 'SETUP_BRANCH' in os.environ:
    version += "-%s" % os.environ['SETUP_BRANCH']

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='nextcode-cli',
    python_requires=">=3.6",
    version=version,
    description="WuXi Nextcode commandline utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='WUXI NextCODE',
    author_email='support@wuxinextcode.com',
    url='https://www.wuxinextcode.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    package_data={'nextcodecli': ['VERSION', 'PUBLIC_KEY']},
    install_requires=[
        str(i.req)
        for i in parse_requirements('requirements.txt', session=False)
        if i.req
    ],
    entry_points={
        'console_scripts': [
            'nextcode = nextcodecli.__main__:cli',
        ]
    },
)
