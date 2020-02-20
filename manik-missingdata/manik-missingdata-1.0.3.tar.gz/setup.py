from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="manik-missingdata",
    version="1.0.3",
    description="Technique for handling missing data.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/manikmangla9/missingdata",
    author="manik mangla",
    author_email="manikmangla9@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 2.7",

    ],
    packages=["manik_missingdata"],
    include_package_data=True,
    install_requires=["pandas","numpy",],
    entry_points={
        "console_scripts": [
            "manik-missingdata=manik_missingdata.MissingData:main",
        ]
    },
)
