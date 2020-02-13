

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlierRemoval-kvarshney-101703295", 
    version="1.0.2",
    author="Kshitiz Varshney",
    author_email="kvarshney_be17@thapar.edu",
    description="A python package for removing outliers from a dataset using InterQuartile Range (IQR)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kv6737/outlier",
    License="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=["outlierRemoval_python"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={"console_scripts":["outlierRemoval=outlierRemoval_python.outlierRemoval:main"]},    
)
