from setuptools import setup, find_packages

setup(
    name="proust",
    version="0.0.1",
    author="Daniel Suo",
    author_email="danielsuo@gmail.com",
    description="A package for time series analysis",
    url="https://github.com/danielsuo/proust",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">3.5",
    install_requires=[
        "numpy",
        "scipy",
        "jax",
        "sklearn",
        "pandas",
        "matplotlib",
        "cython"
    ]
)