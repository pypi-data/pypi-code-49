from setuptools import setup

setup(
    name='arbdlib',
    version='1.01',
    packages=['Arbd'],
    url='https://github.com/hatchnhack/arbd-lib',
    license='GPL-3.0',
    author='Shashikant Chaudhary',
    author_email='contact@hatchnhack.com',
    install_requires=['pyfirmata'],
    description='package to control sensors and actuators present on ARBD1'
)
