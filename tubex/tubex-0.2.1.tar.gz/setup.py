from setuptools import setup, find_packages

with open('requirements.txt', 'rt') as r:
    install_requires = r.read()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tubex",
    version="0.2.1",
    author="Ricky Lim",
    author_email="rlim.email@gmail.com",
    description="Command Line Interface to download MP3 from youtube and MP4 from oreilly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ricky-lim/tubex",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=install_requires,
    entry_points={"console_scripts": ["tubex=tubex.cli:cli"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
