import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tinyserver",
    version="0.0.2",
    author="lorb",
    author_email="lorbritzer@yahoo.de",
    description="A tiny http server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/l0rb/miniserver",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    python_requires='>=3.6',
)
