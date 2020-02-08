import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlier-remover-csv",
    version="1.0.6",
    author="Prateek kr Singh",
    author_email="prateekkumarsingh3@gmail.com",
    description="Outlier remover tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NoOne03/outlier_remover.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
