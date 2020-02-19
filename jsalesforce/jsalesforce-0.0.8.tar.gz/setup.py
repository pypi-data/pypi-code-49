import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsalesforce",  # Replace with your own username
    version="0.0.8",
    author="Frederik Semmel",
    author_email="frederiksemmel@gmail.com",
    description="This package contains useful functions to extract data and write data to Salesforce. It is designed for ETH juniors only",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    py_modules=["jsalesforce"],
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["pandas >= 1.0", "simple_salesforce >= 0.25.3",],
)
