from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README
setup(
    name='outlier_101703291_thapar',
    version='1.0.1',
    description='A outlier Package Project of UCS633',
    author='Krishang Dubey',
    author_email='kdubey1999@gmail.com',
    long_description="This package has been created based on Project 1 of course UCS633."
    "Krishang Dubey COE13 101703291",
    license='MIT',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Python Software Foundation License",
    ],
    packages=["outliers"],
    include_package_data=True,
    entry_points = {
        "console_scripts": [
            "outlier_101703291_thapar= outliers.Outliers:main",
        ]
    },
    )
