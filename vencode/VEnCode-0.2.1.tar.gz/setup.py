import setuptools
import re


def readme():
    with open("README.rst", "r") as readme_file:
        return readme_file.read()


metadata_file = "VEnCode/_metadata.py"
with open(metadata_file, "rt") as file:
    metadata = file.read()
    version_expression = r"^__version__ = ['\"]([^'\"]*)['\"]"
    author_expression = r"^__author__ = ['\"]([^'\"]*)['\"]"
    version_search = re.search(version_expression, metadata, re.M)
    author_search = re.search(author_expression, metadata, re.M)
    if version_search:
        version = version_search.group(1)
    else:
        raise RuntimeError("Unable to find version string in {}.".format(metadata))
    if author_search:
        author = author_search.group(1)
    else:
        raise RuntimeError("Unable to find author string in {}.".format(metadata))

setuptools.setup(
    name='VEnCode',
    version=version,
    description='Package to get VEnCodes as in Macedo and Gontijo, 2019',
    long_description=readme(),
    author=author,
    author_email='andre.lopes.macedo@gmail.com',
    url='https://github.com/AndreMacedo88/VEnCode',
    packages=setuptools.find_packages(),
    install_requires=[
        "biopython",
        "tqdm",
        "numpy",
        "pandas",
        "matplotlib",
        "scipy"
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]
)
