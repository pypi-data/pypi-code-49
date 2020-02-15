from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'requirements.txt'), 'rb') as f:
    install_requires = f.read().decode('utf-8').split('\n')
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Local Variable Manager',
    version="1.0",
    description="CLI tool to manage local key/certs and token.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Sid Premkumar',
    author_email='sid.premkumar@gmail.com',
    url='https://sidpremkumar.com',
    license='MIT',
    install_requires=install_requires,
    packages=[
        'lvmanager',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            "lvmanager=lvmanager.main:main",
        ],
    },
)