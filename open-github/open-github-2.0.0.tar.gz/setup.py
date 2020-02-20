import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="open-github", # Replace with your own username
    version="2.0.0",
    author="Gonzalo Vazquez",
    author_email="gvazquez@usmakestwo.io",
    description="A simple script that opens a Github page from the command line.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/usmakestwo/open_github",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)