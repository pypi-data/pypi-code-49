import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sslbookdata", 
    version="0.1",
    author="Oliver Obst",
    author_email="o.obst@westernsydney.edu.au",
    description="9 data sets for semi-supervised learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/oliverobst/sslbookdata",
    packages=setuptools.find_packages(),
    package_data={
        "": ["data/*.mat"], },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
