import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rohit",
    version="0.0.1",
    author="Rohit Sanjay",
    author_email="sanjay.rohit2@gmail.com",
    description="Rohit Sanjay's Python Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rohitsanj/rohit",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
