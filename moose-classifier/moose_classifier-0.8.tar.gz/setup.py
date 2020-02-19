import setuptools
import sys

if sys.version_info < (3, 0):
    raise EnvironmentError('Please install using pip3 or python3')

setuptools.setup(author='Chris Rosenthal',
                 author_email='crosenth@gmail.com',
                 classifiers=[
                     'License :: OSI Approved :: '
                     'GNU General Public License v3 (GPLv3)',
                     'Development Status :: 4 - Beta',
                     'Environment :: Console',
                     'Operating System :: OS Independent',
                     'Intended Audience :: End Users/Desktop',
                     'License :: OSI Approved :: '
                     'GNU General Public License v3 (GPLv3)',
                     'Programming Language :: Python :: 3.9',
                     'Programming Language :: Python :: 3.8',
                     'Programming Language :: Python :: 3.7',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.5',
                     ],
                 description='Alignment based taxonomic classifier',
                 entry_points={
                     'console_scripts': {'classify=classifier.classify:main'}},
                 install_requires=['pandas>=0.24.0'],
                 keywords=[
                     'ncbi', 'blast', 'classifier', 'genetics', 'genomics',
                     'dna', 'rna', 'bioinformatics'],
                 license='GPLv3',
                 name='moose_classifier',
                 packages=setuptools.find_packages(exclude=['tests']),
                 version=0.8,
                 url='https://github.com/crosenth/moose'
                 )
