import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tableToDocument",
    version="0.0.1",
    author="Pantelis Giankoulidis",
    author_email="pgiankoulidis@isc.tuc.gr",
    description="A package for writing python datatypes to documents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pgiank28/tableToDocument",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
