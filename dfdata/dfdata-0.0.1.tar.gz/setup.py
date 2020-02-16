import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dfdata", 
    version="0.0.1",
    author="Eric Chen",
    author_email="eric.chen.2728@gmail.com",
    description="Download financial data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eric2827/DFdata",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
