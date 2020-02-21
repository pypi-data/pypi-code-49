# encoding: utf-8

from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mld_normal_yan_werneck_tcc",
    version="0.0.5",
    author="Yan Werneck",
    author_email="yan_werneck@yahoo.com.br",
    url="https://github.com/yanwerneck/tcc",
    description="Dinamic Linear Model With Normal Distribution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license = 'MIT',
    install_requires=[
        "numpy==1.18.1",
        "pandas==1.0.1",
        "scipy==1.4.1",
        "pymc3==3.7"
    ],

    packages=["mld_normal"],
    python_requires='>=3.6',
)