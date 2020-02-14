import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crypto-trader-ArtifaxXx", # Replace with your own username
    version="0.0.1",
    author="ArtifaxXx",
    author_email="",
    description="A pet crypto trading project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArtifaxXx/crypto-trader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)