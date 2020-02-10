from setuptools import setup, find_packages
import versioneer

import os
import io

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='acondbs',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='A GraphQL server for product DB',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Simons Observatory',
    author_email='so_software@simonsobservatory.org',
    url='https://github.com/simonsobs/acondbs',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(exclude=['docs', 'tests'])
)
