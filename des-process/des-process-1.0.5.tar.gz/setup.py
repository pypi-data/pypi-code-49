import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="des-process",
  install_requires=[
    "requests",
  ],
  version="1.0.5",
  author="Matheus Allein",
  author_email="mtsallein@gmail.com",
  description="A collection of functions for fetching processes and products from DES.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/linea-it/des-process",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)