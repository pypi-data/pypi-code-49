import setuptools
with open("README.MD", "r") as inFile:
    long_description = inFile.read()

setuptools.setup(
    name="station-tools",
    version="0.1.2",
    author="Bob Fogg",
    author_email="bob.fogg@celltracktech.com",
    description="A package for managing and analyzing CTT LifeTag datasets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bobfogg/sensor-station-tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)