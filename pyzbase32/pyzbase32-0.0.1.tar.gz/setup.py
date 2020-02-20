import setuptools
from distutils.core import Extension

ext = Extension('pyzbase32.ext',
  sources = [
    'src/pyzbase32.c',
    'src/zbase32.c',
  ],
  depends = ['include/zbase32.h'],
  include_dirs = ['include'],
)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyzbase32",
    version="0.0.1",
    author="Tobyn Baugher",
    author_email="tobynb@gmail.com",
    description="z-base-32 encoding/decoding written in C, with an associated Python 3 module.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sr-gi/zbase32",
    packages=setuptools.find_packages(),
    ext_modules = [ext],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)