import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arushigupta_101703106_outlier", # Replace with your own username
    version="0.0.4",
    author="Arushi Gupta",
    author_email="agupta11_be17@thapar.edu",
    description="A small package that removes outliers from a pandas dataframe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Arushi872/arushi_gupta_101703106_outlier",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)