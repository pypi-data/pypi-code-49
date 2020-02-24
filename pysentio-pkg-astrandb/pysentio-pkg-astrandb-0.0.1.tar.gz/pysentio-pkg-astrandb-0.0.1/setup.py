import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysentio-pkg-astrandb", 
    version="0.0.1",
    author="Ake Strandberg",
    author_email="ake@strandberg.eu",
    description="Python library for Sentio Pro Sauna Controller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/astrandb/pysentio",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
