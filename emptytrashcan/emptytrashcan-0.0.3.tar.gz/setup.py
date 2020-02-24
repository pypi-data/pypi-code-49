import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="emptytrashcan",  # Replace with your own username
    version="0.0.3",
    author="Larbi Gharib",
    author_email="larbizard@gmail.com",
    description="A simple function to emtpy your linux trashcan",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/larbizard/emptytrashcan",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
