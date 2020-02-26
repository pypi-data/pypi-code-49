
from setuptools import setup, find_packages
from os import path


VERSION = "v0.3.0-rc.2"

HERE = path.dirname(__file__)
with open(path.join(HERE, "README.md"), "r", encoding="utf-8") as f:
    long_description = f.read()


_install_requires = ["pc-ble-driver-py>=0.13", "cryptography", "pytz"]

setup(
    name="blatann",
    version=VERSION.lstrip("v"),  # Remove the leading v, pip doesn't like that
    description="API for controlling nRF52 connectivity devices through pc-ble-driver-py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThomasGerstenberg/blatann",
    author="Thomas Gerstenberg",
    email="tgerst6@gmail.com",
    keywords="ble bluetooth nrf52 nordic",
    packages=find_packages(exclude=["test", "test.*"]),
    install_requires=_install_requires,
    python_requires=">=3.7.*",
)
