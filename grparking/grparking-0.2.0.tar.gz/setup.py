import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grparking",
    version="0.2.0",
    author="Example Author",
    author_email="digitalservices@grcity.us",
    description="Packages to export, transform, and load data from The City of Grand Rapids parking systems",
    long_description_content_type="text/markdown",
    url="https://github.com/GRInnovation/parking_package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
)