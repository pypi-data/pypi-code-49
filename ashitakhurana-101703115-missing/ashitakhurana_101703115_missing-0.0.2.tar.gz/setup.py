import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ashitakhurana_101703115_missing", # Replace with your own username
    version="0.0.2",
    author="Ashita Khurana",
    author_email="ashitakhurana99@gmail.com",
    description="A small package that replaces missing values.",
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