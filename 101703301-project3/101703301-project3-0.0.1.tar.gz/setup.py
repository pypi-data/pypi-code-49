import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="101703301-project3", # Replace with your own username
    version="0.0.1",
    author="Kushagra-Thakral",
    author_email="kushagra.thakral@gmail.com",
    description="Handling NULL values in a dataset using backfill and forwardfill",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
