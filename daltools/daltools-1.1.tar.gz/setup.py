from setuptools import setup
from daltools import __version__

setup(
    name="daltools",
    author="Olav Vahtras",
    author_email="olav.vahtras@gmail.com",
    version=__version__,
    url="https://github.com/vahtras/daltools",
    packages=["daltools"],
    install_requires=["blocked-matrix-utils", "fortran-binary"]
    )
