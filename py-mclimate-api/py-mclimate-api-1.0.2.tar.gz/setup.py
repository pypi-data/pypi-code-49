import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-mclimate-api",
    version="1.0.2",
    author="MClimate",
    author_email="hi@seemelissa.com",
    description="MClimate API Wrapper in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pernichev/mclimate_api_wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)