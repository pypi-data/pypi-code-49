import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="evonik-apitest",
    version="0.1.1",
    author="Benjamin Schiller",
    author_email="benjamin.schiller@evonik.com",
    description="Helpers for testing APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://evodl.visualstudio.com/api-test",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "exrex", "uuid", "pytest"
    ],
)
