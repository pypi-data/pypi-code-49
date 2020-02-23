import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytorch_lr_tuner",  # Replace with your own username
    version="0.0.1",
    author="Saif Mahmud",
    author_email="saif.dhrubo@gmail.com",
    description="Optimum learning rate finder for PyTorch Models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Therap-ML/pytorch-lr-tuner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
