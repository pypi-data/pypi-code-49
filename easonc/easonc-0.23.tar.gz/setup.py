from setuptools import setup

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='easonc',
    version='0.23',
    description='easonc test',
    url='https://github.com/EasonC13/easonc',
    author='EasonC',
    author_email='eason.tw.chen@gmail.com',
    license='MIT',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    
)
