# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='giant',
      version='1.1.4',
      description="Giant challenge"
                  "For linux installations run this before installing:"
                  "     conda uninstall PortAudio"
                  "     sudo apt-get install portaudio19-dev."
                  "Need more help? Check the dependencies websites \n"
                  " About pysine https://pypi.org/project/pysine/ \n"
                  " About it's installation https://github.com/lneuhaus/pysine",
      url='',
      author='GSCap',
      author_email='sistemas@gscap.com.br',
      license='',
      packages=find_packages(),
      install_requires=['pycrypto', 'pysine'],
      zip_safe=False,
      python_requires='>=3.6')
