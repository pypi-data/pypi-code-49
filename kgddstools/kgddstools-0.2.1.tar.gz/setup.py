from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name = 'kgddstools',
     version = '0.2.1',
     #scripts = ['kgddstools'] ,

     author = "Kelvin Ducray",
     author_email = "kelvin.ducray@gmail.com",

     description = "Data science functions for convience",
     long_description = long_description,
     long_description_content_type = "text/markdown",

     url = "https://github.com/kelvinducray/kgddstools",
     packages = find_packages(),#exclude=['docs', 'tests*']),

     classifiers = [
         "Programming Language :: Python :: 3",
         "License :: Public Domain",
         "Operating System :: OS Independent",
     ],
 )
