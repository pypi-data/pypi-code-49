import setuptools 

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="toto-pubsub-nicolasances", # Replace with your own username
    version="1.0.0",
    author="nicolasances",
    author_email="nicolasances@gmail.com",
    description="A pubsub library for Toto",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nicolasances/py-toto-pubsub",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)