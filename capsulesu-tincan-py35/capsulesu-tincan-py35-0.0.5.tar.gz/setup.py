from setuptools import setup

setup(
    name='capsulesu-tincan-py35',
    packages=[
        'tincan',
        'tincan/conversions',
        'tincan/documents',
    ],
    version='0.0.5',
    description='A Python 3 library for implementing Tin Can API.',
    author='Devs CAPSULE Sorbonne Universite',
    author_email='dev-capsule@listes.upmc.fr',
    url='https://github.com/leveque/TinCanPython/',
    license='Apache License 2.0',
    keywords=[
        'Tin Can',
        'TinCan',
        'Tin Can API',
        'TinCanAPI',
        'Experience API',
        'xAPI',
        'SCORM',
        'AICC',
    ],
    install_requires=[
        'aniso8601',
        'pytz',
    ],
)
