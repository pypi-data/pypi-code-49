import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latex2sympy-custom4", # Replace with your own username
    version="0.0.2",
    author="presidentkevvol",
    author_email="helsinkiwhite@gmail.com",
    description="A simple rearrangement and packaged version of augustt198's latex2sympy using ANTLR",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
