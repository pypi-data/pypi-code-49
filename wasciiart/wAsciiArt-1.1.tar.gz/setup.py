from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="wAsciiArt",
    version="1.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    author="witrdotnet",
    author_email="witr.net@gmail.com",
    description="Provides ascii art representation of witrdotnet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/witrdotnet/wAsciiArt",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.0',
)
