import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datalake_vqd_utils", # Replace with your own username
    version="0.0.20",
    author="Casper van Houten",
    author_email="casper.vanhouten@viqtordavis.com",
    description="Package containing tools for cloud-based data lakes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
