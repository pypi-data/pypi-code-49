import setuptools
from src.fileloghelper import _VERSION

print(_VERSION)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fileloghelper",
    version=_VERSION,
    author="mithem",
    author_email="miguel.themann@gmail.com",
    description="Helper for logging to files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mithem/filelog",
    packages=["fileloghelper"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_dir={'': 'src'}
)
