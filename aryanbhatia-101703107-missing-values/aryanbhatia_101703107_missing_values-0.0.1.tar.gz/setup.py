import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aryanbhatia_101703107_missing_values", # Replace with your own username
    version="0.0.1",
    author="Aryan Bhatia",
    author_email="abhatia_be17@thapar.edu",
    description="A small package that replaces missing values.",
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