import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlier-akashjindal347", # Replace with your own username
    version="0.0.1",
    author="Akash Jindal",
    author_email="akashjindal347@gmail.com",
    description="Outlier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akashjindal347/Python-Packages",
    packages=["outlier"],
    include_package_data = True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)