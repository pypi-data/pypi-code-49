import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="mreddata", # Replace with your own username
    version="0.3.52",
    author="Matthew Breeding",
    author_email="matthew.l.breeding@vanderbilt.edu",
    description="A colletion of data and visualization tools for MRED/HDF5",
    long_description="Visit github page at https://github.com/matthew-breeding/mreddata for full details",
    long_description_content_type="text/markdown",
    url="https://github.com/matthew-breeding/mreddata",
    download_url='https://pypi.org/project/mreddata',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
