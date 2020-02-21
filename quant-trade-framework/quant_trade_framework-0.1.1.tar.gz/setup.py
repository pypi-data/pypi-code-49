from setuptools import setup
import setuptools

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setup(
    name="quant_trade_framework",
    version="0.1.1",
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
    setup_requires=[
        # "pyecharts==1.6.2",
        # "matplotlib==3.1.1",
        # "peewee==3.11.2",
        # "pytz==2019.3",
        # "requests==2.22.0",
        # "SQLAlchemy==1.3.10",
        # "pymongo==3.9.0",
        # "jqdatasdk==1.7.5",
        # "redis==3.3.11",
        # "numpy==1.17.3",
        # "pandas==0.24.0",
        # "dataclasses==0.7",
        # "strategies==0.2.3"
    ],
    install_requires=[
        "pyecharts",
        "matplotlib",
        "peewee",
        "pytz",
        "requests",
        "SQLAlchemy",
        "pymongo",
        "jqdatasdk",
        "redis",
        "numpy",
        "pandas",
        "dataclasses",
        "strategies"
    ],
    python_requires='>=3.6',
)