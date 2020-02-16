import setuptools
from os.path import join, dirname

import speech_semaphore
version = speech_semaphore.__version__

with open(join(dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as fin:
    requirements = fin.read().splitlines()

setuptools.setup(
    name='speech_semaphore',
    version=version,
    license="Apache License Version 2.0",
    author="Roman Doronin",
    python_requires=">=3.6",
    description='sinthesis speech with pauses',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    install_requires=requirements,
)
