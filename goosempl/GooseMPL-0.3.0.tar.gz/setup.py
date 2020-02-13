
from setuptools import setup
import re

filepath = 'GooseMPL/__init__.py'
__version__ = re.findall(r'__version__ = \'(.*)\'', open(filepath).read())[0]

setup(
    name='GooseMPL',
    version=__version__,
    author='Tom de Geus',
    author_email='tom@geus.me',
    url='https://github.com/tdegeus/GooseMPL',
    keywords='matplotlib, style',
    description='Style and extension functions for matplotlib',
    long_description='Style and extension functions for matplotlib',
    license='MIT',
    install_requires=['matplotlib>=2.0.0', 'numpy>=1.0.0'],
    packages=['GooseMPL'],
)
