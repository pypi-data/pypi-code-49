import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamsql", # Replace with your own username
    version="0.0.3",
    author="streamsql",
    author_email="help@streamsql.io",
    description="API package for StreamSQL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://streamsql.io",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
