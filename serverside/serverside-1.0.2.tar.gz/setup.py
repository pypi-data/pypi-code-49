import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="serverside",
    version="1.0.2",
    author="stacksmith",
    author_email="contact@stacksmith.co",
    description="Python serverside toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stacksmithco/python-serverside",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
