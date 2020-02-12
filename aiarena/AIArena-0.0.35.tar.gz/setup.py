import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AIArena",
    version="0.0.35",
    author="Tristan Neate",
    author_email="tristan@neateworks.com",
    description="AIArena beta",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tristan-neateworks/AIArena",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'dill',
        'gym'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
