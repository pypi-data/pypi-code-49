
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "CHANGES"), encoding="utf-8") as f:
    version = f.readline().split()[0]

setup(
    name = "lightparse",
    version = version,
    description = "Light to use argument parser for cli tools",
    long_description = long_description,
    url = "http://keeflorin.fi/lightparse/",
    author = "Nireco",
    author_email = "marko.rasa+py@paivola.fi",
    license = "MIT",
    classifiers = [
    ],
    python_requires = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4",
    keywords = "",
    packages = find_packages(),
    install_requires = [
    ],
    extras_require = {},
    package_data = {},
    data_files = {},
    entry_points = {
        "console_scripts": [
        ],
    },
    )
