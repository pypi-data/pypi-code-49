import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="third python package", # Replace with your own username
    version="0.0.1",
    author="Nitin Berwal",
    author_email="nnitin_be17@thapar.edu",
    description="My package in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)