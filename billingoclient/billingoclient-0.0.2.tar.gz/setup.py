import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="billingoclient",
    version="0.0.2",
    author="Mocsar Kalman",
    author_email="mocsar@yusp.com",
    description="Python package to access billingo rest api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests>=2.23.0', 'PyJWT>=1.7.1'],
    python_requires='>=3.7',
)
