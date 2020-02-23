import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="faable", # Replace with your own username
    version="1.0.0",
    author="Faable",
    author_email="marc@faable.com",
    description="Faable APIs from python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/faable/api-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)