from setuptools import setup, find_packages

setup(
    name="fileclean",
    version="0.2",
    author="Brendon Lin",
    author_email="brendon.lin@outlook.com",
    description="Package for clean local files",
    packages=find_packages(),
    entry_points={"console_scripts": ["fileclean = fileclean.view:main"]},
)
