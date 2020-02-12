from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="outlier-removal-101703289",
    version="1.0.2",
    description="A Python package for removing outliers in dataset using the Interquartile Range technique.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/khushgrover/outlier-removal-python",
    author="Khushnuma Grover",
    author_email="khushgrover16@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["outlier_removal"],
    include_package_data=True,
    install_requires=['pandas',
                      'numpy'
     ],
    entry_points={
        "console_scripts": [
            "remove-outlier = outlier_removal.outlier:main",
        ]
    },
)
