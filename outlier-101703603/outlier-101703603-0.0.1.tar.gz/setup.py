import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlier-101703603",
    version="0.0.1",
    author="Vanshika",
    author_email="angivanshikaangi@gmail.com",
    description="to remove outlier",
    url="https://github.com/vanshika-angi/outlier-removal",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
