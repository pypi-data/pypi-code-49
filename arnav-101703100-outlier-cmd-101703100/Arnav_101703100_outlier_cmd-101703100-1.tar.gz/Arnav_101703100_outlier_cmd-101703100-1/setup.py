import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Arnav_101703100_outlier_cmd-101703100", # Replace with your own username
    version="1",
    author="Arnav Jain",
    author_email="ajain2_be17@thapar.edu",
    description="Outlier removal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)