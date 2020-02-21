import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clear_screen",
    version="0.1.14",
    description="A simple function for clearing a Python Interpreter/Shell",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
