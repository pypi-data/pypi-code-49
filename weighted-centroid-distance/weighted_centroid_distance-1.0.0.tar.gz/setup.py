import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weighted_centroid_distance",
    version="1.0.0",
    author="duexai",
    author_email="contact@duex.ai",
    description="Python serverside toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/duexai/weighted-centroid-distance",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
