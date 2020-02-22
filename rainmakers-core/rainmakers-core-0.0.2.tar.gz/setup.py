from setuptools import setup, find_packages

'''
python -m venv vert
source vert/bin/activate
python -c 'import setuptools'
python setup.py sdist

tar --list -f dist/{xyz.tar.gz}

manifest.in
include {filename}
recurvise-include /{path}/*
'''

setup(
    name='rainmakers-core',
    version='0.0.2',
    author='rainmakers',
    author_email='rainmakers9090@gmail.com',
    packages=find_packages()
)
