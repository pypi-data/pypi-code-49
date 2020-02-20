import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="usaepay", 
    version="0.0.1",
    author="usaepay",
    author_email="706@usaepay.com",
    description="sdk for usaepay rest api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://secure.usaepay.com/",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)