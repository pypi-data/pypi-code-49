import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlier_simran", # Replace with your own username
    version="0.0.1",
    author="Simranpreet kaur",
    author_email="skaur_be17@thapar.edu",
    description="A python package to implement outliers by interquartile",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/outlier",
    packages=["out_sim"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    install_requires=["requests"],
)# -- coding: utf-8 --

# -- coding: utf-8 --