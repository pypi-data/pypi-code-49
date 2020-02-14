import setuptools
from texercise import __version__

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
