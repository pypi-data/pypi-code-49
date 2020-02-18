from setuptools import setup

def readme():
    with open('README.md', encoding="utf8") as f:
        README = f.read()
    return README


setup(
    name="topsis-pkg",
    version="1.0.0",
    author="Pulkit Gupta",
    author_email="guptapulkit48@gmail.com",
    description="A package for TOPSIS analysis.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/gupta-pulkit/topsis-pkg",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["topsis_pkg"],
    include_package_data=True,
    install_requires=["numpy", "pandas"],
    entry_points={
        "console_scripts": [
            "topsis-pkg=topsis_pkg.topsis:main",
        ]
    },
)
