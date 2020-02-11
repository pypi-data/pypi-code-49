from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='zpytrading',
    packages=['zpytrading'],
    version='0.0.14',
    license='MIT',
    description='Zinnion Streaming / Trading SDK',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mauro Delazeri',
    author_email='mauro@zinnion.com',
    url='https://github.com/Zinnion/zpytrading',
    download_url='https://github.com/Zinnion/zpytrading/archive/v0.0.14.tar.gz',
    keywords=['zpytrading', 'zinnion', 'sdk', 'api'],
    install_requires=[
        'pyzmq',
        'pandas',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
