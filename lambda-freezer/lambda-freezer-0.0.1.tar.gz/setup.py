import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambda-freezer",
    version="0.0.1",
    author="Keith Lagrange",
    author_email="punolagrange@gmail.com",
    description="Helpers to deploy lambda functions in an immutable way",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/klagrange/lambda-freezer",
    packages=['lambda_freezer'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "boto3"
    ]
)
