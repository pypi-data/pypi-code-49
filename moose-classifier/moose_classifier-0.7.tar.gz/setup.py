import setuptools
import sys

if sys.version_info < (3, 0):
    raise EnvironmentError('Please install using pip3 or python3')

setuptools.setup(author='Chris Rosenthal',
                 author_email='crosenth@gmail.com',
                 classifiers=[
                     'License :: OSI Approved :: '
                     'GNU General Public License v3 (GPLv3)',
                     'Development Status :: 3 - Alpha',
                     'Environment :: Console',
                     'Operating System :: OS Independent',
                     'Intended Audience :: End Users/Desktop',
                     'License :: OSI Approved :: '
                     'GNU General Public License v3 (GPLv3)',
                     'Programming Language :: Python :: 3 :: Only'],
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
                 package_data={'classifier': ['data/*']},
                 version=0.7,
                 url='https://github.com/crosenth/moose'
                 )
