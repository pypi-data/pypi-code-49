from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

__name__ = "spriteutils-pkg"
__author__ = "Long Nguyen"
__copyright__= "Copyright (C) 2019, Intek Institute"
__email__ = "long.nguyen@f4.intek.edu.com"
__description__ = "Utilities for finding sprites in a sprite sheet"
__long_description_content_type__ = "text/markdown"

__version__ = "1.1.3"
__github_url__ = "https://github.com/intek-training-jsc/sprite-sheet-Long-Nguyen-96"

__language__ = "Programming Language :: Python :: 3"
__license__ = "License :: OSI Approved :: MIT License"
__os__ = "Operating System :: OS Independent"
__maintainer__ = "Long Nguyen"

__python_version__ = ">=3.7"


setup(
    install_requires=["numpy==1.18.1", "pillow==7.0.0"],
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    description=__description__,
    long_description=long_description,
    long_description_content_type=__long_description_content_type__,
    url=__github_url__,
    packages=["spriteutils"],
    package_dir={"spriteutils": "src/spriteutils"},
    classifiers=[__language__, __license__, __os__,],
    python_requires=__python_version__,
)
