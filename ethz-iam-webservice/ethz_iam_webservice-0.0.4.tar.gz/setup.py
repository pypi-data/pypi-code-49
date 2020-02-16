import sys

if sys.version_info < (3,3):
    sys.exit('Sorry, Python < 3.3 is not supported')

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='ethz_iam_webservice',
    version= '0.0.4',
    author='Swen Vermeul |  ID SIS | ETH Zürich',
    author_email='swen@ethz.ch',
    description='Manage users, groups and services of the ETH Identity and Access Management system (IAM)',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.ethz.ch/vermeul/ethz-iam-webservice',
    packages=find_packages(),
    license='Apache Software License Version 2.0',
    install_requires=[
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    zip_safe=False,
)
