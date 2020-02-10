import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outliers_aarshi", # Replace with your own username
    version="0.0.1",
    author="Aarshi Arora",
    author_email="aarshiarora50@gmail.com",
    description="A small package that removes outliers from a pandas dataframe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
