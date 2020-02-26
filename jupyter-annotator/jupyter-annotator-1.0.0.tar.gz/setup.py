import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jupyter-annotator",
    version="1.0.0",
    author="Shih-hong Tsai",
    author_email="doublebeet@gmail.com",
    description="This package provides an annotation UI for arbitrary dataset in json format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DoubleBite/jupyter-annotator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)