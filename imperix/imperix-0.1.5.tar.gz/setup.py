import setuptools

with open("README.md", "r") as handle:
    long_description = handle.read()

setuptools.setup(
    name = "imperix",
    version = "0.1.5",
    description = "Imperix Node SDK including the NodeLink communication handlers that allow robots and drones to communicate with the Imperix streamers and Commander API.",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    author = "Aptus Engineering Inc.",
    author_email = "software@aptusai.com",
    url = "https://bitbucket.org/pinetree-ai/imperix-node-sdk-python3",
    packages=setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6'
)