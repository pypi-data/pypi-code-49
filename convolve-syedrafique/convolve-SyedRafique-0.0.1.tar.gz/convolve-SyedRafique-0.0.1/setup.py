import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="convolve-SyedRafique",
    version="0.0.1",
    author="syed hamza rafique",
    author_email="syedrafique2016@gmail.com",
    description="image processsing package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[],
    python_requires='>=3.6',
)
