import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Missing_Values_101703291", 
    version="0.09",
    author="Krishang Dubey",
    author_email="kdubey1999@gmail.com",
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
        'console_scripts': ['Missing_Value=Missing_Values_101703291.Missing_Values_101703291:main'],
    },
    python_requires='>=3.6',
)
