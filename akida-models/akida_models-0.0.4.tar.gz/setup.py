from os import path
from setuptools import setup, find_packages

# Read the contents of the README file
directory = path.abspath(path.dirname(__file__))
with open(path.join(directory, 'README'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='akida_models',
      version='0.0.4',
      description='Akida Models',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Corentin Friedrich',
      author_email='cfriedrich@brainchip.com',
      url='https://doc.brainchipinc.com',
      license='Apache 2.0',
      license_files=['LICENSE', 'LICENSE.3rdparty'],
      packages=find_packages(),
      install_requires=['cnn2snn>=1.7.0'],
      python_requires='>=3.6')
