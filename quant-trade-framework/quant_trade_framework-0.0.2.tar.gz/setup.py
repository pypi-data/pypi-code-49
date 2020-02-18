from setuptools import setup
import setuptools

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setup(
    name="quant_trade_framework",
    version="0.0.2",
    author="chuan.yang",
    author_email="chuan.yang0606@gmail.co,",
    description="Quant Trade Framwork",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yangchuan123/QuantTradeFramework.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)