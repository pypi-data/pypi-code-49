import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlier_rem_101703235", # Replace with your own username
    version="0.0.1",
    author="Hitesh Gupta",
    author_email="phoenixhitesh8@gmail.com",
    description="A python package to implement outlier_removal using IQR",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/Topsis",
    packages=["hit_out_rem"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    install_requires=["requests"],
    entry_points={"console_scripts": ["outlier_remove=hit_out_rem.outlieR:main",]},
)# -*- coding: utf-8 -*-

