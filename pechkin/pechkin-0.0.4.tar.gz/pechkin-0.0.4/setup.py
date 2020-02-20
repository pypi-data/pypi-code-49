import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pechkin",
    version="0.0.4",
    author="Vitalii Nemchenko",
    author_email="vitalik648@gmail.com",
    description="Some tools for delivery services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VNemchenko/pechkin",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
