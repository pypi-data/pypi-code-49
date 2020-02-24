import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WMSB",
    version="0.0.0",
    author="Westly Durkee",
    author_email="westsnetwork@gmail.com",
    description="A package for interfacing with the West Message Service Bus, a REST API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://upload.pypi.org/legacy/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)