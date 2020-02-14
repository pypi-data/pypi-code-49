from setuptools import setup, find_packages
from gg69_expeval import __version__

setup(
    name="gg69-super-calc-engine",
    description="One line calculator engine with example of wrapping his functional",
    long_description="",
    keywords=["cool", "calc", "expeval", "calculator", "69"],
    author="Andreew Gregory",
    author_email="grinadand@gmail.com",
    url="https://github.com/1Gregory/gg69-calc-engine.git",
    # Stupid crutch
    download_url="https://github.com/1Gregory/gg69-calc-engine/archive/%s.tar.gz" % __version__,
    version=__version__,
    install_requires=[
        "colorama"
    ],
    packages=find_packages(),
    license="MIT",
)
