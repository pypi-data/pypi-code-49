
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyparallelizer",
    version="1.0.0",
    author="Isaac YIMGAING",
    author_email="isaac.yimgaing@gmail.com",
    description="A package that makes it easy to create Pypi packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    keywords = ['PYTHON', 'DATAFRAME', 'MULTIPROCESSING'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 
