import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ccalafiore",
    version="000.000.021",
    author="Carmelo Calafiore",
    author_email="cc18849@essex.ac.uk",
    description="personal package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/ccalafiore/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
