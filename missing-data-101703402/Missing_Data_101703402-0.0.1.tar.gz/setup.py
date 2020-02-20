import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name="Missing_Data_101703402", # Replace with your own username
    version="0.0.1",
    author="Pratyaksh Verma",
    author_email="pverma_be17@thapar.edu",
    description="Missing Data filling",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
python_requires='>=3.6',
)