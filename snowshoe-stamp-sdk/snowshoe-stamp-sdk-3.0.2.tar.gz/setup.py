import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="snowshoe-stamp-sdk",
    version="3.0.2",
    author="Snowshoe Stamps",
    author_email="engineering@snowshoestamp.com",
    description="SnowShoeStamp Client Api Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/snowshoestamp/snowshoe-sdk-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)