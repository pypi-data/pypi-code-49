import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="forgery",
    version="0.0.1",
    author="AbdElAziz Moftah",
    author_email="abdelazizimoftah@gmail.com",
    description="Forgery and Fabrication Detection using ML.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YuP0ra/forgery",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
