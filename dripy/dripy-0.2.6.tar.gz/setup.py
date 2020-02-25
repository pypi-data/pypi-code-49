import setuptools
from pkg import name, version, author, author_email, description, install_requires

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bthornton191/dripy",
    packages=setuptools.find_packages(exclude=['test', 'pkg']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    install_requires = install_requires
)