"""
To install AttrDict:
    python setup.py install
"""
import setuptools
from setuptools import setup

DESCRIPTION = "A collection of useful libraries"

try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    LONG_DESCRIPTION = DESCRIPTION

setup(
    name="elibs",
    version="1.0.9",
    author="Osni Pezzini Junior",
    author_email="osni.pezzini@gmail.com",
    packages=setuptools.find_packages(),
    url="https://github.com/ellitedev/elibs",
    license="MIT License",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    classifiers=(
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ),
    install_requires=(
        'requests',
        'wxpython',
    ),
    tests_require=(
        'nose>=1.0',
        'coverage',
    ),
    zip_safe=True,
)
