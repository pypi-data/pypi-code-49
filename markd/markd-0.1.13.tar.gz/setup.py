"""
Project setup
"""
import os
import re
import setuptools

def envstring(var):
    """
    Get environment variable
    """
    return os.environ.get(var) or ""

# read the contents of your README file
CWD = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(CWD, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

if os.path.isfile("variables"):
    try:
        with open("variables", "r") as fh:
            VARIABLES = fh.read().strip().split("\n")
        for v in VARIABLES:
            key, value = v.split("=")
            os.environ[key] = re.sub("['\"]", "", value)
    except FileNotFoundError:
        pass


setuptools.setup(
    name="markd",
    version="0.1.13",
    author="Panagis Tselentis",
    author_email="tselentispanagis@gmail.com",
    description="A simple python markdown files generator",
    url="https://github.com/pantsel/markd",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=["markd", "markd.main"],
    # license=envstring("LICENCE"),
    classifiers=[
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries',
        'Environment :: Plugins',
    ],
)
