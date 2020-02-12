from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="lfdata",
    version="0.0.1",
    description="Tools for interacting with GT's LF AWESOME Receiver data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="David Richardson",
    author_email="drichardson42@gatech.edu",
    url="https://github.gatech.edu/LF-Group/lfdata",
    py_modules=["lfdata"],
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 or later "
        "(GPLv3+)",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
    ],
    install_requires=["scipy"],
    extras_require={"dev": ["twine"]},
)
