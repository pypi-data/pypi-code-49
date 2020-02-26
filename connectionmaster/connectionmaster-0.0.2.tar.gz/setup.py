import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="connectionmaster",
    version="0.0.2",
    author="Nathan Merrill",
    author_email="mathiscool3000@gmail.com",
    description="A python utility for remote server management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nathansmerrill/connectionmaster",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)