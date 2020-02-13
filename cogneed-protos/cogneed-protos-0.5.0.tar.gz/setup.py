import setuptools
import os


setuptools.setup(
    name="cogneed-protos",
    version=os.environ.get('VERSION'),
    packages=setuptools.find_packages(),
    install_requires=["grpcio-tools"]
)
