import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="workerqueue",
    version="0.0.1",
    author="Jaeseo Park",
    description="A thread-based worker queue",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaeseopark/workerqueue",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3"
)
