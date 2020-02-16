import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="missing_values_antuanant", # Replace with your own username
    version="0.0.1",
    author="Anant Chopra",
    author_email="anantchopra95@gmail.com",
    description="Technique for filling Missing values",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Anant99-sys/Missing-values",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
