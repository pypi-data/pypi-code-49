from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

install_requires = ['p_tqdm', 'pandas', 'numpy', 'scipy', 'scikit-learn', 'sympy', 'boto3']

setup(name='kidaura_ds',
      version=version,
      description='Kidaura data science module',
      author='Paras Sharmaa',
      author_email='paras@kidaura.com',
      license='MIT',
      packages=find_packages(include=('kds',)),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires)
