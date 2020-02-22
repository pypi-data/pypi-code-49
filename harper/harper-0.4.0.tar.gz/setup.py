from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="harper",
    version="0.4.0",
    description="Audio and music tools for python",
    license="MIT",
    author="Jim Ulbright",
    url="http://www.github.com/julbright/harper/",
    packages=["harper"],
    install_requires=["numpy", "matplotlib", "pyalsaaudio",],
)
