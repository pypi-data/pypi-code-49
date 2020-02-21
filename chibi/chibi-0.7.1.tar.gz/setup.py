import os
try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup, find_packages

here = os.path.abspath( os.path.dirname( __file__ ) )
README = open(os.path.join( here, 'README.rst' ) ).read()

setup(
    name='chibi',
    version='0.7.1',
    description='',
    long_description=README,
    license='',
    author='dem4ply',
    author_email='',
    packages=find_packages(),
    install_requires=[
        'GitPython>=2.1.5', 'requests>=2.19.1', 'pika>=0.12.0', 'fleep>=1.0.1',
        'Pillow>=5.3.0', 'dateutils>=0.6.6', 'xmltodict>=0.12.0',
        'pyyaml>=5.1.2'
    ],
    dependency_links = [],
    url='https://github.com/dem4ply/chibi',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ] )
