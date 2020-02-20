import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my third python package", # Replace with your own username
    version="0.0.1",
    author="Parteek Satija",
    author_email="psatija_be17@thapar.edu",
    description="My third package in python related to missing values",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)