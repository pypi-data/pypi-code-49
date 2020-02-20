import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="citcall-devel",
    version="0.1",
    author="Citcall",
    author_email="devel@citcall.com",
    description="Citcall REST API for Python",
    long_description="Citcall REST API for Python. API support for Synchchronous Miscall, Asynchronous miscall, and SMS.",
    long_description_content_type="text/markdown",
    url="https://github.com/citcall/citcall-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)