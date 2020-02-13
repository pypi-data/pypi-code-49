from setuptools import setup

NAME = "hdy_pypi_test"
VERSION = "1.1.0"
AUTHOR = "hdy"
AUTHOR_EMAIL = "1015296415@qq.com"
URL = "https://pypi.org/project/hdy-pypi-test/"
LICENSE = "MIT"
MODULES = ["hdy_pypi_test"]
DESC = "test in Python."

setup(
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    name=NAME,
    version=VERSION,
    py_modules=MODULES,
    url = URL,
    description=DESC,
    entry_points={"console_scripts": ["hdy_pypi_test=hdy_pypi_test:hdy_pypi_test"]},
)
