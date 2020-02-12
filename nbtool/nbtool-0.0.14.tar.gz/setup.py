import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nbtool", # Replace with your own username
    version="0.0.14",
    scripts=['bin/nb'],
    author="zhchangAuthor",
    author_email="zhchang@gmail.com",
    description="nb tool package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    include_package_data=True,
)
