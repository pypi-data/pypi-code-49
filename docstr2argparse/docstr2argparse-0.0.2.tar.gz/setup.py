# This Python file uses the following encoding: utf-8
from setuptools import setup, find_packages

setup(
    name='docstr2argparse',
    packages=find_packages(),
    version='0.0.2',
    description='Automatically generate CLI from a docstring.',
    author='Mateusz Krzysztof Łącki',
    author_email='matteo.lacki@gmail.com',
    url='https://github.com/MatteoLacki/docstr2argparse.git',
    keywords=['docstring parser'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'],
    # install_requires=[]
)
