# -*- coding: utf-8 -*-
"""Setup module for elasticsearch mapping includes."""
import os

from setuptools import setup

readme = open('README.rst').read()

DATABASE = "postgresql"
INVENIO_VERSION = "3.1.0"

install_requires = [
    'elasticsearch<8.0.0,>=7.0.0'
]

g = {}
with open(os.path.join('invenio_oarepo_mapping_includes', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name="invenio_oarepo_mapping_includes",
    version=version,
    url="https://github.com/oarepo/invenio-oarepo-mapping-includes",
    license="MIT",
    author="Miroslav Simek",
    author_email="miroslav.simek@vscht.cz",
    description="An inclusion mechanism for elasticsearch mappings",
    zip_safe=False,
    packages=['invenio_oarepo_mapping_includes'],
    entry_points={
        'invenio_config.module': [
            'invenio_oarepo_mapping_includes = invenio_oarepo_mapping_includes.config',
        ],
        'invenio_base.apps': [
            'invenio_oarepo_mapping_includes = invenio_oarepo_mapping_includes.ext:InvenioOARepoMappingIncludesExt'
        ],
        'invenio_base.api_apps': [
            'invenio_oarepo_mapping_includes = invenio_oarepo_mapping_includes.ext:InvenioOARepoMappingIncludesExt'
        ]
    },
    include_package_data=True,
    setup_requires=install_requires,
    install_requires=install_requires,
    platforms='any',
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
