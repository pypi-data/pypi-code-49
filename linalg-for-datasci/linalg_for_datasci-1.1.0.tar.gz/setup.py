import pathlib

from setuptools import find_packages
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="linalg_for_datasci",
    version="1.1.0",
    description="Code supporting the computational instruction for the course STAT 89A: Linear Algebra for Data Science at UC Berkeley",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/stat-89a/linalg_for_datasci",
    author="William Krinsman",
    author_email="krinsman@berkeley.edu",
    license="BSD",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: BSD License",
    ],
    packages=[
        "linalg_for_datasci",
        "linalg_for_datasci.datasets",
        "linalg_for_datasci.plotting",
        "linalg_for_datasci.widgets",
    ],
    include_package_data=True,
    install_requires=["ipywidgets", "matplotlib", "numpy", "pandas", "plotly",],
)
