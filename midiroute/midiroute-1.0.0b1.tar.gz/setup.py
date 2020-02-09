"""A command line utility for routing and monitoring MIDI ports."""

import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).absolute().parent

# Get the long description from the README file
with open(str(pathlib.Path(here, "README.md")), encoding="utf-8") as f:
    long_description = f.read()

PROJECT_NAME = "midiroute"
DESCRIPTION = __doc__
INSTALL_REQUIRES = ["click", "mido", "python-rtmidi", "tabulate"]
EXTRAS_REQUIRE = {
    "tests": ["pytest", "pytest-asyncio", "asynctest", "coverage[toml]>=5.0.2"],
}
EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["tests"] + ["pre-commit"]
EXTRAS_REQUIRE["azure-pipelines"] = EXTRAS_REQUIRE["tests"] + ["pytest-azurepipelines"]

setup(
    name=PROJECT_NAME,
    version="1.0.0-beta.1",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rwalton00/midiroute",
    author="Rob Walton",
    author_email="rwalton00@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="midi interface router monitor diagnostics",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6, <4",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    entry_points={"console_scripts": ["midiroute=midiroute.main:main"]},
)
