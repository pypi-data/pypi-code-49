from setuptools import setup, find_packages
from runpy import run_path as run_path
import os

here = os.path.abspath(os.path.dirname(__file__))

d = run_path(os.path.join(here, "hgfluiddyn/_version.py"))
__version__ = d["__version__"]

setup(
    version=__version__, packages=find_packages(exclude=["doc", "tmp"]),
)
