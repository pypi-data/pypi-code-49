from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(name='imageSegmentAnalyzer',
      version='0.20',
      description='For segmenting and analyzing images',
      keywords='Image analysis',
      url='https://github.com/CSSFrancis/empyer',
      author='CSSFrancis',
      author_email='csfrancis@wisc.edu',
      liscense='MIT',
      packages=find_packages(),
      install_requires=['numpy>=1.10,!=1.70.0',
                        'matplotlib',
                        'rawpy'],
      #  include_package_data=True, (this appearently breaks everything when you try to install the package :<)
      zip_safe=False)
