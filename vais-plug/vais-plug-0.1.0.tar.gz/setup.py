import pathlib
import setuptools
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="vais-plug",
    version="0.1.0",
    description="Skeleton Plugin for VAIS analytic system",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/vais/product/analytic/skeleton-plugin-lib",
    author="Binh Nguyen",
    author_email="binhnguyen@vais.vn",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["rq==1.1.0", "requests==2.22.0", "redis==3.3.11", "prometheus_client==0.7.1", "flask==1.1.1"]
)
