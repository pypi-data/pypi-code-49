import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="drf-dumas",
    version="0.0.1",
    author="nakhoa",
    author_email="nakhoa17@gmail.com",
    description="tiny utils for DRF",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frangte/dumas",
    packages=['dumas'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
