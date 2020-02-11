from setuptools import find_packages
from setuptools import setup

import os

with open(os.path.join("Products", "PloneHotfix20200121", "README.txt")) as myfile:
    readme = myfile.read()
with open("CHANGES.rst") as myfile:
    changes = myfile.read()
long_description = readme + "\n" + changes

version = "1.1"

setup(
    name="Products.PloneHotfix20200121",
    version=version,
    description="Various Plone hotfixes, 2020-01-21",
    long_description=long_description,
    # Get more strings from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="plone security hotfix patch",
    author="Plone Security Team",
    author_email="security@plone.org",
    url="https://plone.org/security/hotfix/20200121",
    license="GPL",
    packages=find_packages(),
    namespace_packages=["Products"],
    include_package_data=True,
    zip_safe=False,
    install_requires=["setuptools"],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
)
