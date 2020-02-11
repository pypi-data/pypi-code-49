from os import path as os_path
from setuptools import setup

this_directory = os_path.abspath(os_path.dirname(__file__))


def read_file(filename):
    """
        Read File Contents
        Args:
            filename - Specified File to be read.
    """
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(
    name='nest_list_print',
    version='1.0.4',
    py_modules=['nest_list_print'],
    author='Wancheng Zhou',
    author_email='wancheng2012@gmail.com',
    url='http://www.headfirstlabs.com',
    description='A simple printer of nested lists',
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",  # Project README
    data_files=['./README.md'],                     # Data file specification
    license="MIT",
)
