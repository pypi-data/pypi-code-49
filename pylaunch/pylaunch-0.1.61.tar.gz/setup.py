from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pylaunch",
    version="0.1.61",
    package_dir={"": "src"},
    packages=["pylaunch", "pylaunch.roku", "pylaunch.dial"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sandersland/pylaunch",
    author="Steffen Andersland",
    author_email="stefandersland@gmail.com",
    license="MIT",
    keywords=["dial", "roku"],
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    extras_require={
        "dev": ["nose==1.3.7", "twine==3.1.1", "pre-commit==2.0.1", "black==19.10b0",]
    },
)
