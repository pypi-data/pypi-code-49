import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yuDebug", # Replace with your own username
    version="1.0.0",
    author="puluterYu",
    author_email="pkmq24@qq.com",
    description="The package provides a more direct way to help students ask their questions about the errors in their codes by combining the codes and the errors to one file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pkmq24/yuDebug",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)