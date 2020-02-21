from setuptools import setup, find_packages

from shawn_logger import __version__ as version

setup(
    name='shawn_logger',
    version=version,
    packages=find_packages(),
    author="shawn",
    url='https://github.com/tungph/shawn_logger',
)
