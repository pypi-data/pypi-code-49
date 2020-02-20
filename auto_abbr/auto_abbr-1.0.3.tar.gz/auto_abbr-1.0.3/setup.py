
import setuptools


with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name='auto_abbr',
    version='1.0.3',
    author='dandanlemuria',
    author_email='18110980003@fudan.edu.cn',
    url='https://github.com/LemuriaChen/auto_abbr',
    description='a list of abbreviations for a given string', requires=['requests', 'lxml'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
