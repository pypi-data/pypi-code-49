import setuptools
import handbook

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BiostarHandbook",
    version=handbook.version,
    author="Istvan Albert",
    author_email="istvan.albert@gmail.com",
    description="Utilities for the Biostar Handbook ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/biostars/biostar-handbook-code",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=[
        'scripts/foo.sh',
        'scripts/r/foo.r',
    ],
    entry_points={
        'console_scripts': [
            'comm.py=handbook.comm:main',
            'combine.py=handbook.combine:main',
            'reformat.py=handbook.reformat:main',
            'genotype.py=handbook.genotype:main',
            'search_taxa.py=handbook.search_taxa:main',
        ],
    },

    python_requires='>=3.6',

)
