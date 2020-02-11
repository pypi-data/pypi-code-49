# SpectroscPy v.3
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='SpectroscPy',
      version='0.0.0',
      description='SpectroscPy: Python tools for spectroscopy.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://gitlab.com/kdu002/SpectroscPy',
      author='Karen Oda Hjorth Dundas, Magnus Ringholm, Yann Cornaton, Benedicte Ofstad',
      author_email='karen.o.dundas@uit.no',
      license='GPLv3+', 
      packages=['spectroscpy', 'spectroscpy.tests'])
