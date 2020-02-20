import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="handle-missing-csv",
    version="0.0.1",
    author="Prateek Kr Singh",
    author_email="prateekkumarsingh3@gmail.com",
    description="Handle both categorical and non-categorical missing values",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NoOne03/handle_missing_value.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
