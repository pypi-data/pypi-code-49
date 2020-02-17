from setuptools import setup

with open("VERSION") as f:
    version = f.readline()

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="ncapi-client",
    description="Python client for NCAPI",
    version=version,
    install_requires=[
        "requests",
        "websockets",
        "click>=7.0",
        "halo",
        "tabulate",
        "tqdm",
        "nest_asyncio",
        "numpy",
        "pyyaml",
        "matplotlib",
        "ipywidgets",
        "parso>=0.5.1",
        "google-resumable-media==0.3.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "ncs = ncapi_client.ncs:safe_cli",
            "ncs-dev = ncapi_client.ncs:cli",
        ]
    },
    packages=["ncapi_client"],
    python_requires=">=3.6",
)
