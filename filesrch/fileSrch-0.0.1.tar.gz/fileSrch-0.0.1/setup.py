import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fileSrch",
    version="0.0.1",
    author="goutam",
    author_email="goutam@protonmail.ch",
    description="A simple package for searching files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/goutamenara/filemanager.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
