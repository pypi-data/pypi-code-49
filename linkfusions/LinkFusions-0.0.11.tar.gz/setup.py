from setuptools import setup, find_packages
from LinkFusions import __version__

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name="LinkFusions",
    version=__version__,
    description="Python Library to Interface LinkFusions API",
    long_description='',
    author="Cloud Custom Solutions",
    packages=find_packages(),
    install_packages=[],
    include_package_data=True,
    install_requires=[
        'requests==2.22',
        'curlify==2.2.1'
    ],
    url="https://github.com/CloudPR/EM-LF-Repo",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
