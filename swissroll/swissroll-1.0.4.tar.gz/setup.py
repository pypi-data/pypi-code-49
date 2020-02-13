import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="swissroll",
    version="1.0.4",
    description="Higher Level API for working with Probability Distributions.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/tirthasheshpatel/swissroll",
    author="Tirth Patel and GitHub Community",
    author_email="tirthasheshpatel@gmail.com",
    license="BSD-3-Clause",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["numpy", "scipy", "matplotlib", "sklearn"],
)
