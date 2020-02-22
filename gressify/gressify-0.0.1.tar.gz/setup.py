try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open("requirements.txt") as fp:
    install_requires = fp.read()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="gressify",
    version="0.0.1",
    author="dedoussis",
    author_email="ddedoussis@gmail.com",
    description="Adds a rule on a vpc security group",
    long_description=long_description,
    keywords="aws vpc ec2 security group rule ip ingres egress",
    install_requires=install_requires.split(),
    packages=find_packages(),
    entry_points={"console_scripts": ["gressify = gressify.__main__:main"]},
)
