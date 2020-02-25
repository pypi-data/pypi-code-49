import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nvision",
    version="1.3.0",
    author="Nipa Cloud Platform",
    author_email="devr@nipa.cloud",
    description="Nipa Cloud Platform: Nvision Python SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nipa-cloud/nvision-python",
    packages=['nvision'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
    ],
    keywords=[
        'Machine Learning',
        'Deep Learning',
        'Computer Vision',
        'Nipa Cloud Service'
    ],
    python_requires=">=3.5",
    install_requires=["requests>=2.22.0",
                      "numpy>=1.18.1",
                      "bleach>=2.1.0"])
