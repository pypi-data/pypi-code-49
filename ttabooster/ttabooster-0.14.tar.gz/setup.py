from setuptools import setup

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='ttabooster',
      version='0.14',
      url='https://github.com/OmriKaduri/ttabooster',
      license='MIT',
      author='Seffi Cohen, Omri Kaduri',
      author_email='Kaduriomri@gmail.com',
      description='Boost pretrained models with test time augmentation selection',
      packages=['ttabooster'],
      long_description=long_description,
      long_description_content_type='text/markdown',
      download_url='https://github.com/OmriKaduri/ttabooster/archive/0.14.zip',
      zip_safe=False,
      install_requires=[  # I get to this in a second
          'numpy>=1.17.4',
          'pandas>=0.25.3',
          'tensorflow>=2.0.0',
          'scikit-learn>=0.22'],
      )
