import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="101703573_Missing-pkg-suruchipundir",
    version="0.0.1",
    author="Suruchi Pundir",
    author_email="suruchipundir@gmail.com",
    description="Python package to handle missing data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/suruchipundir/missing-data",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
