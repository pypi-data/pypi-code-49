import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aryansindhi_101703110_outlier_cmd", # Replace with your own username
    version="0.0.5",
    author="Aryan Sindhi",
    author_email="asindhi_be17@thapar.edu",
    description="A small package that removes outliers from a pandas dataframe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aryansindhi18/Aryan_Sindhi_101703110_outlier_removal",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)