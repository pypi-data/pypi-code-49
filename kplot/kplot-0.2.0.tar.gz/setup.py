import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kplot",
    version="0.2.0",
    author="Keyan Gootkin",
    author_email="KeyanGootkin@gmail.com",
    description="A small package for making matplotlib plots pretty <3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KeyanGootkin/kplot",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={"": ["**styles/**.mplstyle"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)