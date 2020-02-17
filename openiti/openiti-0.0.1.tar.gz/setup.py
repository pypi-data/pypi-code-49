import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openiti", # Replace with your own username
    version="0.0.1",
    author="Soheil Merchant, Maxim Romanov, Masoumeh Seydi, Peter Verkinderen",
    author_email="peter.verkinderen@gmail.com",
    description="A package for dealing with the openITI corpus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://https://github.com/OpenITI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
