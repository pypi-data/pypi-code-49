from os import path

from setuptools import setup

import lvmcache2mqtt

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='lvmcache2mqtt',
    version=lvmcache2mqtt.__version__,
    description='Python module to pulish LVM cache statistics to MQTT.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JonasPed/lvmcache2mqtt',
    author='Jonas Pedersen',
    author_email='jonas@pedersen.ninja',
    license='Apache 2.0',
    packages=['lvmcache2mqtt'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6'
)
