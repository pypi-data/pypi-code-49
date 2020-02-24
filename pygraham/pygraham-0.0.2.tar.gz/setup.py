import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygraham",
    version="0.0.2",
    author="Bernardi Riccardo",
    author_email="riccardo.bernardi@rocketmail.com",
    description="functional methods for python data structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/riccardobernardi/PythonFunctionalMethods",
    packages=setuptools.find_packages()+['pygraham'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    ],
)