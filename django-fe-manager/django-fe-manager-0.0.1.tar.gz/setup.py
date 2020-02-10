#!/usr/bin/env python
from setuptools import setup

version = '0.0.1'

setup(
    name='django-fe-manager',
    version=version,
    author='Antonio Vázquez Blanco',
    author_email='antoniovazquezblanco@gmail.com',
    url='https://gitlab.com/antoniovazquezblanco/django-fe-manager/',
    description='Manage front end dependencies in Django.',
    long_description=open('README.md').read() + "\n",
    license='MIT license',
    requires=['django (>= 2.0)'],
    packages=['fe_manager', 'fe_manager.templatetags'],
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