import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="database-manager",
    version="0.0.21",
    author="Shane Byers",
    author_email="shane@shane-byers.com",
    description="Database Manager for MySQL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShaneBByers/DatabaseManager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'mysql-connector',
    ],
    python_requires='>=3.6',
)
