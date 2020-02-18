# from distutils.core import setup
from setuptools import setup, find_packages
setup(name='sfdc_api',
      version='0.1.4dev1',
      packages=find_packages(),
      license='MIT',
      download_url='https://github.com/FernandoPicazo/sfdc_api.git',
      long_description='',
      description='A Salesforce API wrapper focused on a zero dependency development workflow')
