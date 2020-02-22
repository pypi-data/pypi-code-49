import setuptools
from mftoolbox import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mftoolbox",
    version="4.0.2",
    author="Celso Oliveira",
    author_email="c.oliveira@live.com",
    description="A set of tools to support my MF2 and MagicFII projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/coliveira2001/mftoolbox",
    packages=['mftoolbox'], #setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[            # I get to this in a second
        'configparser',
        'zeep',
        'lxml',
        'bs4',
        'selenium',
      ],
    python_requires='>=3.5',
)