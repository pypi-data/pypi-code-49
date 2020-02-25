import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="configs-adampippin",
    version="0.0.1",
    author="Adam Pippin",
    author_email="hello@adampippin.ca",
    description="Tool for transforming and working with config files containing Mozilla SOPS secrets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://adampippin.ca/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
