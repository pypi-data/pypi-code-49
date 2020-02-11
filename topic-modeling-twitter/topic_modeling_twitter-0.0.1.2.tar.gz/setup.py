import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topic_modeling_twitter", # Replace with your own username
    version="0.0.1.2",
    author="Parisa Zahedi",
    author_email="p.zahedi@uu.nl",
    description="a package with topic-modeling solutions for twitter data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)