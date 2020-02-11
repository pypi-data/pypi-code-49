import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='sinch-spectre',
    version='0.1.0',
    scripts=['bin/spectre'],
    author='Sinch Routing Team',
    author_email='max.forsman@sinch.com',
    description='CLI tool for generating API specification from a generic data model.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://www.git.clxnetworks.net/routing/spectre',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
)

