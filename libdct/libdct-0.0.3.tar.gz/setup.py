import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="libdct", # Replace with your own username
    version="0.0.3",
    author="Lai Yongquan",
    author_email="ranchlai@163.com",
    description="A library for audio processing by Discrete Cosine Transform (DCT) ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ranchlai/libdct",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
