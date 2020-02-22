from setuptools import *

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="topsis-priyank_raheja-101703404",
    version="1.0",
    description="Topsis analysis",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="priyank raheja",
    author_email="praheja_be17@thapar.edu",
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
