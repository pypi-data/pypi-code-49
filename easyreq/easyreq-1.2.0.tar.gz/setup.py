from setuptools import setup, find_packages
import os

#import global variables
import easyreq.config as conf

with open(conf.reqPath, 'r') as f:
    required = f.read().splitlines()

with open(conf.readmePath, 'r') as f:
    long_description = f.read()

setup(
    name='easyreq',
    version=conf.version,
    license='MIT',
    author='Krzysztof Janiszewski',
    author_email='krzychu.janiszewski@gmail.com',
    description='Test package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://kjaniszewski.pl',
    download_url='https://gitlab.com/Krzysidlo/easyreq',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'easyreq = easyreq.main:main'
        ]
    },
    install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
