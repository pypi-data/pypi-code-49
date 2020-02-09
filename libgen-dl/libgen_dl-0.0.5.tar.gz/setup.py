import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="libgen_dl",  # Replace with your own username
    version="0.0.5",
    author="prydt",
    author_email="pranoydll@gmail.com",
    description="Download books from Library Genesis from the command line!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.prydt.xyz/pry/libgen_dl",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "appdirs==1.4.3",
        "attrs==19.3.0",
        "beautifulsoup4==4.8.2",
        "certifi==2019.11.28",
        "chardet==3.0.4",
        "Click==7.0",
        "idna==2.8",
        "lxml==4.5.0",
        "pathspec==0.7.0",
        "regex==2020.1.8",
        "requests==2.22.0",
        "soupsieve==1.9.5",
        "toml==0.10.0",
        "typed-ast==1.4.1",
        "urllib3==1.25.8",
    ],
    entry_points={
        "console_scripts": [
            "libgen_dl=libgen_dl:main",
        ]
    },
)
