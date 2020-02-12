import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tanayagarwal1", # Replace with your own username
    version="1.0.0",
    author="Tanay Agarwal",
    author_email="tanaygupta1234@gmail.com",
    description="outlier removal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" ",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "tanayagarwal1=data_project.outliers:main",
        ]
    },
    python_requires='>=3.5',
)
