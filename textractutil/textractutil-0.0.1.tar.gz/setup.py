import setuptools

with open("README.md", "r") as f:
	readme_description = f.read()

setuptools.setup(
	name="textractutil",
	version="0.0.1",
	author="Yifan Wu",
	author_email="yw693@cornell.edu",
	description="Python utilities for parsing AWS Textract results.",
	long_description=readme_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.3",
    install_requires=[
        "pyyaml>=5.1,<=5.2"
    ]
)

