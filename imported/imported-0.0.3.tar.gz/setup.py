"""Setup for imported package."""

from pathlib import Path
import re
from setuptools import setup, find_packages
from typing import Dict, List, Union

INSTALL_REQUIRES: List[str] = []
EXTRAS_REQUIRES: Dict[str, List[str]] = {
    "tests": [
        "pytest",
        ],
    }


def find_version(fname: Union[Path, str]) -> str:
    """Attempt to find the version number in the file fname.

    Raises RuntimeError if not found.
    """
    version = ""
    reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
    for line in Path(fname).read_text().split('\n'):
        m = reg.match(line)
        if m:
            version = m.group(1)
            break
    if not version:
        raise RuntimeError("Cannot find version information")
    return version


version = find_version('imported/__init__.py')
long_description = Path("README.md").read_text()

setup(
    name="imported",
    version=version,
    author="Brian Larsen",
    author_email="bmelarsen+imported@gmail.com",
    license='MIT',
    description="Simple function to list imported modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brl0/imported",
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
