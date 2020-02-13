import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Outlier_Removal_101883059-Priyanshu_Tuli", # Replace with your own username
    version="0.0.1",
    author="Priyanshu Tuli",
    author_email="priyanshu1tuli@gmail.com",
    description="A package for removing the outliers from a dataset using Z score",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Priyanshu0/Outlier-Removal-Using-Z-score",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)