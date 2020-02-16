import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="missingValuesArshdeepsk", # Replace with your own username
    version="0.0.1",
    author="Arshdeep Singh",
    author_email="akawatra_be17@thapar.edu",
    description="Use this package to replace missing values in your data by mean of columns",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arshdeepsk/missingValuesArsh",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
    	"console_scripts": [
         	"missingValuesArshdeepsk=missingValues.missingValuesArsh:removeMissingValues",
	]
    }
)