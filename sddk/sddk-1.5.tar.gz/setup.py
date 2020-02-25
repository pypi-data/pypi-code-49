import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sddk", # Replace with your own username
    version="1.5",
    author="Vojtech Kase",
    author_email="vojtech.kase@gmail.com",
    description="A package to access sciencedata.dk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sdam-au/sddk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
