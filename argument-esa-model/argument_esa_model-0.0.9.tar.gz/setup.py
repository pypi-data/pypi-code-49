import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "argument_esa_model",
    version = "0.0.9",
    author = "Yamen Ajjour",
    author_email = "yajjour@hotmail.com",
    description = "An ESA implementation in python.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://git.webis.de/args/args-topic-modeling/tree/master/src/python/esa",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
