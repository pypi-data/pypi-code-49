import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="option-price", 
    version="0.1.4",
    author="QSCTech-Sange",
    author_email="3160105521@zju.edu.cn",
    description="Awesome but light option price calculator in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://qsctech-sange.github.io/option-price",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
