import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dlake",
    version="0.1.0",
    author="Abhishek Upperwal",
    author_email="mesh@soket.in",
    description="Dynamic timer to learn the update frequency of a resource on the web",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/upperwal",
    package_dir={'src':'src'},
    packages=setuptools.find_packages(),
    py_modules=['dlake'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        'src': ['*.crt'],
    },
    include_package_data=True,
    install_requires = [
        'pymongo'
    ]
)