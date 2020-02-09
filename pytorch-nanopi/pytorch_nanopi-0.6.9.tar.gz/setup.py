import setuptools
import pytorch_nanopi
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
NAME = pytorch_nanopi.NAME
VERSION = pytorch_nanopi.PYTORCH_VERSION


PACKAGES = setuptools.find_packages()
setuptools.setup(
    name=NAME,
    version=VERSION,
    description='This is a package for torch on nano system',
    long_description=long_description,
    author='fastbiubiu',
    author_email='fastbiubiu@163.com',
    url='https://github.com/NocoldBob/pytorch/nano',
    # package_dir=PACKAGE_DIR,
    include_package_data=True,
    install_requires=[],
    packages=PACKAGES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
