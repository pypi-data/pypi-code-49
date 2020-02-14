#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['Click>=7.0', 'matplotlib',
                'numpy', 'pyfiglet', 'pandas', 'pillow']

setup(
    author="Prashant Kumar Kuntala",
    author_email='prashantkuntala@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],
    description="Quality Control and Visualization utilities for Yeast Epigenome Project ",
    entry_points={
        'console_scripts': [
            'exo=exo.cli:main',
            'calculate-contrast=exo.calculate_contrast_threshold:cli',
            'fourcolor=exo.create_fourcolor_plot:cli',
            'bedtoucsc=exo.format_peaks:cli',
            'totaltagorder=exo.total_tag_ordering:cli',
            'remove-overlapping-motifs=exo.remove_overlapping_motifs:cli',
            'processbedgraph=exo.process_genome_coverage:cli',
            'makecomposite=exo.make_composite:cli',
            'motifcomposite=exo.make_motif_composite:cli',
            'mergeheatmaps=exo.merge_heatmap_png:cli',
            'makeheatmap=exo.make_heatmap:cli'
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords='exo',
    name='exo',
    packages=find_packages(include=['exo', ]),
    url='https://github.com/CEGRcode/exo',
    version='0.1.2',
)
