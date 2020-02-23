import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = '0.0.3'
setuptools.setup(
    name="soco-doc-parser-python",
    version=VERSION,
    author="kyusonglee",
    description="Python SDK for using SOCO platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.soco.ai",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Free for non-commercial use",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        "unoconv>=0.9.0",
        "boto3>=1.10.16"
    ]
)