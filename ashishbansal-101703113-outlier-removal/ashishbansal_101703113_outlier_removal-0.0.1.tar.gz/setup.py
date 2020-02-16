import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ashishbansal_101703113_outlier_removal", # Replace with your own username
    version="0.0.1",
    author="Ashish Bansal",
    author_email="abansal2_be17@thapar.edu",
    description="A small package that removes outliers from a pandas dataframe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)