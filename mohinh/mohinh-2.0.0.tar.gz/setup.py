import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mohinh",
    version="2.0.0",
    author="Robin Thibaut",
    author_email="Robin.Thibaut@UGent.be",
    description="A model builder package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/robinthibaut/mohinh",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['numpy', 'matplotlib']
)
