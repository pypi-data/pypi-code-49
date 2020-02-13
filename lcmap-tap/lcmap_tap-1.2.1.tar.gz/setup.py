"""
LCMAP TAP - Timeseries Analysis and Plotting Tool package setup information
"""

from setuptools import setup, find_packages


def readme():
    """Use the README as a long description for publishing to PyPI"""
    with open("README.rst") as file:
        return file.read()


def version():
    """Returns the application version"""
    return "1.2.1"


setup(
    name="lcmap_tap",
    version=version(),
    description="A data visualization tool for PyCCD time-series model results and Landsat ARD",
    long_description=readme(),
    long_description_content_type="text/x-rst",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: Public Domain",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="usgs eros lcmap",
    url="https://github.com/USGS-EROS/lcmap-tap",
    author="USGS EROS LCMAP",
    author_email="",
    license="Unlicense",
    packages=find_packages(),
    install_requires=[
        "cython",
        "cytoolz",
        "matplotlib",
        "pandas",
        "PyQt5==5.10.1",
        "PyYaml",
        "requests",
        "lcmap-merlin==2.3.1",
    ],
    extras_require={
        "tests": ["pytest", "pytest-cov",],
        "docs": ["sphinx", "sphinx-autobuild", "sphinx_rtd_theme"],
        "deploy": ["twine"],
    },
    entry_points={"gui_scripts": ["lcmap_tap = lcmap_tap.__main__:main"]},
    python_requires=">=3.6",
    include_package_data=True,
)
