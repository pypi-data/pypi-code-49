import re
import pathlib

from setuptools import setup
from sys import version_info


if version_info < (3, 6, 0):
    raise RuntimeError("abconfig requires Python 3.6+")

here = pathlib.Path(__file__).parent
txt = (here / 'abconfig' / '__init__.py').read_text('utf-8')

try:
    version = re.findall(r"^__version__ = '([^']+)'\r?$", txt, re.M)[0]
except IndexError:
    raise RuntimeError('Unable to determine version.')

with open('README.md', 'r') as f:
    long_description = f.read()

args = dict(
    name='abconfig',
    version=version,
    author='Alexander Shevchenko',
    author_email='kudato@me.com',
    description='Simple and powerful configuration manager for Python projects',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kudato/abconfig.git",
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    packages=['abconfig'],
    extras_require={
        'yaml': ['pyyaml>=5.1'],
        'toml': ['toml>=0.10.0'],
        'vault': ['hvac>=0.9.6, <0.11.2'],
        'aws': ['boto3>=1.10.45']
    },
    python_requires='>=3.6.0'
)

setup(**args)