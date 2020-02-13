import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="101703312_outlierRemoval", 
    version="1.0.0",
    author="Lovish Jindal",
    author_email="ljindal1_be17@thapar.edu",
    description="A python package for removing outliers from a dataset using InterQuartile Range (IQR)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    License="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=["outlier_python"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={"console_scripts":["outlierRemoval=outlier_python.outlierRemoval:main"]},    
)
