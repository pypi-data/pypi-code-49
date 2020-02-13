import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="edafos",
    version="0.0.1-dev",
    author="Nick Machairas",
    author_email="nick@machairas.com",
    description="A Suite of Soil Mechanics Algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nickmachairas/edafos",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy==1.18.1',
        'Pint==0.10.1',
    ],
)
