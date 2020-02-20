import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deepcrawl",
    version="0.0.1",
    author="Christopher Evans",
    author_email="ce@deepcrawl.com",
    description="A package to simplify usage of the DeepCrawl REST API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DeepCrawlSEO/dc_api_wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)