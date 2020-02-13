import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arshkawatra", # Replace with your own username
    version="0.0.3",
    author="Arshdeep Kawatra",
    author_email="akawatra_be17@thapar.edu",
    description="Outliers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" ",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    entry_points={
    	"console_scripts": [
         	"arshkawatra=O.outliersArsh:main",
	]
    },		
    python_requires='>=3.6',
)