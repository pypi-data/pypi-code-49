#!/usr/bin/python3
# -*- coding: utf-8 -*-

# setup.py file is part of sun.

# Copyright 2015-2020 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# sun is a tray notification applet for informing about
# package updates in Slackware.

# https://gitlab.com/dslackw/sun

# sun is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup

from sun.__metadata__ import (
    __all__, __version__,
    __email__, __author__,
    conf_path, icon_path,
    desktop_path
)

INSTALLATION_REQUIREMENTS = [
    'urllib3>=1.25.7',
    'dbus-python>=1.2.4',
    'notify2>=0.3.1',
    'PyGObject>=3.18.2'
    ]
DOCS_REQUIREMENTS = []
TESTS_REQUIREMENTS = [
    'pytest>=5.3.2'
]
OPTIONAL_REQUIREMENTS = []


setup(
    name=__all__,
    packages=['sun', 'sun/gtk', 'sun/cli'],
    scripts=['bin/sun_daemon', 'bin/sun', 'bin/sun_gtk'],
    version=__version__,
    description='Tray notification applet for informing about package updates '
                'in Slackware',
    long_description=open('README.rst').read(),
    keywords=['tray', 'notify', 'slackware', 'desktop'],
    author=__author__,
    author_email=__email__,
    package_data={'': ['LICENSE.txt', 'README.rst', 'CHANGES.md']},
    data_files=[(conf_path, ['conf/sun.conf']),
                (icon_path, ['icon/sun.png']),
                (desktop_path, ['sun.desktop'])],
    url='https://gitlab.com/dslackw/sun',
    install_requires=INSTALLATION_REQUIREMENTS,
    extras_require={
        'optional': OPTIONAL_REQUIREMENTS,
        'docs': DOCS_REQUIREMENTS,
        'tests': TESTS_REQUIREMENTS,
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7',
        'Topic :: Desktop Environment',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Software Distribution',
        ],
    python_requires='>=3.7'
)
