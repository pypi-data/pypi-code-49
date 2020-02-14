# python3 setup.py sdist bdist_wheel

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="makeover",
    version="0.0.1",
    description="this package automatically generates visualization dashboard of given data",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/zahash/makeover",
    author="zahash",
    author_email="zahash.z@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["makeover"],
    include_package_data=True,
    install_requires=["pandas", "dash"],
    entry_points={
        "console_scripts": [
            "makeover=makeover.__main__:main",
        ]
    },
)
