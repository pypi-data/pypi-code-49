import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytorch_lr_finder",
    version="0.0.3",
    author="Tanjid Hasan Tonmoy",
    author_email="thtonmoy7@gmail.com",
    description="A package for finding optimal learning rate for pytorch models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Therap-ML/tanjid-lr-finder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy","pandas", "matplotlib", "torch"],
    python_requires='>=3.6',
)