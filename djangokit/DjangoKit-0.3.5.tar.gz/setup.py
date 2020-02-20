#
# Copyright (c) 2019, Grigoriy Kramarenko
# All rights reserved.
# This file is distributed under the BSD 3-Clause License.
#
import setuptools

# Dynamically calculate the version based on djangokit.VERSION.
version = __import__('djangokit').get_version()

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DjangoKit",
    version=version,
    author="Grigoriy Kramarenko",
    author_email="root@rosix.ru",
    description=("DjangoKit is a set of extensions for Django."),
    long_description=long_description,
    url="https://gitlab.com/djbaldey/djangokit/",
    license="BSD License",
    zip_safe=False,
    packages=['djangokit'],
    include_package_data=True,
    install_requires=[
        'django>=2.2',
        'pillow>=6.2.1',
        'pycryptodome>=3.9.0',
        'pytz>=2019',
        'unidecode>=1.1.1',
    ],
    extras_require={
        'markdown': ['markdown>=3.1.1'],
        'pygments': ['pygments>=2.5.2'],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Natural Language :: Russian",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.5",
)
