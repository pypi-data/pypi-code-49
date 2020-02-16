import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rtimbo-version",
    version="1.0.0",
    author="Rafael",
    author_email="timbo.rafa@gmail.com",
    description="Version Comparator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/timbo-rafa/version",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
