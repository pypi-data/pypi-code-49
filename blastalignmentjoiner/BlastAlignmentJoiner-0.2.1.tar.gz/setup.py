#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='BlastAlignmentJoiner',
      version='0.2.1',
      description='A program to take files in the Blast9 format and generate a set of longest contiguous alignments',
      author='Ali Sajid Imami',
      author_email='Ali.Sajid.Imami@gmail.com',
      packages=find_packages(),
      url="https://github.com/AliSajid/brain_microbiome",
      long_description=long_description,
      long_description_content_type="text/markdown",
      license="MIT",
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "Intended Audience :: Education",
          "Intended Audience :: Science/Research",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3",
          "Topic :: Scientific/Engineering :: Bio-Informatics",
      ],
      entry_points={
        "console_scripts": [
            "run_blast_aligner = run_blast_aligner:main",
        ]
    }
)
