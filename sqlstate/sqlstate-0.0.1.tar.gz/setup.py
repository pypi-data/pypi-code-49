import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sqlstate",
    version="0.0.1",
    author="Andryo Marzuki",
    author_email="stabbish@gmail.com",
    description="A lightweight state framework for Python applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marzukia/sqlstate",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)