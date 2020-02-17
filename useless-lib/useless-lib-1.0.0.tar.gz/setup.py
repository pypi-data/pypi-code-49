from setuptools import setup, find_packages
from useless_lib import __version__

setup(
    name="useless-lib",
    description="...",
    long_description="",
    keywords=["useless"],
    author="Andreew Gregory",
    author_email="grinadand@gmail.com",
    url="https://github.com/1Gregory/useless-lib.git",
    # Stupid crutch
    download_url="https://github.com/1Gregory/useless-lib/archive/%s.tar.gz" % __version__,
    version=__version__,
    install_requires=[],
    packages=find_packages(),
    license="MIT",
)
