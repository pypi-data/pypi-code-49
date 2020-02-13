import setuptools
from justblast.__version__ import version
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(this_directory, 'requirements.txt'), encoding='utf-8'
          ) as r:
    requirements = r.read().strip().split()
setuptools.setup(
    name='justblast',
    version=version,
    packages=setuptools.find_packages() + ['justblast'],
    url='https://github.com/jshleap/justblast',
    license='GNU v3',
    author='jshleap',
    scripts=['bin/justblast'],
    author_email='jshleap@gmail.com',
    description='Simple program to more efficiently run blast in multicore '
                'systems, as well as rough taxonomomic annoation using BASTA '
                'LCA',
    python_requires='>=3.6',
    install_requires=[requirements],
    dependency_links=['https://github.com/timkahlke/BASTA#BASTA'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
