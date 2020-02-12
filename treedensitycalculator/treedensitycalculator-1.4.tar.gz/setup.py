# -*- coding: UTF-8 -*-.
from setuptools import setup, find_packages

setup(
    name='treedensitycalculator',
    version='1.4',
    description='The Tree Density Calculator is a QGIS plugin and CLI package designed to calculate tree densities.',
    author='Ann Crabbé (KU Leuven); Tinne Cahy (Geo Solutions)',
    author_email='ann.crabbe@kuleuven.be',
    packages=find_packages(where="localmaxfilter"),
    package_dir={
        '': 'localmaxfilter',
    },
    license='This program is free software; you can redistribute it and/or modify it under the terms of the GNU '
            'General Public License as published by the Free Software Foundation; either version 3 of the License, or '
            'any later version.',
    url='https://bitbucket.org/kul-reseco/localmaxfilter',
    entry_points={
        'console_scripts':
            [
                'treedensity = localmaxfilter.cli.local_max_filter_cli:main'
            ],
    }
)
