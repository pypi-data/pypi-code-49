import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="b22ao",
    version="0.0.1",
    author="Douglas Winter",
    author_email="douglas.winter@diamond.ac.uk",
    description="API for B22 AO operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.diamond.ac.uk/douglas/b22ao",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy', 'scipy', 'pyepics'],
    python_requires='>=3.6',
)
