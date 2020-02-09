#! /usr/bin/env python
from setuptools import setup, find_packages

NAME = "orange-canvas-core-ml"
VERSION = "0.1.12.dev0"
DESCRIPTION = "Core component of Orange Canvas modifed"

with open("README.rst", "rt", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

URL = "http://zhaoyang.org.cn/"
AUTHOR = "SZZYIIT"
AUTHOR_EMAIL = 'gengy@zhaoyang.org'

LICENSE = "GPLv3"
DOWNLOAD_URL = 'https://github.com/szzyiit/orange-canvas-core'
PACKAGES = find_packages()

PACKAGE_DATA = {
    "orangecanvas": ["icons/*.svg", "icons/*png", "*.qm"],
    "orangecanvas.styles": ["*.qss", "orange/*.svg"],
}

INSTALL_REQUIRES = (
    "setuptools",
    "AnyQt",
    "docutils",
    "commonmark",
    "requests",
    "cachecontrol[filecache]",
    "pip>=18.0",
)


CLASSIFIERS = (
    "Development Status :: 1 - Planning",
    "Environment :: X11 Applications :: Qt",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
    "Topic :: Scientific/Engineering :: Visualization",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Intended Audience :: Education",
    "Intended Audience :: Developers",
)

EXTRAS_REQUIRE = {
    ':python_version=="3.4"': ["typing"],
    'DOCBUILD': ['sphinx', 'sphinx-rtd-theme'],
}

PROJECT_URLS = {
    "Bug Reports": "https://github.com/szzyiit/orange-canvas-core/issues",
    "Source": "https://github.com/szzyiit/orange-canvas-core/",
    "Documentation": "https://orange-canvas-core.readthedocs.io/en/latest/",
}

PYTHON_REQUIRES = ">=3.4"

if __name__ == "__main__":
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/x-rst",
        url=URL,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        license=LICENSE,
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        install_requires=INSTALL_REQUIRES,
        extras_require=EXTRAS_REQUIRE,
        project_urls=PROJECT_URLS,
        python_requires=PYTHON_REQUIRES,
    )
