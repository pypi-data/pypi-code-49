# coding: utf-8

from setuptools import setup, find_packages

setup(
    name = "cisco-python-api",
    version = "0.0.2",
    packages = find_packages('src'),
    package_dir = {"": "src"},
    install_requires = [
        'requests>=2.21.0,<3',
    ],
    author='Nelson Fonseca',
    author_email='nelson@mambowifi.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)

