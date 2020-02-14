import setuptools
from pathlib import Path

with (Path(__file__).parent / 'texercise' / 'version').open() as f:
    __version__ = f.readline()

setuptools.setup(
    name='texercise',
    version=__version__,
    author='Rasmus Laurvig Haugaard',
    author_email='rasmus.l.haugaard@gmail.com',
    description='command line interface for exercises',
    url='https://github.com/RasmusHaugaard/texercise-cli',
    scripts=[
        'bin/texercise',
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        'request',
        'click',
        'tabulate',
    ],
    python_requires='>=3.6',
)
