import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wto",
    version="0.1.0",
    author="Greg LaRocca",
    author_email="larocca89@gmail.com",
    description="A Python library to query the WTO's API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LaRocca89/wto_data_puller",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    python_requires='>=3.6',
)