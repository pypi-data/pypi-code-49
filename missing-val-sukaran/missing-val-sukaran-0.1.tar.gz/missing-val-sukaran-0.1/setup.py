import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="missing-val-sukaran", # Replace with your own username
    version="0.1",
    author="Sukaran Grover 101753016 TIET",
    author_email="sgsoxy8@gmail.com",
    description="A small missing values package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sukaran/Remove-NaN",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)