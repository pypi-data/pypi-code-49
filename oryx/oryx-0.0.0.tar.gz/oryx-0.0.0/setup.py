from setuptools import setup, find_packages

setup(
    name='oryx',
    packages=find_packages(exclude=["examples"]),
    python_requires='>=3.7'
)
