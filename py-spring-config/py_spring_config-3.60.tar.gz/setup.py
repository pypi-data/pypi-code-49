from setuptools import setup, find_packages
import subprocess

with open("README.md", "r") as fh:
    long_description = fh.read()

MAJOR_VERSION = "v3."
MINOR_VERSION = subprocess.run("git rev-list --all --count".split(), stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip()
VERSION = MAJOR_VERSION + MINOR_VERSION

setup(
    name='py_spring_config',
    version='{}'.format(VERSION),
    description='Module for custom Dynaconf loader \
                to access a Spring Config server',
    long_description='',
    url='https://github.com/Receptiviti/py_spring_config',
    author="Tanya Whyte & Lucas Sant' Anna",
    author_email='twhyte@receptiviti.com',
    license='Receptiviti Inc.',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='python spring cloud config',
    packages=find_packages(exclude=['*.sh', 'tests', 'tests/*',
                                    "*.egg-info", "EGG-INFO",
                                    './dist', './build', '.*']),
    include_package_data=True,
    install_requires=['requests', 'dynaconf'],
    setup_requires=['requests-mock', 'pylint', 'twine'],
    test_suite='test',
    package_data={
        'sample': [''],
    },
)
