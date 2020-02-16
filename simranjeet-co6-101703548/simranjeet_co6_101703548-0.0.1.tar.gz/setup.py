import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='simranjeet_co6_101703548', # Replace with your own username
    version="0.0.1",
    author="Simarpreet Singh",
    author_email="ssingh8_be17@thapar.edu",
    description="A small package that showcases topsis approach",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)