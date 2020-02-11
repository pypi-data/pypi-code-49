from setuptools import setup, find_packages

import sys
if sys.version_info.major == 3:
	import LaueTools.LaueToolsGUI
	python3entry_points = {
        'console_scripts': [
            'lauetools = LaueTools.LaueToolsGUI:start',
        ]}
else:
  python3entry_points= {}

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="LaueTools",
    version="3.0.0.28",
    packages=find_packages(),
    python_requires='>=2.6 , <3.8',

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['docutils>=0.3',
                      'numpy>=1.11.3',
                      'scipy>=0.19.0',
                      'matplotlib>=2.0.0',
                      'wxpython>=3.0',
                      'networkx>=2.1'],  # add libtiff or fabio ?

    include_package_data=True,


    # metadata for upload to PyPI
    author="J S Micha",
    author_email="micha@esrf.fr",
    description="Distribution of LaueTools Package from gitlab.esrf.fr repository for pip",
    long_description=long_description,
    long_description_content_type="text/markdown",
	
    license="MIT",
    keywords="Lauetools x-ray scattering data analysis GUI Laue",
    url="https://sourceforge.net/projects/lauetools/",  # project home page, if any
    classifiers=[
"Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
	"Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 2.7",
	"Programming Language :: Python :: 2.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	entry_points = python3entry_points,
    # could also include long_description, download_url, classifiers, etc.
)
