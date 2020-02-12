import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outliers_101703325", # Replace with your own username
    version="0.0.1",
    author="Maninder Singhr",
    author_email="manindersinghsandhu563@gmail.com",
    description="A Simple Package to detect and remove outliers using Inter-Quatile Range",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
