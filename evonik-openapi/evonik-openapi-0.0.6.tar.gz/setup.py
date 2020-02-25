import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="evonik-openapi",
    version="0.0.6",
    author="Benjamin Schiller",
    author_email="benjamin.schiller@evonik.com",
    description="Generate and merge client/server stubs using openapi-generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://evodl.visualstudio.com/openapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "uuid"
    ],
    scripts=['bin/evonik-openapi'],
)
