import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eltools",  # Replace with your own username
    version="1.1.0",
    author="Vitalii Balakin",
    author_email="balakinvitalyv@gmail.com",
    description="This is a simple package for elegant preprocessing procedure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
