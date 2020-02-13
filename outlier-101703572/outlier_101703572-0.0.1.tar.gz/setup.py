from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="outlier_101703572",
    version="0.0.1",
    description="Python package to remove outliers from csv file(row removal)",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/sunvir72",
    author="Sunvir Singh",
    author_email="sunvirsingh72@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["outlier_101703572"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "outlier-101703572=outlier_101703572.__init__:main",
        ]
    },
)
