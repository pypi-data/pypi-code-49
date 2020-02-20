import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="missing-pypck",
    version="1.0.0",
    author="Nishchay Mahajan",
    author_email="nmahajan_be17@thapar.edu",
    description="Outlier removal package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nishchaym/missing_data_py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
