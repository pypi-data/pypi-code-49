from setuptools import setup

NAME = "hanqingcode"
PACKAGES = "pack"
VERSION = "1.1.5"
URL = "https://pypi.org/project/hangqincode"
AUTHOR = "hdy"
AUTHOR_EMAIL = "1015296415@qq.com"
LICENSE = "MIT"
MODULES = ["hanqingcode"]
DATAFILE = ["rose.txt"]
DESC = "this is a gift for someone!"

setup(
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    name=NAME,
    version=VERSION,
    license=LICENSE,
    url=URL,
    data_files=DATAFILE,
    py_modules=MODULES,
    description=DESC,
    entry_points={"console_scripts": ["hanqingcode = hanqingcode:main"]},
)
