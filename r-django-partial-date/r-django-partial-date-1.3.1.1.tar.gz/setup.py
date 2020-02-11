import os
import sys

from setuptools import setup

from codecs import open

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

# This check and everything above must remain compatible with Python 2.7.
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of r-django-partial-date requires Python {}.{}, but you're trying to
install it on Python {}.{}.
This may be because you are using a version of pip that doesn't
understand the python_requires classifier. Make sure you
have pip >= 9.0 and setuptools >= 24.2, then try again:
    $ python -m pip install --upgrade pip setuptools
    $ python -m pip install django
This will install the latest version of r-django-partial-date which works on your
version of Python.
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)

here = os.path.abspath(os.path.dirname(__file__))


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    try:
        file = open(path, encoding='utf-8')
    except TypeError:
        file = open(path)
    return file.read()


with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='r-django-partial-date',
    version='1.3.1.1',
    description='Django custom model field for partial dates with the form YYYY, YYYY-MM, YYYY-MM-DD',
    long_description=read('README.rst'),
    author_email='ramses.mtz96@gmail.com',
    author='Ramses Martinez',
    url='https://github.com/RamsesMartinez/r-django-partial-date',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=['fields', 'django', 'dates', 'partial'],

    packages=['partial_date'],

    install_requires=[
        'django',
    ],
)
