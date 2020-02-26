import setuptools
from setuptools import setup
setup(name='surfgen',
version='0.2.8',
description='Tools for creating slab models',
author='Zheng-Da He',
author_email='z.he@fz-juelich.de, jameshzd@mail.ustc.edu.cn, zhengdahe.electrocatalysis@gmail.com',
license='GPL-3.0',
packages=setuptools.find_packages(),
homepage='https://surfgen.readthedocs.io/en/latest/',
requires=['ase', 'pymatgen'],
zip_safe=False)
