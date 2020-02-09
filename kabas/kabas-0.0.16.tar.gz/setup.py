import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="kabas",
    version="0.0.16",
    description="Sharing and collaboration tools for data experimentation",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="Pieter S.",
    author_email="",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["kabas"],
    include_package_data=True,
    data_files=[('kabas', ['kabas/config.json'])],
    install_requires=["requests", "pandas"],
    entry_points={},
)