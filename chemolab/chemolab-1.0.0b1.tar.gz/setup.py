from setuptools import setup

setup(
    name='chemolab',
    description='ChemoLab is an educational based chemistry library for Python',
    packages=['chemolab', 'chemolab/core', 'chemolab/elements', 'chemolab/elements/data'],
    version='1.0.0-beta_001',
    author='MeleiDigitalMedia',
    author_email='meleidigitalmedia@gmail.com',
    url='https://github.com/MeleiDigitalMedia/ChemoLab/',
    download_url='https://github.com/MeleiDigitalMedia/ChemoLab/archive/1.0.0-beta_001.tar.gz',
    license='MIT',
    python_requires='>=3.8',
    include_package_data=True
)
