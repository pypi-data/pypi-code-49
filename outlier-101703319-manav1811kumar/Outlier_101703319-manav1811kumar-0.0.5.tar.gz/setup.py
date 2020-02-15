import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Outlier_101703319-manav1811kumar", # Replace with your own username
    version="0.0.5",
    author="Manav Kumar",
    author_email="manav1811kumar@gmail.com",
    description="A package for removing the outliers from a dataset using inter quartile range(IQR)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)