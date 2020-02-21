from setuptools import setup, find_packages

with open('README.md','r') as fh:
    long_description=fh.read()
name='kryptic'
__version__='1.0'
description='A tool for generating passwords'
requirements=open('requirements.txt').readlines()
requirements=[r.strip() for r in requirements]
packages = [name] + [
    name + '.' + package for package in find_packages(where=name)
]
setup(
    name=name,
    version=__version__,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=('>=3.6.0'),
    license='MIT',
    install_requires=requirements,
    packages=find_packages()#packages
)