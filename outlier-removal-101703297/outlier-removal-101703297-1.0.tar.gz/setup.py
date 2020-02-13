from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="outlier-removal-101703297",
    version="1.0",
    description="A Python package for removing outliers in dataset using the Interquartile Range technique.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/kanchitbajaj8070/outlier-removal-101703297",
    author="kunal bajaj",
    author_email="kanchitbajaj8070@gmail.com",
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
            "remove-outliers = outlier_removal.outlier:main",
        ]
    },
)
