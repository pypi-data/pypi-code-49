
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pklcache",
    version="0.1",
    author="Pietro Spadaccino",
    description="Quick and dirty caching function results on disk using pickle",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MrSpadala/pklcache",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
