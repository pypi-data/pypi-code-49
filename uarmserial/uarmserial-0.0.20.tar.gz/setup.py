import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uarmserial",
    version="0.0.20",
    author="Ryan Shah",
    author_email="ryan.k.shah@gmail.com",
    description="Python package for connecting to and communicating with a uARM Swift Pro robot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ryankshah/uarmserial",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
