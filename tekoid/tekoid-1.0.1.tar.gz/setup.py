from setuptools import setup, find_packages
import os
from codecs import open

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name="tekoid",
    version="1.0.1",
    packages=find_packages(include=["tekoid", "tekoid.*"]),
    author_email="viet.nk@teko.vn",
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=[
        'requests',
        'pyjwt',
        'cryptography'
    ],
)
