import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="missing_data", 
    version="1.0.0",
    author="Tanay Agarwal",
    author_email="tanaygupta1234@gmail.com",
    description="Missing Values",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    entry_points={
    	"console_scripts": [
            "missing_data=package.missing_data:missing_data"
    	]
    },
    python_requires='>=3.5',
)
