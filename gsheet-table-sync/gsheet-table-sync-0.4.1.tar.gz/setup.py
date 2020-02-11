from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="gsheet-table-sync",
    version="0.4.1",
    packages=find_packages(exclude=['docs', 'test*']),
    install_requires=['google-api-python-client','google-auth'],
    python_requires='>=3.3',
    license='MIT',
    author='nottony',
    author_email='nottony-pypi@yahoo.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/asetiawan/gsheet_table_sync',
    description='keeping google sheet data in sync',
)
