# # # # # # # # # # # # # # # # # # # #
# Pape (a Python package)
# Copyright 2020 Carter Pape
# 
# See file LICENSE for licensing terms.
# # # # # # # # # # # # # # # # # # # #


import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name            = "pape",
    version         = "0.0.6",
    description     = "A package for personalized Python add-ons, created by Carter Pape",
    
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    
    author          = "Carter Pape",
    author_email    = "pape-python-package@carterpape.com",
    
    url         = "https://github.com/CarterPape/pape-python-package",
    packages    = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    
    python_requires = '>=3',
)
