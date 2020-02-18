import ast
import os
import re

from pkg_resources import parse_requirements
from setuptools import setup, find_packages

CURDIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(CURDIR, 'README.md')) as f:
    README = f.read()

with open(os.path.join(CURDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read()


def get_version():
    init_path = os.path.join(CURDIR, 'line_info', '__init__.py')
    with open(init_path) as init:
        match = re.search(r'__version__\s+=\s+(?P<version>.*)', init.read())
        version = match.group('version') if match is not None else "'unknown'"
    return str(ast.literal_eval(version))


setup(
    name='line_info',
    version=get_version(),
    author='MrMrRobat',
    author_email='appkiller16@gmail.com',
    description='CLI tool to fetch helpful info about line of code, such as issue number, related PRs, etc.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/MrMrRobat/line_info',
    packages=find_packages(CURDIR),
    include_package_data=True,
    entry_points={'console_scripts': ['line_info=line_info.__main__:main']},
    zip_safe=False,
    install_requires=[str(req) for req in parse_requirements(REQUIREMENTS)],
    python_requires='>=3.6',
    license='License :: OSI Approved :: MIT License',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
