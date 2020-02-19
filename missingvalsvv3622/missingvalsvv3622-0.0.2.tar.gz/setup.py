import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="missingvalsvv3622", # Replace with your own username
    version="0.0.2",
    author="Vishesh Verma",
    author_email="visheshv2001@gmail.com",
    description="Use this package to replace missing values in your data by mean of columns",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" ",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
    	"console_scripts": [
         	"missingvalsvv3622=missingvals.missingvals:removeMissingValues",
	]
    }
)