import setuptools
from two import __version__

try:
    import numpy
except ImportError:
    import subprocess
    subprocess.call("pip install numpy", shell=True)

from numpy.distutils.core import setup, Extension
ext = Extension(
    name='sirfck',
    sources=['two/sirfck.c'],
    libraries=['blas']
)

setup(
    author="Olav Vahtras",
    author_email="olav.vahtras@gmail.com",
    version=__version__,
    url='https://github.com/vahtras/two_electron',
    name='two-electron',
    packages=['two'],
    install_requires=["blocked-matrix-utils", "fortran-binary", "daltools"],
    ext_modules=[ext]
)
