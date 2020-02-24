import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autosolveclient", # Replace with your own username
    version="0.0.3",
    author="Aycd Inc",
    author_email="contact@aycd.io",
    description="Client module for connecting to the Aycd Autosolve Network",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pika',
        'requests',
        'asyncio',
        'logger'
    ],
    python_requires='>=3.6',
)