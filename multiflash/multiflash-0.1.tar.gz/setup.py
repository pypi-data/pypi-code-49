from setuptools import setup

with open("README.md", encoding="utf8") as f:
    readme = f.read()

with open("multiflash/__init__.py", encoding="utf8") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split('"')[1]

setup(
    name="multiflash",
    description="study aid",
    long_description=readme,
    long_description_content_type="text/markdown",
    version=version,
    author="John Reese",
    author_email="john@noswap.com",
    url="https://github.com/jreese/multiflash",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    license="MIT",
    packages=["multiflash", "multiflash.tests"],
    package_data={"multiflash": ["py.typed"]},
    python_requires=">=3.7",
    setup_requires=["setuptools>=38.6.0"],
    install_requires=[],
)
