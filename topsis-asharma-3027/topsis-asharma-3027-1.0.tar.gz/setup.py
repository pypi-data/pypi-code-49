from setuptools import *

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="topsis-asharma-3027",
    version="1.0",
    description="Topsis analysis of a csv file",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="abhishek sharma",
    author_email="asharma1_be17@thapar.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["TOPSIS_package"],
    include_package_data=True,
    install_requires=["numpy","pandas"],
    entry_points={
        "console_scripts": [
            "topsisB=TOPSIS_package.cli:main",
        ]
    },
)