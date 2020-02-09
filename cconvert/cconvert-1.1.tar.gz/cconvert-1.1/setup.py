"""Setup for the chocobo package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Aravind Balaji",
    author_email="snaravindbalaji@gmail.com",
    name='cconvert',
    license="MIT",
    scripts=['bin/cconvert'],
    description='Convert your base currency to resultant currency from terminal!!!',
    version='1.1',
    long_description=README,
    url='https://github.com/tedevelynmosby/Terminal-currency-converter/',
    packages=setuptools.find_packages(),
    python_requires=">=3.3",
    install_requires=['requests'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)