import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MissingValues_Arsh", # Replace with your own username
    version="0.0.2",
    author="Arshpreet Singh",
    author_email="asingh9_be17@thapar.edu",
    description="Treating Missing values in a dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)