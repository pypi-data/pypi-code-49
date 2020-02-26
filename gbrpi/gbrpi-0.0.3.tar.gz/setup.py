from setuptools import setup

setup(
    name='gbrpi',
    version='0.0.3',
    description='A python library for Raspberry Pi operations used for FRC',
    license='Apache License 2.0',
    packages=['gbrpi',
              'gbrpi/electronics',
              'gbrpi/net',
              'gbrpi/constants'],
    author='Ido Heinemann',
    author_email='idohaineman@gmail.com',
    keywords=['rpi', 'raspberry pi', 'frc'],
    url='https://github.com/GreenBlitz/GBRPi',
    download_url='https://github.com/GreenBlitz/GBRPi/archive/v0.0.3.tar.gz',
    install_requires=[
        'pynetworktables',
        'pigpio',
        'pyserial'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

        'Intended Audience :: Developers',  # Define that your audience are developers

        'Programming Language :: Python :: 3',  # Specify which python versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
)
