# -*- coding: utf-8 -*-

import setuptools

long_description = 'load online k8s workload manifest to a helm chart'

packages = ['m2chart']

setuptools.setup(
    name='m2chart',
    version='1.0.0',
    author='yu.deng',
    author_email='dengyu326@gmail.com',
    description='load online k8s workload manifest to a helm chart',
    long_description=long_description,
    long_description_content_type='text/plain',
    packages=packages,
    package_data={'m2chart': ['*']},
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pyyaml',
        'kubernetes'
    ],
    entry_points={
        'console_scripts': [
            'm2chart = m2chart.main:main'
        ]
    },
)
