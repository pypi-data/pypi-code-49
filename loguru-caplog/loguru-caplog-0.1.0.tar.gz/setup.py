import pathlib

from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent


def read(file_name: str) -> str:
    return (HERE / file_name).read_text("utf-8").strip()


setup(
    name="loguru-caplog",
    version="0.1.0",
    packages=find_packages(
        exclude=["tests", "tests.*", "*.tests.*", "*.tests"]
    ),
    python_requires=">=3.6",
    install_requires=["loguru==0.4.1", "pytest==5.3.5"],
    author="Dinn757",
    description="Сaptures loguru logging output",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
)
