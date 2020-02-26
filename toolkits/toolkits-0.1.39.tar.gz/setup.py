import sys
from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES

from setuptools import find_packages

PACKAGE = "toolkits"
NAME = "toolkits"
DESCRIPTION = "toolkits for quickly reference"
AUTHOR = "li_jia_yue"
AUTHOR_EMAIL = "59727816@qq.com"
URL = "https://github.com/starwithmoon/toolkits"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=open("README.rst").read(),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=find_packages(),
    package_data={
                # If any package contains *.txt files, include them:
                '': ['*.dat']},
    keywords='toolkits tools',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'schedule',
        'esmre',
        'unicodecsv', 'log4python', 'unipath', 'arrow', 'fire'
    ],
    zip_safe=False,
)
