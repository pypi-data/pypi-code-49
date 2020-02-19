from distutils.core import setup

setup(
    name='bdi_ml_utils',
    version='0.0',
    description='Utilities for ml workflows',
    author='Shlomi Uziel',
    author_email='shlomi.uziel@nielsen.com',
    packages=['bdi_ml_utils'],
    install_requires=['boto3'],
)
