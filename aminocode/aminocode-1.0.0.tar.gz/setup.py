from setuptools import setup, find_packages
 
setup(name='aminocode',
      version='1.0.0',
      author='Diogo de Jesus Soares Machado, Roberto Tadeu Raittz',
      author_email='diogomachado.bioinfo@gmail.com,',
      description='The aminocode library can be used to encode texts written in natural language in a format based on amino acids',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.rst').read(),
      zip_safe=False,
      install_requires=['numpy', 'unidecode', 'Biopython'],
      )