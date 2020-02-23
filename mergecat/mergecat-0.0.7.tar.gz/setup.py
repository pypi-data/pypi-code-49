import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mergecat",
    version="0.0.7",
    author="Ian Moore",
    author_email="mergecat@yttr.org",
    description="Automatic voice line clip extractor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yttrian/mergecat",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "mergecat = mergecat.__main__:mergecat"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "click"
    ]
)
