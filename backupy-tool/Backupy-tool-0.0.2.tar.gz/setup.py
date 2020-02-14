from setuptools import find_packages, setup
from os import path


def readme():
    curr = path.abspath(path.dirname(__file__))
    with open(path.join(curr, 'README.md')) as f:
        content = f.read()
    return content


setup(
    name="Backupy-tool",
    version="0.0.2",
    description="Python script for backup files, directories and databases. Save your data from loss or damage.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/KonstantinPankratov/Backupy",
    author="Konstantin Pankratov",
    author_email="hello@kopa.pw",
    license="MIT",
    keywords=["backup", "backup script", "backup utility", "backup database", 'backup mysql'],
    install_requires=[
        "pytest"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
)