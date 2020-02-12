import setuptools

setuptools.setup(
    name="artifacts-metadata",
    version="0.0.2",
    author="Cosmin Catalin Sanda",
    author_email="cosmin@audienceproject.com",
    description="A library for managing artifacts metadata in DynamoDB",
    long_description="A library that allows generating and storing metadata for artifacts with"
                     "complex dependencies, parameters and configuration, such as machine learning "
                     "models.",
    url="https://github.com/audienceproject/artifacts-metadata-py",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=["boto3>=1.0.0"]
)
