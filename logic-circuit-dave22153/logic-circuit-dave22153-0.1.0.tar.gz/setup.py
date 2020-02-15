"""Setup package for logic_circuit.
"""

from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="logic-circuit-dave22153",
    version="0.1.0",
    description="Logic circuit creation and viewing utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Dave22153",
    author_email="dkanekanian@gmail.com",
    url="https://gitlab.com/fruity-games/logic-circuit",
    packages=find_namespace_packages(include=["logic_circuit.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    python_requires=">=3.2")
