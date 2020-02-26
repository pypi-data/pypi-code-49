# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('readme.org', 'r') as fh:
    long_description = fh.read()

setup(
    name='naps_utilities',
    packages=find_packages(exclude=["examples/*"]),
    version='0.1.1',
    description='Lib to handle ease of use of pointclouds ',
    author=u'Virgile Daugé',
    author_email='virgile.dauge@loria.fr',
    url='https://github.com/virgileTN/naps_utilities',
    keywords=['pointclouds', 'filtering'],
    install_requires=['numpy',
                      'pose_transform'],
    long_description=long_description,
    long_description_content_type='text/plain',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
        ],
)
