import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RKP", 
    version="0.1.0",
    author="Lennard Epping, Felix Hartkopf",
    author_email="EppingL@rki.de, HartkopfF@rki.de",
    description="Relative K-mer Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/microbial_genomics/relative-kmer-project",
    packages=setuptools.find_packages(),
    scripts=['RKP/RKP.py','RKP/create_kmers.sh', 'RKP/map_kmers.sh', 'RKP/heatmap.R'],
    install_requires=[
       "numpy == 1.17.3",
       "matplotlib == 3.1.2",
       "pandas == 0.25.3",
       "biopython == 1.76",
       "argparse == 1.4.0",
       "tqdm == 4.41.1"
   ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)