import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trusender-python", # Replace with your own username
    version="0.0.1",
    author="TruSender",
    author_email="bramu.ss@gmail.com",
    description="TruSender Python bindings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bramu/trusender-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

