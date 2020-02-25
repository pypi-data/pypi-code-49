# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# oarepo-heartbeat-common is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Common heartbeat checks for OArepo instances"""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

INVENIO_VERSION = os.environ.get('INVENIO_VERSION', '3.2.1')

tests_require = [
    'check-manifest>=0.25',
    'coverage>=4.0',
    'isort>=4.3.3',
    'pydocstyle>=2.0.0',
    'pytest-cov>=2.5.1',
    'pytest-pep8>=1.0.6',
    'Sphinx>=1.5.1',
    'oarepo-heartbeat>=1.0.0',
    'invenio[base,auth,metadata,postgresql,elasticsearch6]~={0}'.format(INVENIO_VERSION),
]

extras_require = {
    'docs': [
        'Sphinx>=1.5.1',
    ],
    'tests': tests_require,
}

setup_requires = [
    'Babel>=1.3',
    'pytest-runner>=3.0.0,<5',
]

install_requires = [
    'Flask-BabelEx>=0.9.3',
]

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('oarepo_heartbeat_common', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='oarepo-heartbeat-common',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='Invenio oarepo heartbeat checks',
    license='MIT',
    author='Miroslav Bauer',
    author_email='bauer@cesnet.cz',
    url='https://github.com/oarepo/oarepo-heartbeat-common',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'flask.commands': [
            'heartbeat = oarepo_heartbeat_common.cli:heartbeat',
        ],
        'invenio_base.apps': [
            'oarepo_heartbeat_common = oarepo_heartbeat_common:OARepoHeartbeatCommon',
        ],
        'invenio_base.blueprints': [
            'oarepo-heartbeat = oarepo_heartbeat.views:blueprint',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 4 - Beta',
    ],
)
