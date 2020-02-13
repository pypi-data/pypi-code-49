from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README
setup(
    name='Outliers_101703296_thapar',
    version='1.0.1',
    description='A row outlier removal Package Project of UCS633',
    author='Kuljot Singh Saggu',
    author_email='kuljot2216@gmail.com',
    long_description="This package has been created based on Project 2 of course UCS633."
    "Kuljot Singh Saggu COE14 101703296",
    license='MIT',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Python Software Foundation License",
    ],
    packages=["outliers_101703296"],
    include_package_data=True,
    entry_points = {
        "console_scripts": [
            "Outliers_101703296_thapar= outliers_101703296.remove_outliers:main",
        ]
    },
    )
