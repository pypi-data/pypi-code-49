from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="MissingValues_101703292",
    version="1.0.2",
    description="A Python package to handle missing values in the dataset",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Kriti Pandey",
    author_email="kritip105@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["MISSING_3292"],
    include_package_data=True,
    install_requires=["numpy","pandas"],
    entry_points={
        "console_scripts": [
            "MISSING-3292=MISSING_3292.missingval_3292:main",
        ]
    },
)