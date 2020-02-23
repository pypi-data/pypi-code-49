import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trials",
    version="0.0.1",
    author="Kevin Miller & Larry Sleeper",
    author_email="kevinjacksonmiller@gmail.com",
    description="A Package designed to create a regulatory compliant define.XML document",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kevinjacksonm/trials",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
