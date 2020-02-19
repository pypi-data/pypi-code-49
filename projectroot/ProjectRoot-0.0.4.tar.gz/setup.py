import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ProjectRoot",
    version="0.0.4",
    author="Dennis Maier",
    author_email="dennis@dennis-maier.de",
    description="Sets your working dir to your project root. Add a .root_dir file to your desired directory. The script fill look it up and set's its parent dir as your working dir.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)