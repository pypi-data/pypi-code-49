import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outliers_101703144", # Replace with your own username
    version="0.0.1",
    author="BHUPINDER KUMAR",
    author_email="bkumar_be17@thapar.edu",
    description="A Simple Package to detect and remove outliers using Inter-Quatile Range",
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
