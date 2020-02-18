#!/usr/bin/env python
from setuptools import setup


setup(name='collectd-top',
    version='0.0.1',
    description='CollectD plugin for top processes statistics',
    author='Yehor Panasenko',
    author_email='yehor.panasenko@gmail.com',
    url='https://github.com/gaurapanasenko/collectd-top',
    packages=[
        'collectd_top',
    ],
    package_dir={'collectd_top': 'collectd_top'},
    keywords='collectd-top',
    include_package_data=True,
    install_requires=[
    'collectd',
        ],
)
