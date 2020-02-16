import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pgtoolbox", # Replace with your own username
    version="0.0.6",
    author="Bernard Louis Alecu",
    author_email="bernard.alecu10@gmail.com",
    description="A python-postgres database toolbox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires = ['pg8000>=1.13.2'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
