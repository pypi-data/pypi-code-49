import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

    def find_packages(where="."):
        return [
            folder.replace("/", ".").lstrip(".")
            for (folder, _, fils) in os.walk(where)
            if "__init__.py" in fils
        ]


INSTALL_REQUIRES = ["future>=0.16.0", "requests>=2.21.0"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="doorda_sdk",
    version="1.0.11",
    author="Samuel Tan",
    author_email="samuel@doorda.com",
    description="Doorda SDK for access to Hosted Platform",
    license="Apache License 2.0",
    long_description=long_description,
    url="https://github.com/doorda/doorda-python-sdk",
    packages=["doorda_sdk"]
    + ["doorda_sdk." + i for i in find_packages("doorda_sdk")],
    package_data={"doorda_sdk": ["LICENSE", "requirements.txt"]},
    download_url="https://github.com/Doorda/doorda-python-sdk/releases/latest",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    install_requires=INSTALL_REQUIRES,
)
