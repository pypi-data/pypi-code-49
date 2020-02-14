"""
setuptools entrypoint

Copyright (C) 2020, fondlez "Anuber"-Kronos, fondlez at protonmail.com
"""
import os
from setuptools import setup, find_packages


with open('familyledger/VERSION', 'rt') as version_file:
    __version__ = version_file.read().strip()

with open('README.rst', 'rt') as fh:
    long_description = fh.read()

setup(
    name='FamilyLedger',
    version=__version__,
    author='fondlez "Anuber"-Kronos',
    author_email='fondlez@protonmail.com',
    url='https://github.com/anuber-Kronos/familyledger',
    description='Family Ledger is an application for collecting and viewing '
        'in-game item data held in World of Warcraft accounts.',
    long_description = long_description,
    download_url='https://github.com/anuber-Kronos/familyledger',
    packages=['familyledger', 'familyledger.utils', 'familyledger.slpp'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'ledger = familyledger.ledger:setup',
            'ledger_web = familyledger.ledger_web:setup',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing',
        'Topic :: Games/Entertainment :: Role-Playing',
    ],
    install_requires=[
        'remi==2019.11',
        'tqdm',
        'XlsxWriter',
    ],
)