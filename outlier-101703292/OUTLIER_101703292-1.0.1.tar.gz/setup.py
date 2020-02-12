from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="OUTLIER_101703292",
    version="1.0.1",
    description="A Python package to remove outliers from a dataset",
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
    packages=["Outlier_3292"],
    include_package_data=True,
    install_requires=["numpy","pandas"],
    entry_points={
        "console_scripts": [
            "Outlier-3292=Outlier_3292.3292_outliers:main",
        ]
    },
)