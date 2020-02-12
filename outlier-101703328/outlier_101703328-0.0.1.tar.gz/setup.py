import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlier_101703328", # Replace with your own username
    version="0.0.1",
    author="Manmeet",
    author_email="manmeetkahlon2904@gmail.com",
    description="This package is used to remove outliers in a dataset.",
    url="https://github.com/manmeetkahlon/OUTLIER_101703328",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
