import re
from pathlib import Path
import setuptools


def getRequirements():
    requirements = []
    with open("requirements.txt") as f:
        requirements = f.read().splitlines()
    return requirements


def getLongDescription():
    with open("README.md", "r", encoding="utf-8") as fh:
        longDescription = fh.read()
    return longDescription


def getVersion():
    path = Path(__file__).parent.resolve() / "digiformatter" / "__init__.py"
    with open(path, "r") as fp:
        version_file = fp.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if not version_match:
        raise RuntimeError("Unable to find version string.")
    version = version_match.group(1)
    return version


setuptools.setup(
    name="digiformatter",
    version=getVersion(),
    author="DigiDuncan",
    author_email="digiduncan@gmail.com",
    description="Make your terminals look spicy.",
    long_description=getLongDescription(),
    long_description_content_type="text/markdown",
    url="https://github.com/DigiDuncan/DigiFormatter",
    python_requires=">=3",
    install_requires=getRequirements(),
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
    ]
)
