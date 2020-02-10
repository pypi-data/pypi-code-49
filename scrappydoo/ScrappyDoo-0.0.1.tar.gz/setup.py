import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ScrappyDoo",
    version="0.0.1",
    author="Ben Knight",
    author_email="info@bknight.co.uk",
    description="Template package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/benknight135/ScrappyDoo",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)