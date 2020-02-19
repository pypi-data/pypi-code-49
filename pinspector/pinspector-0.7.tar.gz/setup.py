import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pinspector",
    version="0.7",
    author="Dinesh Ilindra",
    author_email="dinesh.iln@gmail.com",
    description="Live object inspector",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ilndinesh/pinspector",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data = True,
    python_requires='>=3.6',
)