#!/usr/bin/env python3

from setuptools import setup, find_packages
import sys

version='1.0.0'

setup(
    zip_safe=True,
    name='RPi.infobot',
    version=version,
    long_description="Application for reporting basic diagnostic information about a Raspberry Pi",
    classifiers=[
      "Development Status :: 3 - Alpha",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: GNU General Public License (GPL)",
      "Programming Language :: Python :: 3",
    ],
    keywords='telegram rpi raspberry-pi',
    author='John Casey',
    author_email='jdcasey@commonjava.org',
    url='https://github.com/jdcasey/rpi.infobot',
    license='GPLv3+',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    install_requires=[
      "python-telegram-bot",
      "ruamel.yaml",
      "click",
      "requests",
      "datetime",
      "netifaces"
    ],
    include_package_data=True,
    test_suite="tests",
    entry_points={
      'console_scripts': [
        'rpi-infobot = rpi_infobot:bot'
      ],
    }
)

