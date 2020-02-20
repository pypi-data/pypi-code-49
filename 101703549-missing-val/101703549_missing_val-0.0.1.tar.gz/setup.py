import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="101703549_missing_val", # Replace with your own username
    version="0.0.1",
    author="Simranpreet kaur",
    author_email="skaur_be17@thapar.edu",
    description="a package to deal with missing values",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/missing_values",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["requests"],
    entry_points={"console_scripts":["missing-val=sin_miss.miss_val:main",]},
)