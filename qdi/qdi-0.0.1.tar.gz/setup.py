# encoding: utf-8
import sys

from setuptools import setup


def read_description():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='qdi',
    version='0.0.1',
    url='https://github.com/qooba/python-qdi',
    license='MIT',

    author='Kuba Sołtys',
    author_email='dev@qooba.net',

    description='Python dependency injection library',
    long_description=read_description(),
    long_description_content_type="text/markdown",

    packages=['qdi'],
    package_data={'qdi': ['py.typed']},
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules']
)
