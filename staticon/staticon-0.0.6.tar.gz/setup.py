import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="staticon",
    version="0.0.6",
    author="Nathan Merrill",
    author_email="mathiscool3000@gmail.com",
    description="A python library for printing pretty status messages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nathansmerrill/staticon",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)