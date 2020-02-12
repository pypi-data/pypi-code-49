from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="outlier-removal-yash-saxena",
    version="1.0.2",
    description="A Python pip package to remove outliers from the dataset",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yashsaxena972/outlier-removal",
    author="Yash Saxena",
    author_email="yash972saxena@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["outlier_removal_yash_saxena"],
    include_package_data=True,
    install_requires=['numpy','pandas'],
    entry_points={
        "console_scripts": [
            "outliers=outlier_removal_yash_saxena.outlier:main",
        ]
    },
) 