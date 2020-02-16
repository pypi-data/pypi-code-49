

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Missing_Values_101703525", 
    version="0.09",
    author="Shreyansh Singhal",
    author_email="sheyansh0624@gmail.com",
    description="Python Package to find missing values in a dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['Missing_Value=Missing_Values_101703525.Missing_Values_101703525:main'],
    },
    python_requires='>=3.6',
)
