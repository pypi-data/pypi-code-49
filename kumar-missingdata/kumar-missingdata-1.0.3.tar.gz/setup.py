from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="kumar-missingdata",
    version="1.0.3",
    description="Technique for handling missing data.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="",
    author="kumar",
    author_email="",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 2.7",

    ],
    packages=["kumar_missingdata"],
    include_package_data=True,
    install_requires=["pandas","numpy",],
    entry_points={
        "console_scripts": [
            "kumar-missingdata=kumar_missingdata.MissingData:main",
        ]
    },
)
