# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages
from distutils.core import Command


here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read()


class Test(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from django.conf import settings
        settings.configure(
            INSTALLED_APPS=('collectionfield.tests',),
            SECRET_KEY='AAA',
            DATABASES={
                'default': {
                    'NAME': ':memory:',
                    'ENGINE': 'django.db.backends.sqlite3'
                }
            },
            MIDDLEWARE_CLASSES = ()
        )
        from django.core.management import call_command
        import django
        django.setup()
        call_command('test', 'collectionfield')


setup(
    name='django-2-collectionfield',
    version='0.0.4a',
    description='Custom Django model field to store multiple values. Updated from original library to support Django 2.',
    long_description=long_description,
    url='https://github.com/rgutierrez-cotech/django-collectionfield',
    author='Pawel Scierski',
    author_email='escer@protonmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 2.2',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords='django models fields collections',
    packages=find_packages(),
    cmdclass={'test': Test},
)
