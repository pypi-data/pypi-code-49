import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="string-routing",
    version="0.0.1",
    author="Gregory Erik",
    author_email="",
    description="A simple way to link strings to functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gregoryerik/string-routing",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
