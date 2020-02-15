import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="recvani",
    version="0.0.8",
    author="Anshuman kumar",
    author_email="anshuman@recvani.com",
    description="The client side python apis for making integration with recvani serveers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Recvani/python-recvani",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests']
)
