import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="recmodule", # Replace with your own username
    version="0.0.1",
    author="KPMG-FL",
    author_email="ukdlcloudopsfrontline@kpmg.co.uk",
    description="This module contain functions that can help make PAR easier and faster",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://stash.customappsteam.co.uk/users/dakuoko/repos/recmodule/browse",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)