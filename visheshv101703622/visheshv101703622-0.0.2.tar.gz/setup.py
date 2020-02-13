import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="visheshv101703622", # Replace with your own username
    version="0.0.2",
    author="Vishesh Verma",
    author_email="visheshv2001@gmail.com",
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
         	"visheshv101703622=New.outliers:main",
	]
    },		
    python_requires='>=3.6',
)