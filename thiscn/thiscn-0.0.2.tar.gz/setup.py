import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thiscn", # Replace with your own username
    version="0.0.2",
    author="Mikele",
    author_email="blive200@gmail.com",
    description="The zen of Python, English and Chinese.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/toyourheart163/thiscn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
