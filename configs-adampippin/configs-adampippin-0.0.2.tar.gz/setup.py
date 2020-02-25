import setuptools
import io
import re

def find_version(filename):
    """Uses re to pull out the assigned value to __version__ in filename."""

    with io.open(filename, "r", encoding="utf-8") as version_file:
        version_match = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]',
                                  version_file.read(), re.M)
    if version_match:
        return version_match.group(1)
    return "0.0-version-unknown"

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="configs-adampippin",
    version=find_version("configs/__init__.py"),
    author="Adam Pippin",
    author_email="hello@adampippin.ca",
    description="Tool for transforming and working with config files containing Mozilla SOPS secrets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://adampippin.ca/",
    packages=setuptools.find_packages(),
    entry_points={'console_scripts': [ 'configs = configs.cli:cli' ]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
