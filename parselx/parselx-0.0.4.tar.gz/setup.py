from setuptools import setup


NAME = "parselx"
DESCRIPTION = (
    "Enhanced version of parsel, extracting data from HTML and XML using complex rules"
)
URL = "https://github.com/wooddance/parselx"
EMAIL = "zireael.me@gmail.com"
AUTHOR = "wooddance"
VERSION = "0.0.4"
REQUIRED = ["parsel", "humanfriendly", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=open("README.rst").read(),
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    python_requires=">=3.6.0",
    install_requires=REQUIRED,
    packages=["parselx"],
)
