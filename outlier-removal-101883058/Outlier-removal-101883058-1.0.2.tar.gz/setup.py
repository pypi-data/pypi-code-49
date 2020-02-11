from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="Outlier-removal-101883058",
    version="1.0.2",
    description="Removing outliers using IQR(Interquartile) range(25%-75%).",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Pritpal SIngh Pruthi",
    author_email="psp.ps001@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
        "Programming Language :: Python :: 3.7",
    ],
    packages=["pritpal_singh_remove_outliers"],
    include_package_data=True,
    install_requires=["numpy","pandas"],
    entry_points={
        "console_scripts": [
            "outliers=pritpal_singh_remove_outliers.outliers:main",
        ]
    },
)
