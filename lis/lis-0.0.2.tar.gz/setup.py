import codecs
from setuptools import setup, find_packages


def read_file(filename, cb):
    with codecs.open(filename, 'r', 'utf8') as f:
        return cb(f)


def read_version():
    lines = read_file('lis/__init__.py', lambda o: o.readlines())
    version_line = next(l for l in lines if l.startswith('__version__'))
    return version_line.split('=')[-1].strip().strip('"').strip("'")


setup(
    name='lis',
    version=read_version(),

    packages=find_packages(),
    url='https://github.com/Marcnuth/lis',

    author='Marcnuth',
    author_email='hxianxian@gmail.com',

    license="Apache License 2.0",

    description="Life is short, use `lis`",
    long_description=read_file('README.md', lambda f: f.read()),
    long_description_content_type='text/markdown',
    install_requires=read_file('requirements.txt', lambda f: list(
        filter(bool, map(str.strip, f)))),

    classifiers=[
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3'
    ]
)
