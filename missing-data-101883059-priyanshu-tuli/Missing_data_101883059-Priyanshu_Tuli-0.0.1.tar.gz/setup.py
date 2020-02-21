import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Missing_data_101883059-Priyanshu_Tuli", # Replace with your own username
    version="0.0.1",
    author="Priyanshu Tuli",
    author_email="priyanshu1tuli@gmail.com",
    description="A package for removing missing data from a dataset using Simple Imputer class",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Priyanshu0/Missing_data_removal_using_SimpleImputer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)