#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

version = '0.0.3'

setup(
    name='django-fe-manager',
    version=version,
    author='Antonio Vázquez Blanco',
    author_email='antoniovazquezblanco@gmail.com',
    url='https://gitlab.com/antoniovazquezblanco/django-fe-manager/',
    description='Manage front end dependencies in Django.',
    long_description=open('README.md').read() + '\n' + open('CHANGELOG.md').read(),
    long_description_content_type="text/markdown",
    license='MIT license',
    requires=['django (>= 2.0)'],
    packages=['fe_manager', 'fe_manager.templatetags', 'fe_manager.utils'],
    test_suite='tests',
    tests_require=['django (>= 2.0)'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
