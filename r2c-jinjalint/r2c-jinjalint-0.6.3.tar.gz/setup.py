from setuptools import (
    find_packages,
    setup,
)
from pathlib import Path

import jinjalint


here = Path(__file__).parent

with (here / 'README.md').open('r') as f:
    long_description = '\n' + f.read()

with open('requirements.txt') as f:
    lines = f.read().split('\n')
    install_requires = [line.split()[0] for line in lines if line]

setup(
    name='r2c-' + jinjalint.__name__,
    version=jinjalint.__version__,
    author='R2C',
    author_email='support@returntocorp.com',
    url=jinjalint.__url__,
    description='A linter for Jinja-like templates',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    license=jinjalint.__license__,
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Security',
        'Topic :: Software Development :: Quality Assurance',
    ],
    entry_points={
        'console_scripts': ['jinjalint=jinjalint.cli:main'],
    },
)
