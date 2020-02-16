import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stabilock4040",
    version="0.0.2",
    author="Adam Brookes",
    author_email="adam@adambrookes.co.uk",
    description="Driver for the Schlumberger/Wavetek Stabilock 4040 Communications Test Set",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/aebrookes/stabilock-4040",
    install_requires=["pyvisa"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
