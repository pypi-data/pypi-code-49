import codecs
from setuptools import setup, find_packages

setup(
    name="pyamap",
    version="1.0.2",
    packages=['pyamap'],
    package_data={
    },
    install_requires=[
        'argparse',
    ],
    author="xlvecle",
    author_email="xlvecle@xlvecle.com",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='''''',
    url='http://xlvecle.github.io/pyamap'
)
