from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="outliers_removal08",
    version="1.0.0",
    description="A Python package to remove the outliers from the dataset to improve the accuracy of the model (UCS633).",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Pulkitg64/outlier_removal",
    author="Pulkit Gupta",
    author_email="pulkitgupta64@gmail.com",
    packages=["outliers_removal_101703408"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "outliers_removal08=outliers_removal_101703408.outlier:main",
        ]
    },
)