import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-gql-next",
    version="0.0.1",
    author="yan darcy",
    author_email="wojiabin@live.cn",
    description="A simple python GraphQL client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wilkice/python-graphql",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)