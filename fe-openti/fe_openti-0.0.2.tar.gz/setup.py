from setuptools import setup, find_packages
setup(
  name = 'fe_openti',
  packages = find_packages(), # this must be the same as the name above
  version = '0.0.2',
  description = 'this module add changes to fe of openti',
  author = 'Abiezer Sifontes',
  author_email = 'ajsifontes@urbos.io',
  url = 'https://github.com/UrbosSmartCity/fe_openti', # use the URL to the github repo
  download_url = 'https://github.com/RDCH106/urbossmartcity/fe_openti/archive/0.0.1.tar.gz',
  classifiers=['Programming Language :: Python',  # Clasificadores de compatibilidad con versiones de Python para tu paqeute
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7'],
)
