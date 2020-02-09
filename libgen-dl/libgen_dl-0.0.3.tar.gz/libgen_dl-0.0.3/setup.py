import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="libgen_dl",  # Replace with your own username
    version="0.0.3",
    author="prydt",
    author_email="pranoydll@gmail.com",
    description="Download books from Library Genesis from the command line!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.prydt.xyz/pry/libgen_dl",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "libgen_dl=libgen_dl:main",
        ]
    },
)
